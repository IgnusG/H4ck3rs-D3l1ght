from lexer.definitions.tokens import DecrementCell
from lexer.definitions.tokens import IncrementCell
from lexer.tokenizer import Tokenizer

from lexer.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class EditCellMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.E_CELL:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return IncrementCell()
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return DecrementCell()
        else:
            tokenizer.rollback_snapshot()
            return False
