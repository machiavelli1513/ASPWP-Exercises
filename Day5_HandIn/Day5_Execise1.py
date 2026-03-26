import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


# Exercise 1 Linear Algebra

#---------------- 1 A ------------------#
print('Exercise 1A:\n'+12*'-')
A = np.matrix('1 -2 3; 4 5 6; 7 1 9')
print(f'A = \n{A}\n')
#---------------- 1 B ------------------#
print('Exercise 1B:\n'+12*'-')
B = np.array([1,2,3])
print(f'B = \n{B}\n')
#---------------- 1 C ------------------#
print('Exercise 1C:\n'+12*'-')
C = scipy.linalg.solve(A,B)
print(f'C = \n{C}\n')
print(f'Correct? {np.allclose(np.dot(A, C), B)}\n')
#---------------- 1 D ------------------#
print('Exercise 1D:\n'+12*'-')
D = A@C
print(f'D = \n{D}: Yes!\n')
#---------------- 1 E ------------------#
print('Exercise 1E:\n'+12*'-')
E = np.random.rand(3,3)
E_x = scipy.linalg.solve(A,E)                          # Solve
print(f'E = \n{E}\n')
print(f'Correct? {np.allclose(np.dot(A, E_x), E)}\n')
E_y = A@E_x                                         # Substitue back
print(f'E_y = \n{E_y}: Yes!\n')
#---------------- 1 F ------------------#
print('Exercise 1F:\n'+12*'-')
A_eig, A_eig_vec = scipy.linalg.eig(A)
print(f'Eigenvalues A:\n{A_eig}')
print(f'Eigenvector A:\n{A_eig_vec}')
print(A)
print(f'Check: A = SXS^-1 = \n{A_eig_vec*np.diag(A_eig)*scipy.linalg.inv(A_eig_vec)}\n')
#---------------- 1 G ------------------#
print('Exercise 1G:\n'+12*'-')
G_inv = scipy.linalg.inv(A)
G_det = scipy.linalg.det(A)
print(f'Inverse of A:\n{G_inv}\nDeterminant of A:\n{round(G_det,3)}\n')
#---------------- 1 H ------------------#
print('Exercise 1H:\n'+12*'-')
H_norm_Frob = scipy.linalg.norm(A,ord='fro')
H_norm_inf = scipy.linalg.norm(A,ord=np.inf)
print(f'Frobenius norm:\n{H_norm_Frob}')
print(f'Infinity norm:\n{H_norm_inf}')

# Exercise 2 Statistics

#---------------- 2 A ------------------#
print('Exercise 2A:\n'+12*'-')
x = np.arange(poisson.ppf(0.01,0.6),poisson.ppf(0.99,0.6))
fig, ax = plt.subplots(1,1,figsize=(9.6,7.2))
fig.suptitle('Poisson PMF,CDF and Histogram')
ax.plot(x,poisson.pmf(x,0.6),label='PMF',color='b',marker='o',markersize=7,linestyle='None')
ax.vlines(x, 0, poisson.pmf(x, 0.6), colors='b', lw=5)

ax.plot(x,poisson.cdf(x,0.6),'r',label='CDF')
ax.hist(poisson.rvs(0.6,size=1000),bins=10,histtype='step',alpha=0.5,density=True,label='1000 random\nPoisson dist. numbers')
ax.set_xlabel('x-values (Arb)')
ax.set_ylabel('Probability')
plt.legend(loc='best')
plt.savefig(fname="/home/Karlsson/Doktorandkurser/AdvancedPythonProgramming/Day5/Day5_Exercise_2.png",dpi=300,format='png')
plt.show()

#---------------- 2 B ------------------#
print('Exercise 2B:\n'+12*'-')

#---------------- 2 C ------------------#
print('Exercise 2C:\n'+12*'-')