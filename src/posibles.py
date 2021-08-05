
class Possibles:

    def __init__(self):
        self.ns = [i for i in range(1,10)]

    def only_one(self) -> bool:
        return len(self.ns) == 1

    def candidate(self):
        return self.ns[0]

    def delete(self, value: int):
        self.ns.remove(value)
    
    def num_possibles(self) -> int:
        return len(self.ns)

    def has(self, value: int) -> bool:
        return value in self.ns

    def __str__(self) -> str:
        s = ''
        for i in self.ns:
            s += str(i)
        return s

    def __repr__(self) -> str:
        return self.__str__()
