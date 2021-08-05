# SudokuSolver
Training with some algorithm...

## Delete call
```
graph TD
    A[delete cell, value] -->|delete from cell, value| B( - only one) --> Z[ERROR]
    A --> C( - more than one)
    C -->|One left| D(delete left value from neighbours)
    C --> E(only 1cell with v in the group)
    E --> H[assign 1cell, v]
```