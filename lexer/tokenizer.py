class Tokenizer:
    def __init__(self, stream):
        self.stream = stream
        self.pointer = 0
        self.snapshots = []

    # Rollback control
    def take_snapshot(self):
        self.snapshots.append(self.pointer)

    def rollback_snapshot(self):
        self.pointer = self.snapshots.pop()

    def purge_snapshot(self):
        del self.snapshots[-1]

    # Handle unexpected EOF
    def check_eof_error(self):
        if self.pointer >= len(self.stream):
            raise EOFError

    # Tokenize Input
    def consume(self) -> str:
        self.check_eof_error()
        item = self.stream[self.pointer]
        self.pointer += 1
        return item

    def peek(self) -> str:
        self.check_eof_error()
        return self.stream[self.pointer]

    def reached_end(self) -> bool:
        return self.pointer >= len(self.stream)

    def pointer_at(self) -> int:
        return self.pointer
