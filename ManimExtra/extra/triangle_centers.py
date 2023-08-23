from __future__ import annotations

from .useful_in_development import *
from .cevians_and_perpendiculars import *
from .intersection import *

from ManimExtra.mobject.geometry.line import Line
from ManimExtra.mobject.geometry.arc import Dot, Circle

__all__ = [
    "Incenter",
    "Excenter",
    "Centroid",
    "Circumcenter",
    "Orthocenter",
    "NinePointCenter",
    "LemoinePoint",
    "GergonnePoint"
]

class Incenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(Bisector(A, B, C), Bisector(A, C, B)), **kwargs)


class Excenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(Bisector(A, B, C),
                                            Bisector(A, C, Line(B, C).scale(2).get_end())), **kwargs)


class Centroid(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(Median(A, B, C), Median(A, C, B)), **kwargs)


class Circumcenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(
            PerpendicularBisector(line=Line(A, B)), PerpendicularBisector(line=Line(A, C))), **kwargs)


class Orthocenter(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(Altitude(A, B, C), Altitude(A, C, B)), **kwargs)


class NinePointCenter(Circumcenter):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__((A + B) / 2, (A + C) / 2, (B + C) / 2, **kwargs)


class LemoinePoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(Symmedian(A, B, C), Symmedian(A, C, B)), **kwargs)


class GergonnePoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(
            Line(A, Line(B, C).get_projection(Incenter(A, B, C).get_center())),
            Line(B, Line(A, C).get_projection(Incenter(A, B, C).get_center())),
        ), **kwargs)


class NagelPoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_lines(
            Line(A, Line(B, C).get_projection(Excenter(B, A, C).get_center())),
            Line(B, Line(A, C).get_projection(Excenter(A, B, C).get_center())),
        ), **kwargs)


class SpiekerCenter(Incenter):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__((A + B) / 2, (A + C) / 2, (B + C) / 2, **kwargs)


class FeuerbachPoint(Dot):
    def __init__(self, A, B, C, **kwargs):
        A, B, C = dot_to_array(A, B, C)
        super().__init__(intersection_line_and_circle(
            Line(Incenter(A, B, C), NinePointCenter(A, B, C)),
            Circle().from_three_points((A+B)/2, (A+C)/2, (B+C)/2))[0], **kwargs)
