from lexer.matcher import Matcher
from lexer.tokenizer import Tokenizer


class Lexer:
    @staticmethod
    def start(text: str):
        tokenizer = Tokenizer(''.join(text.split()))
        tokenized_stream = Matcher.start(tokenizer)

        return tokenized_stream
