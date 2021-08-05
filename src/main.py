from sudoku import Sudoku
import json

s = Sudoku('003020600900305001001806400008102900700000008006708200002609500800203009005010300')

print(json.dumps(s.neighbours))
#print(s.neighbours)