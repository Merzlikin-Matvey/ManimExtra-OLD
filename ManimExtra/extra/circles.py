from .useful_in_development import *
from .intersection import *
from .cevians_and_perpendiculars import *
from .triangle_centers import *
import numpy as np

from ManimExtra.mobject.geometry.arc import Dot, Circle
from ManimExtra.mobject.geometry.line import Line

__all__ = [
    "Tangent",
    "RadicalAxis",
    "Incircle",
    "Circumcircle",
    "NinePointCircle"
]


class Tangent(Line):
    def __init__(self, circle: Circle, dot, length=1, up_right=True, **kwargs):
        dot = dot_to_array(dot)[0]
        if circle.pow(dot) > 0:
            tangent_length = np.sqrt(circle.pow(dot))
            extra_circle = Circle(arc_center=dot, radius=tangent_length)
            tangent_point = sorted(intersection_circles(circle, extra_circle), reverse=up_right, key=lambda m: m[0])[0]
            tangent = Line(dot, tangent_point, )
        elif circle.pow(dot) == 0:
            tangent = Perpendicular(Line(circle.get_center(), dot), dot).set_length(length).move_to(dot)
        else:
            raise Exception("It is impossible to draw a tangent through this point")
        self.point_of_tangency = intersection_line_and_circle(tangent, circle)[0]
        super().__init__(tangent.get_start(), tangent.get_end(), **kwargs)

    def get_point_of_tangency(self) -> np.ndarray:
        return self.point_of_tangency


class RadicalAxis(Line):
    def __init__(self, circle_1: Circle, circle_2: Circle, length=1, **kwargs):
        x1, y1 = circle_1.get_center()[0], circle_1.get_center()[1],
        x2, y2 = circle_2.get_center()[0], circle_2.get_center()[1],
        r1, r2 = circle_1.radius, circle_2.radius

        if x1 != x2:
            y0 = 2 * abs(max(y1, y2))
            x0 = (x2 ** 2 - x1 ** 2 + 2 * y0 * (y1 - y2) + y2 ** 2 - y1 ** 2 + r1 ** 2 - r2 ** 2) / (2 * (x2 - x1))
            perpendicular = Perpendicular(Line(circle_1.get_center(), circle_2.get_center()), np.array([x0, y0, 0]))
            perpendicular.set_length(length).move_to(perpendicular.get_foot())
        elif y1 != y2:
            x0 = 2 * abs(max(x1, x2))
            y0 = (x2 ** 2 - x1 ** 2 + 2 * x0 * (x1 - x2) + y2 ** 2 - y1 ** 2 + r1 ** 2 - r2 ** 2) / (2 * (y2 - y1))
            perpendicular = Perpendicular(Line(circle_1.get_center(), circle_2.get_center()), np.array([x0, y0, 0]))
            perpendicular.set_length(length).move_to(perpendicular.get_foot())
        else:
            raise Exception("Concentric circles do not have a radical axis")

        self.foot = perpendicular.get_foot()

        super().__init__(perpendicular.get_start(), perpendicular.get_end(), **kwargs)

    def get_foot(self) -> np.ndarray:
        return self.foot


class Incircle(Circle):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        I = Incenter(A, B, C)
        super().__init__(arc_center=I, radius=Line(A, B).get_distance(I), **kwargs)


class Circumcircle(Circle):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        O = Circumcenter(A, B, C)
        super().__init__(arc_center=O, radius=distance(O, A), **kwargs)
        

class NinePointCircle(Circumcircle):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__((A+B)/2, (B+C)/2, (A+C)/2, **kwargs)
