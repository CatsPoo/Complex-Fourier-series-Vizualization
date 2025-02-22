import tkinter as tk
from PaintVisualizationCanvas import PaintVisualizationCanvas
from SolarSystemCanvas import SolarSystemCanvas
class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Choose Application Mode")
        self.root.geometry("400x200")

        # Title Label
        label = tk.Label(self.root, text="Select a Mode", font=("Arial", 14))
        label.pack(pady=20)

        # Buttons to select the mode
        btn_original = tk.Button(self.root, text="Draw and Animate Vectors", font=("Arial", 12),
                                 command=self.launch_original_mode)
        btn_original.pack(pady=10)

        btn_reverse = tk.Button(self.root, text="Reverse: Drag & Drop Mode", font=("Arial", 12),
                                command=self.launch_reverse_mode)
        btn_reverse.pack(pady=10)

    def launch_original_mode(self):
        """Launch the existing vector animation program."""
        self.root.destroy()  # Close the menu
        root = tk.Tk()
        app = PaintVisualizationCanvas(root)
        root.mainloop()

    def launch_reverse_mode(self):
        """Launch the new drag & drop mode."""
        self.root.destroy()  # Close the menu
        root = tk.Tk()
        app = SolarSystemCanvas(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    menu = MainMenu(root)
    root.mainloop()
