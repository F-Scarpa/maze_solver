from tkinter import Canvas
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

    


