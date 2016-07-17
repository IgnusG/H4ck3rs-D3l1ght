from helpers.error_handling import IntegerPositionBadProgrammerSucks
from lexer.matcher import TokenStream
from lexer.warnings import Warnings
from parser.complex_tokens import *


class Parser:
    counter = 0

    @staticmethod
    def parse_conditions(token_stream: TokenStream):
        first_instance = token_stream[Parser.counter]
        body = TokenStream([])

        if not isinstance(first_instance, Condition):
            raise BaseException

        Parser.counter += 1
        current_instance = token_stream[Parser.counter]
        while not isinstance(current_instance, JumpBack):
            body.append(current_instance)
            Parser.counter += 1
            current_instance = token_stream[Parser.counter]

            if isinstance(current_instance, Condition):
                current_instance = Parser.parse_conditions(token_stream)

        return ConditionalStatement(first_instance, body)

    @staticmethod
    def parse_integer_group(token_stream: TokenStream):
        first_instance = token_stream[Parser.counter]
        if isinstance(first_instance, Integer):
            Parser.counter += 1
            second_instance = token_stream[Parser.counter]
            if isinstance(second_instance, OutputNumCell):
                return OutputNumDirect(first_instance, second_instance)
            elif isinstance(second_instance, InputNumCell):
                return InputNumDirect(first_instance, second_instance)
            elif isinstance(second_instance, OutputCharCell):
                return OutputCharDirect(first_instance, second_instance)
            else:
                Warnings.add_exception(IntegerPositionBadProgrammerSucks(first_instance.pointer))
        else:
            raise BaseException

    @staticmethod
    def start(token_stream: TokenStream):
        Parser.counter = 0
        out_stream = TokenStream([])

        while Parser.counter < len(token_stream):

            first_instance = token_stream[Parser.counter]
            if isinstance(first_instance, Integer):
                out_stream.append(Parser.parse_integer_group(token_stream))
            elif isinstance(first_instance, Condition):
                out_stream.append(Parser.parse_conditions(token_stream))
            else:
                out_stream.append(token_stream[Parser.counter])

            Parser.counter += 1

        return out_stream
