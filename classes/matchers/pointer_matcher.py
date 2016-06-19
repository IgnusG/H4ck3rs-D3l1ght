from classes.definitions.tokens import Tokens
from classes.definitions.keywords import Keywords
from classes.tokenizer import Tokenizer
from .baselanguage_matcher import BaseLanguageMatcher


class PointerMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: BaseLanguageMatcher.BaseWordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.MV_PTR:
            if baseword_order == BaseLanguageMatcher.BaseWordOrder.LR:
                return Tokens.PointerRight
            elif baseword_order == BaseLanguageMatcher.BaseWordOrder.RL:
                return Tokens.PointerLeft
        else:
            tokenizer.rollback_snapshot()
            return False
