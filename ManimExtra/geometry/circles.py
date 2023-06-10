from manimlib import *
from .chevians import Height

def Incenter(A: Dot, B: Dot, C: Dot, radius, color=WHITE):
    a = Line(B.get_center(), C.get_center()).get_length()
    b = Line(A.get_center(), C.get_center()).get_length()
    c = Line(A.get_center(), B.get_center()).get_length()

    x = (c*C.get_center()[0] + b*B.get_center()[0] + a*A.get_center()[0])/(a+b+c)
    y = (c*C.get_center()[1] + b*B.get_center()[1] + a*A.get_center()[1])/(a+b+c)

    I = Dot(np.array([x,y,0]), radius, color)
    return I

def Incircle(A: Dot, B: Dot, C: Dot, color=WHITE):
    I = Incenter(A,B,C)
    h = Height(A,I,C).get_length()
    circle = Circle(radius=h,color=color).move_to(I.get_center())
    return circle

def Circumscribed_circle(A: Dot, B: Dot, C: Dot, color=WHITE):
    return Circle().from_three_points(A.get_center(), B.get_center(), C.get_center())

def Circumscribed_circle_centre(A: Dot, B: Dot, C: Dot, color=WHITE):
    return Dot(Circumscribed_circle(A,B,C).get_center())

def Eulers_circle(A: Dot, B: Dot, C: Dot, color=WHITE):
    a = Line(B.get_center(), C.get_center())
    b = Line(A.get_center(), C.get_center())
    c = Line(A.get_center(), B.get_center())

    Ma = Dot(a.point_from_proportion(0.5))
    Mb = Dot(b.point_from_proportion(0.5))
    Mc = Dot(c.point_from_proportion(0.5))

    return Circle().from_three_points(Ma.get_center(), Mb.get_center(), Mc.get_center())