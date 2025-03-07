from window_class import Window,Point,Line


def main():
    window = Window(800,600)

    point_a = Point(0,0)
    point_b = Point(100,100)
    line = Line(point_a,point_b)
    window.draw_line(line,"black")
    window.wait_for_close()

if __name__ == "__main__":
    main()


main()