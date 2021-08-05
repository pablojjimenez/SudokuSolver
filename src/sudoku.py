from posibles import *

class Sudoku:
    def __init__(self):
        self.cells = [Possibles() for i in range(1, 82)]

    def __str__(self) -> str:
        board = []
        j = 0
        f = 9
        for i in range(9):
            board.append(self.cells[j:f])
            j = f
            f += 9 if i!=8 else 10

        s = ''
        r=0
        first2 = True
        for i in board:
            s+='\n'
            c = 0
            first = True

            if (r%3 == 0) and (not first2):
                s += '-'.join('\n')
            else: 
                first2 = False  
            r += 1
            
            for j in i:
                if c%3 == 0 and (not first): 
                    s += ' |{:>{w}}'.format(str(j), w=10)    
                else: 
                    s += '{:>{w}}'.format(str(j), w=10)
                    first = False
                c += 1
        s += '\n'
        return s
