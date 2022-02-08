import sys
from gen import generate
from bounds import get_points, analyze_points
from plotter import turtle_plot_ins, make_window2
import winsound

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 3:
        serpenski_length = int(args[-1])
        n = int(args[-2])
    else:
        try:
            n = int(args[-1])
        except ValueError:
            n = 8

    window, canvas, turtle = make_window2()
    turtle.reset()
    screen = turtle.Screen()
    win_dim = screen.window_width(), screen.window_height()
    print('win_dim:', win_dim)
    side_length = min(*win_dim)
    print('side_length:', side_length)
    instructions = generate(n)
    points = get_points(instructions, 1)
    res = analyze_points(points)
    print('res:', res)
    if serpenski_length is None:
        serpenski_length = side_length/res[0][0]
    print('serpenski_side_length:', serpenski_length)
    if serpenski_length/2 < 1:
        raise Exception('Cannot generate for N = %s, side_length = %s' % (n, serpenski_length))
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
    winsound.MessageBeep()
    window.mainloop()

