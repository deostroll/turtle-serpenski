import sys
from gen import generate
from bounds import get_points, analyze_points
from plotter import turtle_plot_ins, make_window2
from time import sleep

if __name__ == '__main__':
    args = sys.argv
    # try:
    #     n = int(args[-1])
    # e
    try:
        n = int(args[-1])
    except ValueError:
        n = 8

    window, canvas, turtle = make_window2()
    turtle.reset()
    screen = turtle.Screen()
    win_dim = screen.window_width(), screen.window_height()
    side_length = min(*win_dim)
    instructions = generate(n)
    points = get_points(instructions, 1)
    res = analyze_points(points)
    serpenski_length = round(side_length/res[0][0])
    if serpenski_length < 2:
        raise Exception('Cannot generate for N = %s' % n)
    turtle.pu()
    turtle.setpos(-win_dim[0]/6, 0)
    turtle.pd()
    turtle.write('N = %s' % n)
    turtle.pu()
    if res[1][1] > 0:
        # upward serpenski
        turtle.setpos(-side_length/2, -side_length/2 + 17)
    else:
        # downard serpenski
        turtle.setpos(-side_length/2, side_length/2 - 5)
    
    turtle.pd()
    turtle_plot_ins(turtle, instructions, serpenski_length)

    window.mainloop()

