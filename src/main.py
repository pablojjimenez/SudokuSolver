from sudoku import Sudoku
import json
import logging

logging.basicConfig(
    filename ='app.log',
    level = logging.NOTSET, 
    filemode = 'w', 
    format = '%(asctime)s : Line No. : %(lineno)d :: %(message)s'
)

s = Sudoku('003020600900305001001806400008102900700000008006708200002609500800203009005010300', logging)

print(s)