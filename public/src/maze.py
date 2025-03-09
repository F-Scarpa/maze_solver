from cell import Cell
from window_class import Window
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._create_cells()

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


        