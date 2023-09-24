from __future__ import annotations

from .useful_in_development import *
from .cevians_and_perpendiculars import *
from .intersection import *

from ManimExtra.mobject.geometry.line import Line, Angle
from ManimExtra.mobject.geometry.arc import Dot, Circle

__all__ = [
    "Incenter",
    "Excenter",
    "Centroid",
    "Circumcenter",
    "Orthocenter",
    "NinePointCenter",
    "LemoinePoint",
    "GergonnePoint",
    "NagelPoint",
    "SpiekerCenter",
    "FeuerbachPoint"
]


def sec(alpha) -> float:
    return 1 / np.cos(alpha)


class Incenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(trilinear_to_cartesian(A, B, C, (1, 1, 1)), **kwargs)


class Excenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(trilinear_to_cartesian(A, B, C, (1, -1, 1)), **kwargs)


class Centroid(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        a, b, c = distance(B, C), distance(A, C), distance(A, B)
        super().__init__(trilinear_to_cartesian(A, B, C, (1 / a, 1 / b, 1 / c)), **kwargs)


class Circumcenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        angle_a = Angle().from_three_points(B, A, C).get_value()
        angle_b = Angle().from_three_points(A, B, C).get_value()
        angle_c = Angle().from_three_points(B, C, A).get_value()
        super().__init__(trilinear_to_cartesian(A, B, C, (np.cos(angle_a), np.cos(angle_b), np.cos(angle_c))), **kwargs)


class Orthocenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        angle_a = Angle().from_three_points(B, A, C).get_value()
        angle_b = Angle().from_three_points(A, B, C).get_value()
        angle_c = Angle().from_three_points(B, C, A).get_value()
        super().__init__(trilinear_to_cartesian(A, B, C, (sec(angle_a), sec(angle_b), sec(angle_c))), **kwargs)


class NinePointCenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        angle_a = Angle().from_three_points(B, A, C).get_value()
        angle_b = Angle().from_three_points(A, B, C).get_value()
        angle_c = Angle().from_three_points(B, C, A).get_value()
        super().__init__(trilinear_to_cartesian(
            A, B, C, (np.cos(angle_b - angle_c), np.cos(angle_c - angle_a), np.cos(angle_a - angle_b))), **kwargs)


class LemoinePoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        a, b, c = distance(B, C), distance(A, C), distance(A, B)
        super().__init__(trilinear_to_cartesian(A, B, C, (a, b, c)), **kwargs)


class GergonnePoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        a, b, c = distance(B, C), distance(A, C), distance(A, B)
        super().__init__(trilinear_to_cartesian(A, B, C, (
            (b * c / (b + c - a)), (c * a / (c + a - b)), (a * b / (a + b - c))
        )), **kwargs)


class NagelPoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        a, b, c = distance(B, C), distance(A, C), distance(A, B)
        super().__init__(trilinear_to_cartesian(A, B, C, (
            ((b + c - a) / a), ((c + a - b) / b), ((a + b - c) / c)
        )), **kwargs)


class Mittenpunkt(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        a, b, c = distance(B, C), distance(A, C), distance(A, B)
        super().__init__(trilinear_to_cartesian(A, B, C, (
            (b + c - a), (c + a - b), (a + b - c)
        )), **kwargs)

class SpiekerCenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        a, b, c = distance(B, C), distance(A, C), distance(A, B)
        super().__init__(trilinear_to_cartesian(A, B, C, (
            (b * c * (b + c)), (a * c * (a + c)), (b * a * (b + a))
        )), **kwargs)


class FeuerbachPoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        angle_a = Angle().from_three_points(B, A, C).get_value()
        angle_b = Angle().from_three_points(A, B, C).get_value()
        angle_c = Angle().from_three_points(B, C, A).get_value()
        super().__init__(trilinear_to_cartesian(A, B, C, (
            (1 - np.cos(angle_b - angle_c)), (1 - np.cos(angle_c - angle_a)), (1 - np.cos(angle_a - angle_b))
        )), **kwargs)
