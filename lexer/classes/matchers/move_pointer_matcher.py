from lexer.classes.definitions.tokens import Tokens
from lexer.classes.tokenizer import Tokenizer
from lexer.classes.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class MovePointerMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.MV_PTR:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return Tokens.PointerRight
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return Tokens.PointerLeft
        else:
            tokenizer.rollback_snapshot()
            return False
