import numpy as np
#========================= 3.1 ============================#
#------------------------ 3.1 A --------------------------#
class Person():
    def __init__(self,first,last):
        self.first_name = first
        self.last_name  = last

    def __str__(self):
        print(f'{self.first_name} {self.last_name}')

m = Person('Peter','Karlsson')
print('Person:')
m.__str__()
#------------------------ 3.1 B --------------------------#
class Student(Person):
    def __init__(self, first, last, subj):
        super().__init__(first, last)
        self.subject = subj
    def __str__(self):
        print(f'{self.first_name} {self.last_name}, {self.subject}')

#------------------------ 3.1 C --------------------------#
n = Student('Pjotor', 'Dostojevski', 'Philosophy')
print('Student:')
n.__str__()
        
#------------------------ 3.1 D --------------------------#
class Teacher(Person):
    def __init__(self, first, last, teaches_course):
        super().__init__(first, last)
        self.course = teaches_course
    def __str__(self):
        print(f'{self.first_name} {self.last_name}, {self.course}')
    
b = Teacher('Mrs', 'Doubtfire', 'Home economy')
print('Teacher:')
b.__str__()

#========================= 3.2 ============================#

#------------------------ 3.2 A --------------------------#
A = np.empty([10,])
A.fill(None)
A[4] = 1
print(f'A = \n{A}\n')
#------------------------ 3.2 B --------------------------#
B = np.arange(10,50,1)
print(f'B = \n{B}\n')
#------------------------ 3.2 C --------------------------#
C = B[::-1]
print(f'C = \n{C}\n')
#------------------------ 3.2 D --------------------------#
D = np.arange(0,9,1)
D= D.reshape(3,3)
print(f'D = \n{D}\n')
#------------------------ 3.2 E --------------------------#
E = [1,2,0,0,4,0]
print(f'E:\n{np.nonzero(E)[0]}\n')
#------------------------ 3.2 F --------------------------#
F = np.random.random(size=30)
print(f'F: Mean value = {np.mean(F)}\n')
#------------------------ 3.2 G --------------------------#
G = np.zeros((4,4))
G[:,[0,3]] = 1
G[[0,3],:] = 1
print(f'G = \n{G}\n')
#------------------------ 3.2 H --------------------------#
l1 = '\u25a0 \u0020 \u25a0 \u0020 \u25a0 \u0020 \u25a0 \u0020;'
l2 = '\u0020 \u25a0 \u0020 \u25a0 \u0020 \u25a0 \u0020 \u25a0;'
matrix_fill = []
for i in range(8):
    if i%2 == 0:
        matrix_fill.append(l1)
    else:
        matrix_fill.append(l2)
H = np.matrix(matrix_fill)
print(f'H = \n{H}\n')           # The visualization is lacking, but technically it IS a matrix,  
#------------------------ 3.2 I --------------------------# # even is the terminal splits it into rows. =D
even_element = np.tile([0,1],4)
odd_element = np.tile([1,0],4)
mat_elements = []
for i in range(8):
    if i%2 == 0:
        mat_elements.append(even_element)
    else:
        mat_elements.append(odd_element)
i = np.matrix(mat_elements)
print(f'I = \n{i}\n')
#------------------------ 3.2 J --------------------------#
J = np.arange(11)
J[3:9] = [-i for i in J[3:9]]
print(f'J = \n{J}\n')
#------------------------ 3.2 K --------------------------#
K = np.random.random(10)
K.sort()
print(f'K = \n{K}\n')
#------------------------ 3.2 L --------------------------#
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print(f'A = {A}')
print(f'B = {B}')
print(f'L = {equal}\n')
#------------------------ 3.2 M --------------------------#
M = np.arange(10, dtype=np.int32)
print(f'Before: {M.dtype}')  
np.power(M,2,out=M)
print(f'After: {M.dtype}')   
#------------------------ 3.2 N --------------------------#
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
print(f'C = \n{C}')
D = np.diag(C)
print(f'Diagonal = {D}')



















