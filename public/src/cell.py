class Cell:
    def __init__(self,window, x1, y1, x2, y2, left_wall = True, top_wall = True, right_wall = True, bottom_wall = True):
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.left_wall = left_wall
        self.top_wall = top_wall
        self.right_wall = right_wall
        self.bottom_wall = bottom_wall

    def draw(self):
        if self.left_wall:
            self.window.create_line(self.x1,self.y1,self.x1,self.y2)
        if self.top_wall:
            self.window.create_line(self.x1,self.y1,self.x2,self.y1)
        if self.right_wall:
            self.window.create_line(self.x2,self.y1,self.x2,self.y2)
        if self.bottom_wall:
            self.window.create_line(self.x1,self.y2,self.x2,self.y2)
