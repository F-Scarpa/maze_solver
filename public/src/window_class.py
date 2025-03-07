from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="grey")
        self.canvas.pack()
        self.window_is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running == True:
            self.redraw()

    def close(self):
        self.window_is_running = False

    def draw_line(self,line,fill_color = "black"):
        line.draw(self.canvas,fill_color)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,a,b):
        self.a = a
        self.b = b

# fill_color is red or black
    def draw(self,canvas,fill_color):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width = 2)

