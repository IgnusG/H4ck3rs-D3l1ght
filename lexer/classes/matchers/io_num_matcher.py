from lexer.classes.definitions.tokens import Tokens
from lexer.classes.tokenizer import Tokenizer
from lexer.classes.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class EditCellMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.IO_NUM:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return Tokens.OutputNumCell
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return Tokens.InputNumCell
        else:
            tokenizer.rollback_snapshot()
            return False
