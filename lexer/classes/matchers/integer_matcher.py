from lexer.classes.tokenizer import Tokenizer
from lexer.classes.definitions.tokens import Tokens


class IntegerMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer):
        token_string = ''

        while not tokenizer.reached_end():
            if not tokenizer.peek().isdigit():
                break
            token_string += tokenizer.consume()

        return Tokens.Integer(int(token_string)) if token_string else False
