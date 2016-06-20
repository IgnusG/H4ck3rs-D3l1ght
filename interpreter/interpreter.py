from lexer.lexer import Lexer
from parser.parser import Parser
from lexer.definitions.tokens import *
from parser.complex_tokens import *


class CriticalExceptionOMG(Exception):
    pass


class Interpreter:
    @staticmethod
    def start():
        internal_storage = [0]
        internal_pointer = 0

        # Interpreter Loop
        while True:
            user_input = input()

            token_stream = Lexer.start(user_input)
            parsed_stream = Parser.start(token_stream)

            for token in parsed_stream:
                if isinstance(token, PointerLeft):
                    if internal_pointer == 0:
                        internal_storage.insert(0, 0)
                    else:
                        internal_pointer -= 1

                elif isinstance(token, PointerRight):
                    internal_pointer += 1

                elif isinstance(token, IncrementCell):
                    if internal_pointer > len(internal_storage):
                        internal_storage += [0] * (internal_pointer - len(internal_storage) + 1)

                    internal_storage[internal_pointer] += 1

                elif isinstance(token, DecrementCell):
                    if internal_pointer > len(internal_storage):
                        internal_storage += [0] * (internal_pointer - len(internal_storage) + 1)

                    internal_storage[internal_pointer] -= 1

                elif isinstance(token, OutputNumCell):
                    print(internal_storage[internal_pointer])

                elif isinstance(token, InputNumCell):
                    number = int(input())
                    internal_storage[internal_pointer] = number

                elif isinstance(token, OutputNumDirect):
                    print(token.value)

                elif isinstance(token, InputNumDirect):
                    internal_storage[internal_pointer] = token.value

                elif isinstance(token, OutputCharCell):
                    print(chr(internal_storage[internal_pointer]))

                elif isinstance(token, InputCharCell):
                    pass

                else:
                    raise CriticalExceptionOMG()
