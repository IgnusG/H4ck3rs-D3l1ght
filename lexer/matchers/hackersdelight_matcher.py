from enum import Enum

from lexer.tokenizer import Tokenizer
from lexer.warnings import Warnings

from helpers.error_handling import HackersWarning
from lexer.definitions.keywords import Keywords


class HackersDelightMatcher:
    class WordOrder(Enum):
        HD = 1
        DH = 2

    class LazyPersonDetected(HackersWarning):
        def __init__(self, pointer, used_alternative, suggested_word):
            super(HackersDelightMatcher.LazyPersonDetected, self).__init__(pointer)
            self.used_alternative = used_alternative
            self.suggested_word = suggested_word

    @staticmethod
    def match(tokenizer: Tokenizer):
        tokenizer.take_snapshot()

        first_word = HackersDelightMatcher.match_baseword(tokenizer)
        second_word = HackersDelightMatcher.match_baseword(tokenizer) if first_word else False
        couple = (first_word, second_word)

        if couple == (Keywords.HACK, Keywords.DEL):
            tokenizer.purge_snapshot()
            return HackersDelightMatcher.WordOrder.HD
        if couple == (Keywords.DEL, Keywords.HACK):
            tokenizer.purge_snapshot()
            return HackersDelightMatcher.WordOrder.DH

        tokenizer.rollback_snapshot()
        return False

    @staticmethod
    def match_baseword(tokenizer: Tokenizer) -> Keywords:
        token_word = ''
        matched_word = ''
        pointer = tokenizer.pointer_at()

        auxiliary_keywords = Keywords.HACK_AUX + Keywords.DEL_AUX
        all_keywords = (Keywords.HACK, Keywords.DEL) + auxiliary_keywords

        while not tokenizer.reached_end():
            one_matched = False
            token_word += tokenizer.peek()
            for word in all_keywords:
                if word.startswith(token_word):
                    if not one_matched:
                        tokenizer.consume()
                    one_matched = True

                    if word == token_word:
                        if matched_word:
                            tokenizer.purge_snapshot()
                        tokenizer.take_snapshot()
                        matched_word = word
                        break
            else:
                if not one_matched and matched_word:
                    tokenizer.rollback_snapshot()
                    break
                if not one_matched and not matched_word:
                    return False
        else:
            return False

        if matched_word in auxiliary_keywords:
            auxiliary_word = matched_word
            matched_word = Keywords.HACK if matched_word in Keywords.HACK_AUX else Keywords.DEL
            Warnings.add_warning(HackersDelightMatcher.LazyPersonDetected(pointer, auxiliary_word, matched_word))

        return matched_word
