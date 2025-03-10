from cell import Cell
from window_class import Window
import time,random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        seed = None,
        window = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.window = window

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range (self.num_rows):
                self._cells[i][j].visited = False


    def _break_walls_r(self,i,j):
        actual_cell = self._cells[i][j]
        actual_cell.visited = True
        if j - 1 >= 0:
            top_cell = self._cells[i][j - 1]
        if i + 1 < self.num_cols:
            right_cell = self._cells[i + 1][j]
        if j + 1 < self.num_rows:
            bottom_cell = self._cells[i][j + 1]
        if i - 1 >= 0:
            left_cell = self._cells[i - 1][j]
        while True:
            to_visit = []
            if j - 1 >= 0 and not top_cell.visited:
                to_visit.append(("top",i,j-1))
            if i + 1 < self.num_cols and not right_cell.visited:
                to_visit.append(("right",i + 1, j)) 
            if j + 1 < self.num_rows and not bottom_cell.visited:
                to_visit.append(("bottom",i, j+1))
            if i - 1 >= 0 and not left_cell.visited:
                to_visit.append(("left",i - 1, j))
            if not to_visit:
                return
            else:
                direction, new_i, new_j = random.choice(to_visit)
                if direction == "top":
                    actual_cell.has_top_wall = False
                    self._cells[new_i][new_j].has_bottom_wall = False
                elif direction == "right":
                    actual_cell.has_right_wall = False
                    self._cells[new_i][new_j].has_left_wall = False
                elif direction == "bottom":
                    actual_cell.has_bottom_wall = False
                    self._cells[new_i][new_j].has_top_wall = False
                elif direction == "left":
                    actual_cell.has_left_wall = False
                    self._cells[new_i][new_j].has_right_wall = False
                self._break_walls_r(new_i,new_j)
                
        





    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0,0)
        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(len(self._cells)-1,len(self._cells[-1])-1)

    def _create_cells(self):
        if self.num_cols == 0:
            raise Exception("Need atleat 1 column")
        if self.num_rows == 0:
            raise Exception("Need atleast 1 row")
        
        self._cells = []
        for i in range (self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self.window)
                column.append(cell)
            self._cells.append(column)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self,i,j):
        x1_coord = self.x1 + (i * self.cell_size_x)
        y1_coord = self.y1 + (j * self.cell_size_y)
        x2_coord = x1_coord + self.cell_size_x
        y2_coord = y1_coord + self.cell_size_y
        self._cells[i][j].draw(x1_coord,y1_coord,x2_coord,y2_coord)
        self._animate()

    def _animate(self):
        if self.window is not None:
            self.window.redraw()
            time.sleep(0.05)


        