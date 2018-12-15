import numpy as np 
A=np.array([[3,2,-1],[0,1,3],[1,2,-1]])
B=np.linalg.inv(A)
C=np.linalg.det(A)
D=B*C
print(B)
print(C)
print(D)