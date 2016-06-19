class Tokens:
    class Integer:
        def __init__(self, value):
            self.value = value

    class PointerLeft:
        pass

    class PointerRight:
        pass

    class IncrementCell:
        pass

    class DecrementCell:
        pass
