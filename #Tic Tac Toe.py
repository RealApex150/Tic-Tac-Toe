#Tic Tac Toe
from tkinter import *
#Setting up graphics
root = Tk()
#Window
root.title("Tic Tac Toe")
root.geometry("500x500")
#Canvas
canvas = Canvas(root, width = 500, height = 500)
#Tic Tac Toe Boxes
canvas.create_line(167, 500, 167, 0)
canvas.create_line(334, 500, 334, 0)
canvas.create_line(500, 167, 0, 167)
canvas.create_line(500, 334, 0, 334)
#Mouse Position
def position(event):
   global x
   x = event.x
   global y
   y = event.y
root.bind('<Motion>', position)
#Fill Box with an X or an O
def fill_box_x(event):
    # If mouse on box 1
    if (x < 167 and y < 167):
        canvas.create_rectangle(167, 0, 0, 167, fill = "white")
        canvas.create_line(167, 0, 0, 167)
        canvas.create_line(0, 0, 167, 167)
    # iF mouse on box 2
    if (x < 334 and x > 167 and y < 167):
        canvas.create_rectangle(334, 0, 167, 167, fill = "white")
        canvas.create_line(334, 0, 167, 167)
        canvas.create_line(167, 0, 334, 167)
    # iF mouse on box 3
    if (x < 500 and x > 334 and y < 167):
        canvas.create_rectangle(500, 0, 334, 167, fill = "white")
        canvas.create_line(500, 0, 334, 167)
        canvas.create_line(334, 0, 500, 167)
    # iF mouse on box 4
    if (x < 167 and y > 167 and y < 334):
        canvas.create_rectangle(167, 167, 0, 334, fill = "white")
        canvas.create_line(167, 167, 0, 334)
        canvas.create_line(0, 167, 167, 334)
    # iF mouse on box 5
    if (x > 167 and x < 334 and y > 167 and y < 334):
        canvas.create_rectangle(334, 167, 167, 334, fill = "white")
        canvas.create_line(334, 167, 167, 334)
        canvas.create_line(167, 167, 334, 334)
    # iF mouse on box 6
    if (x > 334 and x < 500 and y > 167 and y < 334):
        canvas.create_rectangle(500, 167, 334, 334, fill = "white")
        canvas.create_line(500, 167, 334, 334)
        canvas.create_line(334, 167, 500, 334)
    # iF mouse on box 7
    if (x < 167 and y > 334 and y < 500):
        canvas.create_rectangle(167, 334, 0, 500, fill = "white")
        canvas.create_line(167, 334, 0, 500)
        canvas.create_line(0, 334, 167, 500)
    # iF mouse on box 8
    if (x > 167 and x < 334 and y > 334 and y < 500):
        canvas.create_rectangle(334, 334, 167, 500, fill = "white")
        canvas.create_line(334, 334, 167, 500)
        canvas.create_line(167, 334, 334, 500)
    # iF mouse on box 9
    if (x > 334 and x < 500 and y > 334 and y < 500):
        canvas.create_rectangle(500, 334, 334, 500, fill = "white")
        canvas.create_line(500, 334, 334, 500)
        canvas.create_line(334, 334, 500, 500)
def fill_box_o(event):
    # If mouse on box 1
    if (x < 167 and y < 167):
        canvas.create_rectangle(167, 0, 0, 167, fill = "white")
        canvas.create_oval(167, 0, 0, 167)
    # iF mouse on box 2
    if (x < 334 and x > 167 and y < 167):
        canvas.create_rectangle(334, 0, 167, 167, fill = "white")
        canvas.create_oval(334, 0, 167, 167)
    # iF mouse on box 3
    if (x < 500 and x > 334 and y < 167):
        canvas.create_rectangle(500, 0, 334, 167, fill = "white")
        canvas.create_oval(500, 0, 334, 167)
    # iF mouse on box 4
    if (x < 167 and y > 167 and y < 334):
        canvas.create_rectangle(167, 167, 0, 334, fill = "white")
        canvas.create_oval(167, 167, 0, 334)
    # iF mouse on box 5
    if (x > 167 and x < 334 and y > 167 and y < 334):
        canvas.create_rectangle(334, 167, 167, 334, fill = "white")
        canvas.create_oval(334, 167, 167, 334)
    # iF mouse on box 6
    if (x > 334 and x < 500 and y > 167 and y < 334):
        canvas.create_rectangle(500, 167, 334, 334, fill = "white")
        canvas.create_oval(500, 167, 334, 334)
    # iF mouse on box 7
    if (x < 167 and y > 334 and y < 500):
        canvas.create_rectangle(167, 334, 0, 500, fill = "white")
        canvas.create_oval(167, 334, 0, 500)
    # iF mouse on box 8
    if (x > 167 and x < 334 and y > 334 and y < 500):
        canvas.create_rectangle(334, 334, 167, 500, fill = "white")
        canvas.create_oval(334, 334, 167, 500)
    # iF mouse on box 9
    if (x > 334 and x < 500 and y > 334 and y < 500):
        canvas.create_rectangle(500, 334, 334, 500, fill = "white")
        canvas.create_oval(500, 334, 334, 500)
root.bind('<Button-1>', fill_box_x)
root.bind('<Button-3>', fill_box_o)
# Draw Winning Line

   
canvas.pack()
mainloop()



