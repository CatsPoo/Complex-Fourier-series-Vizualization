from Canvas import Canvas
import tkinter as tk
from Vectors_Calculation import Vector_Calculation
import math

class PaintVisualizationCanvas(Canvas):
    def __init__(self, root, points_color='black', points_size=4):
        super().__init__(root, points_color, points_size)

        self.vectors_count = 100
        self.root.title("Single Draw Paint Canvas")

    def mouse_click(self, event):
        if(not self.mouse_enabled): return
        """Draw on the canvas and store point locations, only if allowed."""
        if self.drawing_allowed:
            x, y = event.x, event.y
            self.canvas.create_oval(x, y, x+self.points_size, y+self.points_size, fill=self.points_color, outline=self.points_color)  # Small dot
            self.points.append((x, y))  # Store point location

    def mouse_release(self, event):
        if(not self.mouse_enabled): return
        """Disable further drawing after the first stroke is completed."""
        self.drawing_allowed = False
        print("Drawing disabled. Points saved.")
        self.draw_line_of_ovals(self.points[0],self.points[-1])

    def draw_line_of_ovals(self,point1,point2,spacing = 5):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        steps = max(abs(dx), abs(dy)) 
        if steps == 0:
            return
        x_step = dx / steps
        y_step = dy / steps

        for i in range(0, steps, spacing):  # Draw dots at spaced intervals
            x = int(point1[0] + i * x_step)
            y = int(point1[1] + i * y_step)
            self.points.append((x,y))
            self.canvas.create_oval(x, y, x+self.points_size, y+self.points_size, fill=self.points_color, outline=self.points_color)  # Red dots for visibility
    
    
    def animate_vectors(self,vc,delta_t,t):
        for element in self.elements_to_delete_ids:
            self.canvas.delete(element)

        v = vc.get_vectors_at_t_for_canvas(t)
        v=sorted(v, key=lambda x: x[0])[::-1]
        x1,y1 = self.wisth//2, self.height//2
        x2,y2 = 0,0
        for vector in v:
            dx = vector[0] * math.cos(vector[1]) * 240
            dy = vector[0] * math.sin(vector[1]) * 240
            x2, y2 = x1 + dx, y1 - dy  # Calculate new endpoint
            line_id =  self.canvas.create_line(x1, y1, x2,y2, arrow=tk.LAST, width=1, fill="red")
            self.elements_to_delete_ids.append(line_id)
            x1, y1 = x2, y2
        self.canvas.create_oval(x2,y2, x2+self.points_size, y2+self.points_size, fill="blue", outline="blue")
        t+= delta_t
        self.loop_id = self.root.after(self.timeout, lambda: self.animate_vectors(vc,delta_t,t))
