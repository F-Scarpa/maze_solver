import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()


# Disegna una linea da (50,50) a (350,250)
canvas.create_line(50, 50, 350, 250, fill="black", width=3)


root.mainloop()


