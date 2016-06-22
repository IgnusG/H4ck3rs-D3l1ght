from lexer.tokenizer import Tokenizer

from lexer.definitions.tokens import Integer


class IntegerMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer):
        token_string = ''
        word_start_pointer = tokenizer.pointer_at()

        while not tokenizer.reached_end():
            if not tokenizer.peek().isdigit():
                break
            token_string += tokenizer.consume()

        return Integer(word_start_pointer, int(token_string)) if token_string else False
