from classes.definitions.tokens import Tokens
from classes.definitions.keywords import Keywords
from classes.tokenizer import Tokenizer
from .baselanguage_matcher import BaseLanguageMatcher


class EditCellMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: BaseLanguageMatcher.BaseWordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.IO_CHAR:
            if baseword_order == BaseLanguageMatcher.BaseWordOrder.LR:
                return Tokens.OutputCharCell
            elif baseword_order == BaseLanguageMatcher.BaseWordOrder.RL:
                return Tokens.InputCharCell
        else:
            tokenizer.rollback_snapshot()
            return False
