import tkinter as tk
from Vectors_Calculation import Vector_Calculation
import math
class Canvas:
    def __init__(self, root,points_color = 'black',points_size = 4):
        self.root = root
        self.points_color = points_color
        self.points_size = points_size
        self.wisth = 500
        self.height = 500

        self.time = 0
        self.timeout = 1
        self.delta_t = 0.001

        self.loop_id = None

        self.elements_to_delete_ids = []

        # Canvas setup
        self.canvas = tk.Canvas(self.root, bg="white", width=self.wisth, height=self.height)
        self.canvas.pack()

        self.points = []

        self.drawing_allowed = True  # Flag to allow drawing
        self.mouse_enabled = True

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)
        self.canvas.bind("<Button-1>", self.mouse_click)  # Stop drawing on mouse release

        # Button to print points
        self.button_print = tk.Button(self.root, text="Print Points", command=self.print_points)
        self.button_print.pack(side=tk.LEFT, padx=10, pady=10)

        # Button to reset canvas and allow another draw
        self.button_reset = tk.Button(self.root, text="Reset Canvas", command=self.reset_canvas)
        self.button_reset.pack(side=tk.RIGHT, padx=10, pady=10)

        self.button_draw_vectors = tk.Button(self.root, text="Draw Vectors", command=self.draw_vectors)
        self.button_draw_vectors.pack(side=tk.LEFT, padx=120, pady=10)

        self.draw_axes()

    def draw_axes(self):
        """Draw X and Y axes in the middle of the canvas."""
        self.canvas.create_line(self.wisth // 2, 0, self.wisth // 2, self.height, fill="gray", width=1)  # Y-axis
        self.canvas.create_line(0, self.height // 2, self.wisth, self.height // 2, fill="gray", width=1)  # X-axis

        # Labels
        self.canvas.create_text(self.wisth - 20, self.height // 2 - 10, text="X", fill="black")
        self.canvas.create_text(self.wisth // 2 + 10, 10, text="Y", fill="black")

    def draw_point(self,point):
        if(not self.mouse_enabled): return
        """Draw on the canvas and store point locations, only if allowed."""
        if self.drawing_allowed:
            x, y = point.x, point.y
            self.canvas.create_oval(x-self.points_size//2, y-self.points_size//2, x+self.points_size//2, y+self.points_size//2, fill=self.points_color, outline=self.points_color)  # Small dot
            self.points.append((x, y))  # Store point location

    def mouse_move(self,event):
        pass
    def mouse_click(self, event):
        pass

    def mouse_release(self, event):
        pass
    
    def print_points(self):
        """Print all stored points."""
        print(self.points)  # Output to console

    def reset_canvas(self):
        """Clear the canvas and reset the drawing permission."""
        if(self.loop_id):
            self.root.after_cancel(self.loop_id)
            self.loop_id = None
        self.canvas.delete("all")  # Clear canvas
        self.points = []  # Clear points list
        self.drawing_allowed = True  # Enable drawing again
        self.mouse_enabled = True
        self.draw_axes()
        print("Canvas reset. You can draw again.")

    def draw_vectors(self):
        pass
       
    def animate_vectors(self,vc,t):
        for element in self.elements_to_delete_ids:
            self.canvas.delete(element)

        v = vc.get_vectors_at_t_for_canvas(t)
        v=sorted(v, key=lambda x: x[0])[::-1]
        
        tip_x,tip_y=self.draw_vectors_chain((self.wisth//2,self.height//2),v)

        self.canvas.create_oval(tip_x - self.points_size//2,tip_y - self.points_size//2, tip_x+self.points_size//2, tip_y+self.points_size//2, fill="blue", outline="blue")
        t+= self.delta_t
        self.loop_id = self.root.after(self.timeout, lambda: self.animate_vectors(vc,t))


    def _canvas_to_math_coords(self, point):
        x,y = point
        """Convert canvas coordinates to mathematical coordinates (0,0) centered."""
        center_x, center_y = self.wisth // 2, self.height // 2
        return x - center_x, center_y - y  # Adjust to center origin
    
    def _math_coords_to_canvas(self, math_point):
        math_x,math_y = math_point
        center_x, center_y = self.wisth // 2, self.height // 2
        return int(center_x + math_x), int(center_y - math_y)  # Reverse the transformation
    
    def points_to_cords(self,points):
        math_points = [self._canvas_to_math_coords(point) for point in points]
        return self._normalize_points(math_points)
    
    def _normalize_points(self,points):
        half_width = self.wisth / 2
        half_height = self.height / 2
        return [(x / half_width, y / half_height) for x, y in points]
    
    def _denormalize_points(self,normalized_points):
        half_width = self.canvas_width / 2
        half_height = self.canvas_height / 2
        return [(x * half_width, y * half_height) for x, y in normalized_points]
    

    def cords_to_points(self,points):
        denormlized_points = self._denormalize_points(points)
        return [self._math_coords_to_canvas(point) for point in denormlized_points]
    
    
