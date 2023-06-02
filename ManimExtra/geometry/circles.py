from manim import *
from .chevians import Triangle_height

def Incenter(A: Dot, B: Dot, C: Dot):
    a = Line(B.get_center(), C.get_center()).get_length()
    b = Line(A.get_center(), C.get_center()).get_length()
    c = Line(A.get_center(), B.get_center()).get_length()

    x = (c*C.get_center()[0] + b*B.get_center()[0] + a*A.get_center()[0])/(a+b+c)
    y = (c*C.get_center()[1] + b*B.get_center()[1] + a*A.get_center()[1])/(a+b+c)

    I = Dot(np.array([x,y,0]))
    return I

def Incircle(A: Dot, B: Dot, C: Dot):
    I = Incenter(A,B,C)
    h = Triangle_height(A,I,C).get_length()
    circle = Circle(radius=h).move_to(I.get_center())
    return circle