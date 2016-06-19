from classes.definitions.tokens import Tokens
from classes.definitions.keywords import Keywords
from classes.tokenizer import Tokenizer
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
