import numpy as np
import math
import cmath

class Vector_Calculation:
    def __init__(self,vectors_count,points_list):
        self.canvas_width = 500
        self.canvas_height = 500

        self.vector_count = vectors_count
        self.cords_list = self.points_to_cords(points_list)

        self.detta_t = 1/(len(self.cords_list))
        self.C=None
        self._calculate_vectors_coefficient()

    def _canvas_to_math_coords(self, point):
        x,y = point
        """Convert canvas coordinates to mathematical coordinates (0,0) centered."""
        center_x, center_y = self.canvas_width // 2, self.canvas_height // 2
        return x - center_x, center_y - y  # Adjust to center origin
    
    def _math_coords_to_canvas(self, math_point):
        math_x,math_y = math_point
        center_x, center_y = self.canvas_width // 2, self.canvas_height // 2
        return int(center_x + math_x), int(center_y - math_y)  # Reverse the transformation
    
    def _normalize_points(self,points):
        half_width = self.canvas_width / 2
        half_height = self.canvas_height / 2
        return [(x / half_width, y / half_height) for x, y in points]
    
    def _denormalize_points(self,normalized_points):
        half_width = self.canvas_width / 2
        half_height = self.canvas_height / 2
        return [(x * half_width, y * half_height) for x, y in normalized_points]
    
    def points_to_cords(self,points):
        math_points = [self._canvas_to_math_coords(point) for point in points]
        return self._normalize_points(math_points)
    
    def cords_to_points(self,points):
        denormlized_points = self._denormalize_points(points)
        return [self._math_coords_to_canvas(point) for point in denormlized_points]
    
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
    
    def get_vectors_indexes(self):
         return [i - (self.vector_count//2)  for i in range(self.vector_count)]
    
    def _calculate_vectors_coefficient(self):
        self.C = {}
        vectors_indexes = self.get_vectors_indexes()
        for i in vectors_indexes:
            self.C[i] = self.Cn(i)

    
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




    



