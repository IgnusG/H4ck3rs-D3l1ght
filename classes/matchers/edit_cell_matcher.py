from classes.definitions.tokens import Tokens
from classes.definitions.keywords import Keywords
from classes.tokenizer import Tokenizer
from .baselanguage_matcher import BaseLanguageMatcher


class EditCellMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: BaseLanguageMatcher.BaseWordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.E_CELL:
            if baseword_order == BaseLanguageMatcher.BaseWordOrder.LR:
                return Tokens.IncrementCell
            elif baseword_order == BaseLanguageMatcher.BaseWordOrder.RL:
                return Tokens.DecrementCell
        else:
            tokenizer.rollback_snapshot()
            return False
