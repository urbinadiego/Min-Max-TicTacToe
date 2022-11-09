#Exception for invalid row or col selection | Higher than 3
#or lower than 0

class SelectionOutOFBoundsError(Exception):
    def __init__(self, value) -> None:
        self.value = value