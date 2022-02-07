from asyncio import wait_for
from consts import X, Y, P, M, ANGLE, LENGTH
import math
from plotter import plot_points

def deg2rads(n):
    return n * math.pi/180

def sin(n):
    return math.sin(deg2rads(n))

def cos(n):
    return math.cos(deg2rads(n))

def get_points(ins, length=LENGTH):
    heading = 0
    points = [(0,0)]
    for cmd in ins:
        if cmd == P:
            heading += ANGLE
        elif cmd == M:
            heading -= ANGLE
        else:
            previous_pt = points[-1]
            px, py = previous_pt
            points.append((
                px + (length * cos(heading)), 
                py + (length * sin(heading))
                )
            )
    return points

def analyze_points(points):
    mx = max(points, key= lambda x: x[0])
    my = max(points, key= lambda x: math.fabs(x[1]))
    return mx, my

if __name__ == '__main__':
    from gen import generate
    from plotter import make_window, make_window2, turtle_plot_ins
    import sys
    import time
    from timer import SlidingTimer
    from threading import Event

    def debounce(widget, eventName, func, slidingTimeout):
        # e = Event()    
        def timeoutHandler():
            widget.unbind(eventName, handler)
            func()
            # e.set()
        
        timer = SlidingTimer(slidingTimeout, timeoutHandler, is_daemon=False)
        timer.start()
        def handler(evt):
            time.reset()
            print('Configure...')

        widget.bind(eventName, handler)
        # while not e.is_set():
        #     widget.update_idletasks()
            
    args = sys.argv[1:]
    if len(args) == 0:
        n = 6
    else:
        n = int(args[0])
    
    ins = generate(n)
    points = get_points(ins, 1)
    # # plot_points(points)
    res = analyze_points(points)
    print(res)
    window, canvas, turtle = make_window2()
    turtle.reset()
    screen = turtle.Screen()
    win_dim = screen.window_width(), screen.window_height()
    print('win_dim:', win_dim)
    # turtle_plot_ins(turtle, ins)
    side_length = min(*win_dim)
    print('side_length:', side_length)
    is_win_height_small = True if side_length == win_dim[1] else False

    if is_win_height_small:
        turtle.up()
        padding = 200
        turtle.setposition(-side_length/2, side_length/2)

        turtle.down()
        # turtle.forward(side_length - padding/2)
        # turtle.right(90)
        # turtle.forward(side_length - padding/2)
        # turtle.right(90)
        # turtle.forward(side_length - padding/2)
        # turtle.right(90)
        # turtle.forward(side_length - padding/2)
        
        # turtle.setpos((-win_dim[0]/2 + padding, win_dim[1]/2 - padding))
        # print(turtle.position())
        # turtle.down()
        # turtle.setpos( (win_dim[0] - padding, -win_dim[1] + padding) )  
        # print(turtle.position())

        
    # window.mainloop()

    # debounce(window, '<Configure>', lambda: print('done'), 5)
    # window.mainloop()

    
