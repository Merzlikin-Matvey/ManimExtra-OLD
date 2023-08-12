from __future__ import annotations

import numpy as np
from .arc import Dot, Circle
from .line import Line
from ManimExtra.mobject.types.vectorized_mobject import VGroup

__all__ = [
    "intersection_lines",
    "intersection_circles",
    "intersection_line_and_circle"
]

def intersection_lines(line_1: Line,line_2: Line):
    k1 = line_1.get_slope()
    k2 = line_2.get_slope()

    b1 = line_1.start[1] - k1 * line_1.start[0]
    b2 = line_2.start[1] - k2 * line_2.start[0]

    if k1-k2 == 0:
        raise Exception('Lines are parallel')
    x = (b2-b1)/(k1-k2)
    y = k1*x+b1
    return np.array([x,y,line_1.start[-1]])



def intersection_circles(circle_1: Circle, circle_2: Circle):
    o1 = circle_1.get_center()
    o2 = circle_2.get_center()
    r1 = circle_1.radius
    r2 = circle_2.radius
    l = Line(o1,o2).get_length()
    print(l,r1,r2)
    if l > r1+r2:
        raise Exception('Circles do not intersect')

    x1 = Dot(Line(o1,o2).set_length_about_point(o1,r1).get_end())
    x2 = x1.copy()

    alpha = np.arccos((r2**2 - r1**2 - l**2)/(-2*r1*l))
    x1.rotate(about_point=o1, angle=alpha)
    x2.rotate(about_point=o1, angle=-alpha)
    print([x1.get_center(), x2.get_center()])
    return [x1.get_center(), x2.get_center()]


def intersection_line_and_circle(line: Line, circle: Circle):
    o, r = circle.get_center() , circle.radius
    h = Line(line.get_projection(o),o).get_length()
    if h > r: return VGroup()
    alpha = np.arccos(h/r)
    x1 = Dot(Line(o,line.get_projection(o)).set_length_about_point(o,r).get_end())
    x2 = x1.copy()
    x1.rotate(about_point=o,angle=alpha)
    x2.rotate(about_point=o, angle=-alpha)
    return [x1.ger_center(), x2.get_center()]

