from Canvas import Canvas
from Vectors_Calculation import Vector_Calculation

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

        self.canvas.create_oval(x-center_star_size//2, y-center_star_size//2, x+center_star_size//2, y+center_star_size//2, fill=self.points_color, outline=self.points_color)  # Small dot
        self.points.append((x, y))  # Store point location

    def draw_vectors(self):
        cords = self.points_to_cords(self.points)
        stars_speed = [1,-1]
        C = {}
        for i in range(1,len(cords)):
            vector = (cords[i][0] - cords[i-1][1],cords[i][0] - cords[i-1][1])
            C[stars_speed[i-1]] = complex(vector[0],vector[1]) 
        
        vc = Vector_Calculation(self.vectors_count)
        vc.set_C_Indexes(C)
        self.animate_vectors(vc,0)


    def animate_vectors(self, vc, t):
        return super().animate_vectors(vc,t)
