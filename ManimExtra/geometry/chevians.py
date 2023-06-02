from manim import *
import numpy as np


def Triangle_bisector(A: Dot, B: Dot, C: Dot):
    a = Line(B.get_center(), C.get_center()).get_length()
    b = Line(A.get_center(), C.get_center())
    c = Line(B.get_center(), A.get_center()).get_length()
    x = (a*b.get_length())/(a+c)
    I = Dot(b.point_from_proportion(1-x/b.get_length()))
    return Line(A.get_center(),I.get_center())

def Triangle_median(A: Dot, B: Dot, C: Dot):
    b = Line(A.get_center(),C.get_center())
    M = Dot(b.point_from_proportion(0.5))
    return Line(B.get_center(),M.get_center())

def Triangle_height(A: Dot, B: Dot, C: Dot):
    b = Line(A.get_center(),C.get_center())
    H = Dot(b.get_projection(B.get_center()))
    return Line(B.get_center(),H.get_center())

def Triangle_chevian(A: Dot, B: Dot, C: Dot, alpha=0.375):
    b = Line(A.get_center(),C.get_center())
    X = Dot(b.point_from_proportion(alpha))
    return Line(B.get_center(),X.get_center())
