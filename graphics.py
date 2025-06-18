import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Canvas Eraser")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click = None

        self.canvas.bind('<Motion>', self.mouse_move)
        self.canvas.bind('<Button-1>', self.mouse_click)
        self.root.update()

    def mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def mouse_click(self, event):
        self.last_click = (event.x, event.y)

    def get_mouse_x(self):
        self.root.update()
        return self.mouse_x

    def get_mouse_y(self):
        self.root.update()
        return self.mouse_y

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def set_color(self, object_id, color):
        self.canvas.itemconfig(object_id, fill=color)

    def moveto(self, object_id, x, y):
        bbox = self.canvas.bbox(object_id)
        if bbox:
            current_x = bbox[0]
            current_y = bbox[1]
            dx = x - current_x
            dy = y - current_y
            self.canvas.move(object_id, dx, dy)

    def wait_for_click(self):
        while self.last_click is None:
            self.root.update()
        return

    def get_last_click(self):
        return self.last_click
