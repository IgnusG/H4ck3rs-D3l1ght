from lexer.definitions.tokens import *
from lexer.matcher import TokenStream


class ComplexToken(Token):
    def __init__(self, primary_token: Token, *more_tokens):
        super(ComplexToken, self).__init__(primary_token.pointer)
        self.token_list = TokenStream([primary_token] + list(more_tokens))
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


class ConditionalStatement(ComplexToken):
    def __init__(self, condition: Condition, body: [Token]):
        super(ConditionalStatement, self).__init__(condition, *body)

    def evaluate_condition(self, current_field_value: int):
        if current_field_value and len(self.token_list) > 1:
            return self.token_list[1:] + [self]
        else:
            return []
