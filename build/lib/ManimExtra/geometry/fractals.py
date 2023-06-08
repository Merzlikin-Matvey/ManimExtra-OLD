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

def Sierpinski_triangle(n):
    t1 = Triangle(color=BLUE, stroke_color=RED).shift(UP).set_opacity(1).set_stroke(opacity=0)
    t2 = t1.copy().rotate(about_point=ORIGIN, angle=2 * PI / 3)
    t3 = t1.copy().rotate(about_point=ORIGIN, angle=-2 * PI / 3)

    v = VGroup(t1, t2, t3).scale(0.5).move_to(Triangle().get_center()).shift(UP)
    for i in range(n-1):
        v2 = v.copy().rotate(about_point=ORIGIN, angle=2 * PI / 3)
        v3 = v.copy().rotate(about_point=ORIGIN, angle=-2 * PI / 3)
        v = VGroup(v, v2, v3).scale(0.5).move_to(Triangle().get_center()).shift(UP)
    v.scale(2).move_to(Triangle().get_center())
    return v

def Sierpinski_carpet(n,color=BLUE):
    v = Square(side_length=1,color=color).set_opacity(1)
    for _ in range(n):
        v.shift(DOWN)
        x1 = v.copy().shift(2*UP)
        x2 = v.copy().shift(UP).shift(RIGHT)
        x3 = v.copy().shift(UP).shift(LEFT)
        x4 = v.copy().shift(RIGHT)
        x5 = v.copy().shift(LEFT)
        x6 = v.copy().shift(2*UP).shift(RIGHT)
        x7 = v.copy().shift(2*UP).shift(LEFT)
        v = VGroup(v,x1,x2,x3,x4,x5,x6,x7).scale(1/3)
    return v.scale(3)

