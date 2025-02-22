from Canvas import Canvas
from Vectors_Calculation import Vector_Calculation
import math
class SolarSystemCanvas(Canvas):
    def __init__(self, root, points_color='black', points_size=4):
        super().__init__(root, points_color, points_size)

        self.points_size=30
        self.points_seize_delta = 20
        self.vectors_count = (self.points_size//self.points_seize_delta) + 1

        self.draw_center_star()



    def mouse_click (self, event):
        if(self.points_size<10): return
        self.draw_point(event)
        self.points_size-=self.points_seize_delta

    def draw_center_star(self,center_star_size=50):
        x,y = self.wisth//2, self.height//2

        id = self.canvas.create_oval(x-center_star_size//2, y-center_star_size//2, x+center_star_size//2, y+center_star_size//2, fill=self.points_color, outline=self.points_color)  # Small dot
        self.points.append((x, y))  # Store point location
        self.oval_elements_id.append(id)

    def draw_vectors(self):
        cords = self.points_to_cords(self.points)
        stars_speed = [1,10]
        C = {}
        for i in range(1,len(cords)):
            vector = cords[i][0] - cords[i-1][0] , cords[i][1]-cords[i-1][1]
            C[stars_speed[i-1]] = complex(vector[0],vector[1]) 
        
        vc = Vector_Calculation(self.vectors_count)
        vc.set_C_Indexes(C)
        vc.set_fix_indexes(stars_speed)
        self.animate_vectors(vc,0)



    def move_stars(self,start_point,vectors,mul):
        x1,y1 = start_point
        x2,y2 = 0,0
        for i,vector in enumerate(vectors):
            dx = vector[0] * math.cos(vector[1]) * mul
            dy = vector[0] * math.sin(vector[1]) * mul
            x2, y2 = x1 + dx, y1 - dy  # Calculate new endpoint
            radius = self.get_oval_radius(self.oval_elements_id[i+1])
            self.canvas.coords(self.oval_elements_id[i+1], x2 - radius, y2 - radius, x2 + radius, y2 + radius)
            x1, y1 = x2, y2


    def animate_vectors(self,vc:Vector_Calculation,t):
            for element in self.elements_to_delete_ids:
                self.canvas.delete(element)

            v = vc.get_vectors_at_t_for_canvas(t)
            
            self.draw_vectors_chain((self.wisth//2,self.height//2),v)
            self.move_stars((self.wisth//2,self.height//2),v,245)
            

            #self.canvas.create_oval(tip_x - self.points_size//2,tip_y - self.points_size//2, tip_x+self.points_size//2, tip_y+self.points_size//2, fill="blue", outline="blue")
            t += self.delta_t
            self.loop_id = self.root.after(self.timeout, lambda: self.animate_vectors(vc,t))

    def get_oval_radius(self, oval_id):
        x1, y1, x2, y2 = self.canvas.coords(oval_id)
        radius = (x2 - x1) / 2  # Since it's a circle, width = height
        return radius

