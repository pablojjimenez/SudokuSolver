from posibles import *

class Sudoku:

    def __init__(self, sudoku: str):
        self.groups     = [[] for i in range(27)]
        self.groups_of  = {} #<int, (3)>
        self.neighbours = [[] for i in range(82)]
        self.cells = [Possibles() for i in range(1, 82)]
        
        self.initialize_utils()
        '''
        c = 0
        for i in sudoku:
            if i != '0' and i != '.':
                self.assign(c,int(i)) 
            c += 1
        '''
        
    def initialize_utils(self):
        """
            The board is a matrix 9 x 9
            g the position of the index depending on the 
            group I'm in. Remember 3 roups: rows, columns 
            and squares
        """
        for i in range(9):
            for j in range(9):
                k = i * 9 + j # tranformed into array index
                g = (i, 9 + j, 18 + int(i / 3)*3 + int(j/3))
                
                for w in g:
                    self.groups[w].append(k)
                    self.groups_of[k] = g
        # neighbours
        print(len(self.groups_of[k]) - 1)
        for k in range(len(self.neighbours)):
            for i in range(len(self.groups_of[k]) - 1):
                for j in range(9):
                    k2 = self.groups[self.groups_of[k][i]][j]
                    if k2 != k:
                        self.neighbours[k].append(k2)
        
    def is_solved(self) -> bool:
        for i in self.cells:
            if not i.only_one(): return False
        return True

    def assign(self, cell: int, value: int) -> bool:
        vector = self.cells[cell].ns.copy()
        for i in vector:
            if value != i:
                self.delete(cell, i)

    def delete(self, cell: int, value: int):
        self.cells[cell].delete(value)

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
                s += '-'*95
                s += '\n'
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
