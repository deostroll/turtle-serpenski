from consts import *

def generate(n):
    ins = []
    for x in range(n):
        ins = next(ins)
    return ins

def next(ins):
    if len(ins) == 0:
        return [ X ]

    new_ins = []

    for x in ins:
        if x == X:
            new_ins.extend(RX)
        elif x == Y:
            new_ins.extend(RY)
        else:
            new_ins.append(x)
    return new_ins
