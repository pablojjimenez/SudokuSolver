
class Possibles:

    def __init__(self):
        self.ns = [i for i in range(1,10)]

    def __str__(self) -> str:
        s = ''
        for i in self.ns:
            s += str(i)
        return s

    def __repr__(self) -> str:
        return self.__str__()
