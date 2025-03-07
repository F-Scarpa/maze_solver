from window_class import Window,Point,Line
from cell import Cell


def main():
    window = Window(800, 600)
    cell = Cell(window.canvas,10,10,50,50,False,True,False,False)
    cell.draw()
   # point_a = Point(0,100)
   # point_b = Point(100,100)
    #line = Line(point_a,point_b)
   # window.draw_line(line,"black")
    window.wait_for_close()

if __name__ == "__main__":
    main()


main()