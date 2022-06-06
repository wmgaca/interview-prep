from typing import List

class IntStream:
    def __init__(self, values: List[int]) -> "IntStream":
        self.values = values

    def has_next(self) -> bool:
        # Assume this is already implemented
        pass

    def next(self) -> int:
        # Assume this is already implemented
        pass


class UnionSet(IntStream):
    def __init__(self, a: IntStream, b: IntStream) -> "UnionSet":
        raise NotImplementedError("Implement me.")

    def has_next(self) -> bool:
        raise NotImplementedError("Implement me.")

    def next(self) -> int:
        raise NotImplementedError("Implement me.")


a = IntStream([1, 1, 1, 1])
b = IntStream([1, 3, 4, 4])
c = UnionSet(a, b)

while c.has_next():
    print(c.next()) 
    
# expected to print out:
# 1
# 3
# 4