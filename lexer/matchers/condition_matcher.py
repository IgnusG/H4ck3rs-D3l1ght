from lexer.definitions.tokens import Condition, JumpBack
from lexer.tokenizer import Tokenizer

from lexer.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class ConditionMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder, pointer):
        tokenizer.take_snapshot()

        if not tokenizer.reached_end() and tokenizer.consume() == Keywords.COND:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return Condition(pointer)
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return JumpBack(pointer)
        else:
            tokenizer.rollback_snapshot()
            return False
