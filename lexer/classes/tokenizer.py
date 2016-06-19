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
    def check_eof_error(self, func):
        if self.pointer >= self.stream.len:
            raise EOFError
        return func

    # Tokenize Input
    @check_eof_error
    def consume(self) -> str:
        item = self.stream[self.pointer]
        self.pointer += 1
        return item

    @check_eof_error
    def peek(self) -> str:
        return self.stream[self.pointer]

    def reached_end(self) -> bool:
        return self.pointer >= self.stream.len

    def pointer_at(self) -> int:
        return self.pointer
