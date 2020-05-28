import numpy as np
while True:
        N = int(input('Enter the number of rows of the matrix (value> 0): '))
        M = int(input('Enter the number of columns in the matrix (value> 0): '))
        if N < 0 | N < 0: continue
        else: break;
Z = np.random.random((N,M))
Z = Z * (100)
print(Z)
print('-----------------------')
for n in range(M):
    sum_col = 0
    for m in range(N):
        sum_col += Z[m][n]
    print(sum_col)
input('Press any key to exit')