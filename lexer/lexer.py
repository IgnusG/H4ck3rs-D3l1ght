from lexer.matcher import Matcher
from lexer.tokenizer import Tokenizer


class Lexer:
    @staticmethod
    def start(text: str):
        tokenizer = Tokenizer(''.join(text.split()))
        token_stream = Matcher.start(tokenizer)

        return token_stream
