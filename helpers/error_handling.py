class HackersException(Exception):
    def __init__(self, pointer):
        self.pointer = pointer


class HackersWarning(Warning):
    def __init__(self, pointer):
        self.pointer = pointer

# TODO: Move all exceptions and warnings here ...
