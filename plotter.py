from pickle import TRUE
from textwrap import fill
import turtle as t
# import time
import tkinter as tk
from consts import *
import winsound


def make_window():
    #creating window
    window=tk.Tk()
    
    #getting screen width and height of display
    width= window.winfo_screenwidth() 
    height= window.winfo_screenheight()
    #setting tkinter window size
    # window.geometry("%dx%d" % (width, height))
    window.title("Canvas example")
    # START_WIDTH = width-10 
    # START_HEIGHT = height - 10

    START_WIDTH = width 
    START_HEIGHT = height

    frame = tk.Frame(window, width=START_WIDTH, height=START_HEIGHT)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    xscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
    xscrollbar.grid(row=1, column=0, sticky=tk.E+tk.W)

    yscrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)

    canvas = tk.Canvas(frame, width=START_WIDTH, height=START_HEIGHT,
                            scrollregion=(0, 0, START_WIDTH, START_HEIGHT),
                            xscrollcommand=xscrollbar.set,
                            yscrollcommand=yscrollbar.set, bg='beige')

    canvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

    xscrollbar.config(command=canvas.xview)
    yscrollbar.config(command=canvas.yview)
    frame.pack(fill=tk.BOTH, expand=True)
    turtle = t.RawTurtle(canvas)
    return window, canvas, turtle

def make_window2():
    canvas = t.getcanvas()
    root = canvas.winfo_toplevel()    
    root.title("Serpenski")
    root.state('zoomed')
    return root, canvas, t

    
def plot(instructions):
    w, c, t = make_window()
    t.speed(0)
    w.state('zoomed')
    t.hideturtle()
    for x in instructions:
        if x == M:
            t.right(ANGLE)
        elif x == P:
            t.left(ANGLE)
        else:
            t.forward(LENGTH)

    c.config(scrollregion=c.bbox(tk.ALL))
    winsound.MessageBeep()
    print('done')
    w.mainloop()
        

def plot_points(points):
    w, c, t = make_window()
    t.speed(0)
    w.state('zoomed')
    for pos in points:
        t.setposition(pos)
    c.config(scrollregion=c.bbox(tk.ALL))
    winsound.MessageBeep()
    print('done')
    w.mainloop()

def plot_str(ins):
    return ' '.join([ "-" if cmd == M else "+" if cmd == P else cmd for cmd in ins])

def turtle_plot_ins(turtle, instructions, length=LENGTH):
    t = turtle
    t.hideturtle()
    t.speed(0)
    for x in instructions:
        if x == M:
            t.right(ANGLE)
        elif x == P:
            t.left(ANGLE)
        else:
            t.forward(length)

if __name__ == '__main__':
    import sys
    from gen import generate

    args = sys.argv
    print(args)
    if len(args) >= 2:
        command, value = args[-2:]
    else:
        command = 'plot'
        value = '6'
    """
        X -> Y + X + Y
        Y -> X - Y - X
    """
    # n = 1
    # ins = [ X ]

    # n = 2
    # ins = [ "Y", 1, "X", 1, "Y"]

    # n = 3
    # ins = [ X, M, Y, M, X, 
    #         P, 
    #         Y, P, X, P, Y,
    #         P,
    #         X, M, Y, M, X ]

    # n = 4
    if command == 'plot_str':
        ins = generate(int(value))
        print(plot_str(ins))
    elif command == 'plot':
        try:
            n = int(value)
        except:
            n = 6
        plot(generate(n))
    else:
        ins = [
            Y, P, X, P, Y,
                M,
            X, M, Y, M, X,
                M,
            Y, P, X, P, Y,
            P,
            X, M, Y, M, X,
                P,
            Y, P, X, P, Y,
                P,
            X, M, Y, M, X,
            P,
            Y, P, X, P, Y,
                M,
            X, M, Y, M, X,
                M,
            Y, P, X, P, Y
        ]
        plot(ins)