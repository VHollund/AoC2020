from Helpers.GetInput import get_input
import re
import numpy as np


import math

def rotate(origin, point, a):
    ox, oy = origin
    px, py = point
    angle = np.deg2rad(a)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def degree_to_direction(degree):
    while degree >= 360:
        degree -= 360
    while degree < 0:
        degree += 360
    if degree == 0 or degree == 360 or degree % 360 == 0:
        return "E"
    elif degree == 90:
        return "S"
    elif degree == 180:
        return "W"
    elif degree == 270:
        return "N"



def day_12_2(inp):
    dx, dy = 0, 0
    wx, wy = 10, 1
    sx, sy = 0, 0
    for z in inp:
        k = re.match(r"([\w])([0-9]+)", z)
        if k[1] == "R":
            wx,wy = rotate((sx,sy), (wx,wy),-int(k[2]))
        elif k[1] == "L":
            wx,wy = rotate((sx,sy), (wx,wy),int(k[2]))
        if k[1] == "F":
            for x in range(int(k[2])):
                dx, dy = wx-sx, wy-sy
                sx, sy = wx, wy
                wx, wy = sx+dx, sy+dy
        if k[1] == "N":
            wy += int(k[2])
        elif k[1] == "S":
            wy -= int(k[2])
        elif k[1] == "E":
            wx += int(k[2])
        elif k[1] == "W":
            wx -= int(k[2])
    print(f"waypoint X: {wx},waypoint Y: {wy}")
    print(f"manhattan distance: {abs(sx)+abs(sy)}")



def day_12_1(inp):
    x, y = 0, 0
    dir = 0
    for z in inp:
        k = re.match(r"([\w])([0-9]+)", z)
        if k[1] == "R":
            dir += int(k[2])
        elif k[1] == "L":
            dir -= int(k[2])
        if k[1] == "F":
            k = [k[0],degree_to_direction(dir), k[2]]
        if k[1] == "N":
            y += int(k[2])
        elif k[1] == "S":
            y -= int(k[2])
        elif k[1] == "E":
            x += int(k[2])
        elif k[1] == "W":
            x -= int(k[2])
    print(f"X: {x},Y: {y},dir: {dir}")
    print(f"manhattan distance: {abs(x)+abs(y)}")

if __name__ == '__main__':
    raw_input = get_input(12)
    day_12_2(raw_input)
