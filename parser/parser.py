from helpers.error_handling import HackersException
from lexer.matcher import TokenStream
from lexer.definitions.tokens import *
from lexer.warnings import Warnings
from parser.complex_tokens import OutputNumDirect, InputNumDirect


class IntegerPositionBadProgrammerSucks(HackersException):
    def __init__(self):
        pass


class Parser:
    @staticmethod
    def start(token_stream: TokenStream):
        counter = 0
        while True:
            first_instance = token_stream[counter]
            if isinstance(first_instance, Integer):
                second_instance = token_stream[counter+1]
                if isinstance(second_instance, OutputNumCell):
                    new_token = OutputNumDirect(first_instance, second_instance)
                elif isinstance(second_instance, InputNumCell):
                    new_token = InputNumDirect(first_instance, second_instance)
                else:
                    Warnings.add_exception(HackersException(first_instance.pointer))
                    continue

                token_stream.replace_with(counter, new_token)
                counter += 1

                if counter >= len(token_stream):
                    break

        return token_stream
