from classes.definitions.tokens import Tokens
from classes.definitions.keywords import Keywords
from classes.tokenizer import Tokenizer
from .hackersdelight_matcher import HackersDelightMatcher


class EditCellMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.E_CELL:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return Tokens.IncrementCell
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return Tokens.DecrementCell
        else:
            tokenizer.rollback_snapshot()
            return False
