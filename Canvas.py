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

        self.loop_id = None

        self.elements_to_delete_ids = []

        # Canvas setup
        self.canvas = tk.Canvas(self.root, bg="white", width=self.wisth, height=self.height)
        self.canvas.pack()

        self.points = []

        self.drawing_allowed = True  # Flag to allow drawing
        self.mouse_enabled = True

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)  # Stop drawing on mouse release

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
        self.mouse_enabled = False
        vc = Vector_Calculation(self.vectors_count,self.points)
        delta_t = vc.detta_t

        self.animate_vectors(vc,delta_t,0)
       
    def animate_vectors(self,vc,delta_t,t):
        pass

