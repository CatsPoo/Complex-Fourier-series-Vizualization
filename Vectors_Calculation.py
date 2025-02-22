import math
import cmath

class Vector_Calculation:
    def __init__(self,vectors_count):
        self.vector_count = vectors_count
        self.fix_indexes = None
        self.C=None

    def set_C_Indexes(self,C_indexes):
        self.C = C_indexes

    def set_fix_indexes(self,indexes):
        self.fix_indexes = indexes
        
    def get_vectors_indexes(self):
         if(self.fix_indexes): return self.fix_indexes
         return [i - (self.vector_count//2)  for i in range(self.vector_count)]
    
    def _calculate_vector_position_at_t(self,n,t):
        return self.C[n] * cmath.exp(complex(0,n * 2 * math.pi * t))
    
    def calculateposition_n_at_t(self,n,t):
        vectors_positions = []
        for n in self.get_vectors_indexes()[:n]:
            vectors_positions.append(self._calculate_vector_position_at_t(n,t))
        s = sum(vectors_positions)
        angle = cmath.phase(s)
        norm = abs(s)
        return norm,angle
    
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




    



