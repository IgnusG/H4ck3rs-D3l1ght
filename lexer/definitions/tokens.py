class Token:
    def __init__(self, pointer, value=''):
        self.value = value
        self.pointer = pointer


class Integer(Token):
    pass


class PointerLeft(Token):
    pass


class PointerRight(Token):
    pass


class IncrementCell(Token):
    pass


class DecrementCell(Token):
    pass


class OutputNumCell(Token):
    pass


class InputNumCell(Token):
    pass


class OutputCharCell(Token):
    pass


class InputCharCell(Token):
    pass
