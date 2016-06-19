from enum import Enum

from classes.definitions.keywords import Keywords
from classes.tokenizer import Tokenizer
from classes.warnings import Warnings


class HackersDelightMatcher:
    class WordOrder(Enum):
        HD = 1
        DH = 2

    class LazyPersonDetected(Warning):
        def __init__(self, pointer, used_alternative, suggested_word):
            self.pointer = pointer
            self.used_alternative = used_alternative
            self.suggested_word = suggested_word

    @staticmethod
    def match(tokenizer: Tokenizer):
        tokenizer.take_snapshot()

        first_word = HackersDelightMatcher.match_baseword(tokenizer)
        second_word = HackersDelightMatcher.match_baseword(tokenizer) if first_word else False
        couple = (first_word, second_word)

        if couple == (Keywords.HACK, Keywords.DEL):
            return HackersDelightMatcher.WordOrder.HD
        if couple == (Keywords.DEL, Keywords.HACK):
            return HackersDelightMatcher.WordOrder.DH

        tokenizer.rollback_snapshot()
        return False

    @staticmethod
    def match_baseword(tokenizer: Tokenizer) -> Keywords:
        token_string = tokenizer.consume()
        token_pointer = 1

        # TODO: This needs to go inside the loop: Alternatives should be considered for the first character as well
        if token_string == Keywords.HACK[0]:
            suggested_word = Keywords.HACK
            alternatives = Keywords.HACK_AUX
        elif token_string == Keywords.DEL[0]:
            suggested_word = Keywords.DEL
            alternatives = Keywords.DEL_AUX
        else:
            return False

        while not tokenizer.reached_end():
            token_char = tokenizer.peek()
            if not suggested_word[token_pointer] == token_char:
                for alt in alternatives:
                    if alt[token_pointer] == token_char:
                        Warnings.add_warning(
                            HackersDelightMatcher.LazyPersonDetected(tokenizer.pointer_at, alt, suggested_word))
                        break
                else:
                    return False

            token_pointer += 1
            tokenizer.consume()

        return True
