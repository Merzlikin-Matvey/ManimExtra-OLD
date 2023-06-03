from manim import *
import sys

sys.setrecursionlimit(2000)

def Koch_curve(n=4, length=7, stroke_width=5, color=WHITE):
    LineGroup = Line().set_length(length / (3 ** n))
    def NextLevel(LineGroup):
        return VGroup(
            *[LineGroup.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]
        ).arrange(RIGHT, buff=0, aligned_edge=DOWN)

    for _ in range(n):
        LineGroup = NextLevel(LineGroup)
    KC = (
        VMobject(stroke_width=stroke_width)
        .set_points(LineGroup.get_all_points())
        .set_color(color)
    )
    if n == 0:
        KC.move_to(Koch_curve(2, length, stroke_width, color).get_center())
    else:
        KC.move_to(ORIGIN)
    return KC