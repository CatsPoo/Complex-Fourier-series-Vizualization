import cmath
import math
class ComplexFunctionApproximation:

    def __init__(self,cords):
        self.cords_list = cords
        self.detta_t = 1/(len(self.cords_list))

    def F(self,t):
        t = t%1
        index = int(t // self.detta_t)
        real,imag = self.cords_list[index]
        return complex(real,imag)
    
    def Cn(self,n):
        sum = 0 
        t=0
        while t<=1:
            sum += self.F(t) *  cmath.exp(complex(0,-n * 2 *  math.pi * t)) * self.detta_t
            t+=self.detta_t
        return sum
    
    def calculate_vectors_coefficient(self,vectors_indexes):
        C={}
        for i in vectors_indexes:
            C[i] = self.Cn(i)
        return C
    