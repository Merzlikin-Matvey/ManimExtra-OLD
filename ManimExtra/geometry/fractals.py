from manimlib import *
import scipy.special
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

def Sierpinski_triangle(n,color=WHITE):
    t1 = Triangle(color=BLUE, stroke_color=color).shift(UP).set_opacity(1).set_stroke(opacity=0)
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
    v = Square(side_length=1,color=color).set_opacity(1).set_stroke(opacity=0)
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

def Pascal_Triangle(n):
    def level(n,width):
        v = VGroup(*(Square(side_length=1,stroke_width=width) for i in range(n)))
        return v.arrange(buff=0.17)

    def triangle(n):
        v = VGroup()
        for i in range(1, n + 1):
            width = 4
            if n > 4:
                width -= 0.1*n
            x = level(i,width)
            v += x
        return v.arrange(buff=0.1, direction=DOWN).move_to(ORIGIN)

    def numbers(n):
        m = []
        for i in range(n):
            x = []
            for j in range(i + 1):
                x.append(scipy.special.comb(i, j, exact=True))
            m.append(x)
        return m

    pascal_triangle = triangle(n)
    pascal_numbers = numbers(n)

    result = VGroup()
    for i in range(n):
        v = VGroup()
        for j in range(i+1):
            v += pascal_triangle[i][j]
        for j in range(i+1):
            font = 42
            if len(str(pascal_numbers[i][j])) > 2:
                font -= len(str(pascal_numbers[i][j]))*2.5
            v += Tex(str(pascal_numbers[i][j]),font_size=font).move_to(pascal_triangle[i][j].get_center())
        result += v
    return result


