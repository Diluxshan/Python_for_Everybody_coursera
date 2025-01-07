import numpy as np

x = np.arange(7,16)
y = np.arange(1,18,2)
z = np.column_stack(tup=(x[:: -1], y))

for i, j in z:
    print(' '*i + "*"*j)

x = np.arange(7,14)
y = np.arange(5,18,2)
z = np.column_stack(tup=(x[:: -1], y))

for i,j in z:
    print(' '*i + "*"*j)

# new line for 20025 commit.
# second commit of the year.
