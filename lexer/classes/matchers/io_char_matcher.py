from lexer.classes.definitions.tokens import InputCharCell
from lexer.classes.definitions.tokens import OutputCharCell
from lexer.classes.tokenizer import Tokenizer
from lexer.classes.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class IOCharMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.IO_CHAR:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return OutputCharCell()
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return InputCharCell()
        else:
            tokenizer.rollback_snapshot()
            return False
