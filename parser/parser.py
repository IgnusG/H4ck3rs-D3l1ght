from helpers.error_handling import HackersException
from lexer.matcher import TokenStream
from lexer.warnings import Warnings
from parser.complex_tokens import *


class IntegerPositionBadProgrammerSucks(HackersException):
    pass


class Parser:
    @staticmethod
    def start(token_stream: TokenStream):
        counter = 0
        while counter < len(token_stream):
            first_instance = token_stream[counter]
            if isinstance(first_instance, Integer):
                second_instance = token_stream[counter+1]
                if isinstance(second_instance, OutputNumCell):
                    new_token = OutputNumDirect(first_instance, second_instance)
                elif isinstance(second_instance, InputNumCell):
                    new_token = InputNumDirect(first_instance, second_instance)
                elif isinstance(second_instance, OutputCharCell):
                    new_token = OutputCharDirect(first_instance, second_instance)
                else:
                    Warnings.add_exception(IntegerPositionBadProgrammerSucks(first_instance.pointer))
                    continue

                token_stream.replace_with(counter, new_token)

            counter += 1

        return token_stream
