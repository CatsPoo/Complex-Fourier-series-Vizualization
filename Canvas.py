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
        self.vectors_count = 100
        self.timeout = 10

        self.loop_id = None
        self.root.title("Single Draw Paint Canvas")

        self.elements_to_delete_ids = []
        # Canvas setup
        self.canvas = tk.Canvas(self.root, bg="white", width=self.wisth, height=self.height)
        self.canvas.pack()

        # List to store drawn points
        self.points = []
        self.drawing_allowed = True  # Flag to allow drawing
        self.mouse_enabled = True
        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.disable_drawing)  # Stop drawing on mouse release

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



    def paint(self, event):
        if(not self.mouse_enabled): return
        """Draw on the canvas and store point locations, only if allowed."""
        if self.drawing_allowed:
            x, y = event.x, event.y
            self.canvas.create_oval(x, y, x+self.points_size, y+self.points_size, fill=self.points_color, outline=self.points_color)  # Small dot
            self.points.append((x, y))  # Store point location

    def disable_drawing(self, event):
        if(not self.mouse_enabled): return
        """Disable further drawing after the first stroke is completed."""
        self.drawing_allowed = False
        print("Drawing disabled. Points saved.")
        self.draw_line_of_ovals(self.points[0],self.points[-1])
    
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
        self.mouse_enabled = False
        vc = Vector_Calculation(self.vectors_count,self.points)
        delta_t = vc.detta_t

        self.animate_vectors(vc,delta_t,0)
       
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
    