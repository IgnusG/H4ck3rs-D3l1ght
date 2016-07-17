import sys

from io import StringIO

from lexer.lexer import Lexer
from parser.parser import Parser
from parser.complex_tokens import *


class CriticalExceptionOMG(Exception):
    pass


class Interpreter:
    version = '0.1'
    internal_pointer = 0
    internal_storage = [0]

    @staticmethod
    def run_input(stream):
        token_stream = Lexer.start(stream)
        parsed_stream = Parser.start(token_stream)
        out = StringIO()

        for token in parsed_stream:
            if isinstance(token, PointerLeft):
                if Interpreter.internal_pointer == 0:
                    Interpreter.internal_storage.insert(0, 0)
                else:
                    Interpreter.internal_pointer -= 1

            elif isinstance(token, PointerRight):
                Interpreter.internal_pointer += 1
                if Interpreter.internal_pointer >= len(Interpreter.internal_storage):
                    Interpreter.internal_storage += [0] * (Interpreter.internal_pointer - len(Interpreter.internal_storage) + 1)

            elif isinstance(token, IncrementCell):
                Interpreter.internal_storage[Interpreter.internal_pointer] += 1

            elif isinstance(token, DecrementCell):
                Interpreter.internal_storage[Interpreter.internal_pointer] -= 1

            elif isinstance(token, OutputNumCell):
                out.write(str(Interpreter.internal_storage[Interpreter.internal_pointer]))

            elif isinstance(token, InputNumCell):
                number = int(stream())
                Interpreter.internal_storage[Interpreter.internal_pointer] = number

            elif isinstance(token, OutputNumDirect):
                out.write(str(token.value))

            elif isinstance(token, InputNumDirect):
                Interpreter.internal_storage[Interpreter.internal_pointer] = token.value

            elif isinstance(token, OutputCharCell):
                out.write(chr(Interpreter.internal_storage[Interpreter.internal_pointer]))

            elif isinstance(token, InputCharCell):
                pass
            elif isinstance(token, OutputCharDirect):
                out.write(chr(token.value))

            else:
                raise CriticalExceptionOMG()

        return out.getvalue()

    @staticmethod
    def start(out=sys.stdout):

        out.write('Heya! This is the H4ck3rs D3l1ght Interpreter ' + Interpreter.version + '\n')
        out.flush()

        # Interpreter Loop
        while True:
            out.write('#> ')
            user_input = ''

            tmp_input = True
            while tmp_input:
                tmp_input = input()
                user_input += tmp_input

            if user_input == '#exit':
                break
            if user_input == '#clear':
                out.write('Registers cleared...')
                Interpreter.internal_storage = [0]
                Interpreter.internal_pointer = 0

            out.write(Interpreter.run_input(user_input))
            out.write('\n')
            out.flush()

        out.write('Bye\n')
        out.flush()
