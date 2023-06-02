from manim import *


def Angle_from_three_points(A: Dot, B: Dot, C: Dot, radius=0.3, color=WHITE, adapt=True):
    angle = Angle(
        Line(B.get_center(), C.get_center()),
        Line(B.get_center(), A.get_center()),
        radius=radius, color=color
    )
    if angle.get_value() > PI and adapt:
        angle = Angle(
            Line(B.get_center(), A.get_center()),
            Line(B.get_center(), C.get_center()),
            radius=radius, color=color
        )
    return angle


