from manim import *

def Angle_from_three_points(A: Dot, B: Dot, C: Dot, radius=0.3, color=WHITE):
    return Angle(
        Line(B.get_center(), C.get_center()),
        Line(B.get_center(), A.get_center()),
        radius=radius, color=color
    )