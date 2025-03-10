import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells),num_cols)
        self.assertEqual(len(m1._cells[0]),num_rows)
    
    def test_maze_with_different_dimensions(self):
        num_cols = 10
        num_rows = 10
        m2 = Maze(5,5, num_rows,num_cols,7,15)
        self.assertEqual(len(m2._cells),num_cols)
        self.assertEqual(len(m2._cells[0]),num_rows)

    def test_with_no_columns(self):
        num_cols = 0
        num_rows = 10
        
        with self.assertRaises(Exception) as context:
            m3 = Maze(0,0, num_rows,num_cols,8,8)
            self.assertEqual(str(context.exception),"Need atleat 1 column")

    def test_with_no_rows(self):
        num_cols = 10
        num_rows = 0
        
        with self.assertRaises(Exception) as context:
            m3 = Maze(0,0, num_rows,num_cols,8,8)
            self.assertEqual(str(context.exception),"Need atleat 1 row")

    def test_check_entrance_cell(self):
        m4 = Maze(0,0,10,10,5,5)
        m4._break_entrance_and_exit()
        self.assertEqual(m4._cells[0][0].has_top_wall,False)

    def test_check_exit_cell(self):
        m5 = Maze(0,0,10,10,5,5)
        m5._break_entrance_and_exit()
        self.assertEqual(m5._cells[-1][-1].has_bottom_wall,False)

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m6 = Maze(0,0,num_rows,num_cols,10,10)
        for column in m6._cells:
            for cell in column:
                self.assertEqual(cell.visited,False)


if __name__ == "__main__":
    unittest.main()