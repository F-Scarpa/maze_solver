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


if __name__ == "__main__":
    unittest.main()