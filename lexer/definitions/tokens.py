class Token:
    def __init__(self, value=''):
        self.value = value


class Integer(Token):
    def __init__(self, value):
        super().__init__(value)


class PointerLeft:
    pass


class PointerRight:
    pass


class IncrementCell:
    pass


class DecrementCell:
    pass


class OutputNumCell:
    pass


class InputNumCell:
    pass


class OutputCharCell:
    pass


class InputCharCell:
    pass
