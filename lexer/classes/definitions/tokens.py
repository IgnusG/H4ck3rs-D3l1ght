class Token:
    def __init__(self, value=''):
        self.value = value


class Integer(Token):
    def __init__(self, value):
        super().__init__(value)
        self.type = Integer


class PointerLeft:
    def __init__(self):
        self.type = PointerLeft


class PointerRight:
    def __init__(self):
        self.type = PointerRight


class IncrementCell:
    def __init__(self):
        self.type = IncrementCell


class DecrementCell:
    def __init__(self):
        self.type = DecrementCell


class OutputNumCell:
    def __init__(self):
        self.type = OutputNumCell


class InputNumCell:
    def __init__(self):
        self.type = InputNumCell


class OutputCharCell:
    def __init__(self):
        self.type = OutputCharCell


class InputCharCell:
    def __init__(self):
        self.type = InputCharCell
