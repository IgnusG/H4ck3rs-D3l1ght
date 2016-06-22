from lexer.definitions.tokens import *


class ComplexToken(Token):
    def __init__(self, primary_token, *more_tokens):
        super(ComplexToken, self).__init__(primary_token.pointer)
        self.token_list = [primary_token] + list(more_tokens)
        self.token_count = len(self.token_list)


class OutputNumDirect(ComplexToken):
    def __init__(self, integer: Integer, output_num_cell: OutputNumCell):
        super(OutputNumDirect, self).__init__(integer, output_num_cell)
        self.value = integer.value


class InputNumDirect(ComplexToken):
    def __init__(self, integer: Integer, input_num_cell: InputNumCell):
        super(InputNumDirect, self).__init__(integer, input_num_cell)
        self.value = integer.value


class OutputCharDirect(ComplexToken):
    def __init__(self, integer: Integer, output_char_cell: OutputCharCell):
        super(OutputCharDirect, self).__init__(integer, output_char_cell)
        self.value = integer.value
