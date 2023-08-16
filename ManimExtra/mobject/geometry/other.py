from __future__ import annotations

import numpy as np
from .arc import Dot, Circle
from .line import Line, Angle
from .intersection import intersection_lines
from ...constants import *
from ManimExtra.mobject.types.vectorized_mobject import VGroup



__all__ = [
    "InscribedCircle",
    "ExscribedCircle",
    "CircumscribedCircle",
    "EulerCircle",
    "RadicalAxis",
    "Tangent",
    "PerpendicularBisector",
    "Cevian",
    "Bisector",
    "Median",
    "Altitude",
    "Perpendicular"

]

class InscribedCircle(Circle):

    def __init__(self, A: np.ndarray, B: np.ndarray,C: np.ndarray, **kwargs):
        a, b, c = Line(B, C).get_length(), Line(A, C).get_length(), Line(B, A).get_length()
        x = (a * A[0] + b * B[0] + c * C[0]) / (a + b + c)
        y = (a * A[1] + b * B[1] + c * C[1]) / (a + b + c)
        I = np.array([x,y,A[2]])
        super().__init__(radius=Line(A,B).get_distance(I),arc_center=I, **kwargs)

class ExscribedCircle(Circle):
    def __init__(self, A: np.ndarray, B: np.ndarray,C: np.ndarray, **kwargs):
        biss_1 = Bisector(A, B, C)
        biss_2 = Bisector(A, C, B).rotate(about_point=C, angle=PI/2)
        I = intersection_lines(biss_1, biss_2)
        r = Line(I, Line(A, C).get_projection(I)).get_length()
        super().__init__(radius=r, arc_center=I, **kwargs)

class CircumscribedCircle(Circle):

    def __init__(self, A: np.ndarray, B: np.ndarray,C: np.ndarray, **kwargs):
        o = Circle().from_three_points(A,B,C).get_center()
        r = Line(A,B).get_length()/(2*np.sin(Angle().from_three_points(A,C,B).get_value()))
        super().__init__(radius=r,arc_center=o, **kwargs)


class EulerCircle(CircumscribedCircle):

    def __init__(self, A: np.ndarray, B: np.ndarray,C: np.ndarray, **kwargs):
        M1 = Line(A, B).point_from_proportion(0.5)
        M2 = Line(A, C).point_from_proportion(0.5)
        M3 = Line(C, B).point_from_proportion(0.5)
        super().__init__(M1,M2,M3,**kwargs)



class RadicalAxis(Line):

    def __init__(self, circle_1: Circle, circle_2: Circle):
        x1, y1 = circle_1.get_center()[0], circle_1.get_center()[1]
        x2, y2 = circle_2.get_center()[0], circle_2.get_center()[1]
        r1, r2 = circle_1.radius, circle_2.radius


        if x1 != x2:
            y0 = y1
            x0 = (x2**2 - x1**2 + 2*y0*y1 - 2*y0*y2 + y2**2 - y1**2 + r1**2 - r2**2)
        pass

class Tangent(Line):
    def __init__(self, circle: Circle, dot: np.ndarray, length=1, other=False, **kwargs):
        if round(circle.pow(dot), 2) == 0:
            tangent = Line(dot, circle.get_center()).move_to(dot).rotate(angle=PI/2).set_length(length)
            super().__init__(start=tangent.get_start(), end=tangent.get_end(), **kwargs)


        

class PerpendicularBisector(Line):
    def __init__(self, A: np.ndarray, B: np.ndarray, length=1, **kwargs):
        perpendicular_bisector = Line(A, B).rotate(angle=PI/2).move_to(Line(A, B).get_center()).set_length(length)
        super().__init__(perpendicular_bisector.get_start(), perpendicular_bisector.get_end())

class Cevian(Line):
    def __init__(self, A: np.ndarray, B: np.ndarray, C: np.ndarray, alpha = 0.5, **kwargs):
        D = Line(A,C).point_from_proportion(alpha)
        self.dot = D
        self.general_vertex = B
        self.extra_vertex_1 = A
        self.extra_vertex_2 = C
        super().__init__(B,D, **kwargs)


class Median(Cevian):
    def __init__(self, A=LEFT, B=RIGHT, C=UP, **kwargs):
        super().__init__(A, B, C, 0.5, **kwargs)

class Bisector(Cevian):
    def __init__(self, A=LEFT, B=RIGHT, C=UP,  **kwargs):
        alpha = ((Line(A,C).get_length()*Line(A,B).get_length())/(Line(B,C).get_length()+Line(A,B).get_length()))/Line(A,C).get_length()
        super().__init__(A, B, C, alpha, **kwargs)

class Altitude(Cevian):

    def __init__(self, A=LEFT, B=RIGHT, C=UP, **kwargs):
        x = np.cos(Angle().from_three_points(B,A,C).get_value()) * Line(A,B).get_length()
        super().__init__(A, B, C, x/Line(A,C).get_length(), **kwargs)

    def angles(self, **kwargs):
        angle_1 = Angle().from_three_points(self.general_vertex, self.dot, self.extra_vertex_1,elbow=True,**kwargs).set_z_index(-9)
        angle_2 = Angle().from_three_points(self.general_vertex, self.dot, self.extra_vertex_2,elbow=True,**kwargs).set_z_index(-9)
        return VGroup(angle_1,angle_2)


class Perpendicular(Line):
    def __init__(self, A: np.ndarray, B: np.ndarray, X: np.ndarray, length=1, **kwargs):
        if Line(A, B).is_point_in_line(X):
            perpendicular = Line(A, B).rotate(angle=PI / 2).move_to(X).set_length(length)
        else:
            perpendicular = Line(X, Line(A, B).get_projection(X)).set_length_about_point(
                Line(A, B).get_projection(X), length=length)
        super().__init__(perpendicular.get_start(), perpendicular.get_end(), **kwargs)




