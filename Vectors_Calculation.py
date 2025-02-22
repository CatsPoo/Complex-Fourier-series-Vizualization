import math
import cmath

class Vector_Calculation:
    def __init__(self,vectors_count):
        self.vector_count = vectors_count

        self.C=None

    def set_C_Indexes(self,C_indexes):
        self.C = C_indexes

    
    def get_vectors_indexes(self):
         return [i - (self.vector_count//2)  for i in range(self.vector_count)]
    
    def _calculate_vector_position_at_t(self,n,t):
        return self.C[n] * cmath.exp(complex(0,n * 2 * math.pi * t))
    
    def calculate_all_vectors_at_t(self,t):
        vectors_positions = []
        for n in self.get_vectors_indexes():
            vectors_positions.append(self._calculate_vector_position_at_t(n,t))
        return vectors_positions
    
    
    def get_vectors_at_t_for_canvas(self,t):
        complex_numbers = self.calculate_all_vectors_at_t(t)
        vectors = []
        for complax_number in complex_numbers:
            angle = cmath.phase(complax_number)
            norm = abs(complax_number)
            vectors.append((norm,angle))
        return vectors




    



