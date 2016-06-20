class Token:
    def __init__(self, pointer, value=''):
        self.value = value
        self.pointer = pointer

    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and self.pointer == other.pointer and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


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
