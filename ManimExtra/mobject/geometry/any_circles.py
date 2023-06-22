from __future__ import annotations

import numpy as np
from .arc import Dot, Circle
from .line import Line, Angle


__all__ = [
    "InscribedCircle",
    "CircumscribedCircle",
    "NinePointCircle",
]

class InscribedCircle(Circle):

    def __init__(self, A: np.ndarray, B: np.ndarray,C: np.ndarray, **kwargs):
        a, b, c = Line(B, C).get_length(), Line(A, C).get_length(), Line(B, A).get_length()
        x = (a * A[0] + b * B[0] + c * C[0]) / (a + b + c)
        y = (a * A[1] + b * B[1] + c * C[1]) / (a + b + c)
        I = np.array([x,y,A[2]])
        super().__init__(radius=Line(A,B).get_distance(I),arc_center=I, **kwargs)

class CircumscribedCircle(Circle):

    def __init__(self, A: np.ndarray, B: np.ndarray,C: np.ndarray, **kwargs):
        o = Circle().from_three_points(A,B,C).get_center()
        r = Line(A,B).get_length()/(2*np.sin(Angle().from_three_points(A,C,B).get_value()))
        super().__init__(radius=r,arc_center=o, **kwargs)


class NinePointCircle(CircumscribedCircle):

    def __init__(self, A: np.ndarray, B: np.ndarray,C: np.ndarray, **kwargs):
        M1 = Line(A, B).point_from_proportion(0.5)
        M2 = Line(A, C).point_from_proportion(0.5)
        M3 = Line(C, B).point_from_proportion(0.5)
        super().__init__(M1,M2,M3,**kwargs)