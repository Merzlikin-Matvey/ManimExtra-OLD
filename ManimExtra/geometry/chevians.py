from manimlib import *
from .angle import *

def Triangle_chevian(A: Dot, B: Dot, C: Dot, alpha=0.375, color=WHITE,
                     dot=False, dot_radius=0.2,dot_color=WHITE):
    b = Line(A.get_center(),C.get_center())
    X = Dot(b.point_from_proportion(alpha),radius=dot_radius,color=dot_color)
    if dot:
        return (Line(B.get_center(),X.get_center(),color),X)
    else:
        Line(B.get_center(), X.get_center(), color)


def Bisector(A: Dot, B: Dot, C: Dot, length=-1, color=WHITE,
             dot=False, dot_radius=0.2,dot_color=WHITE):
    a = Line(B.get_center(), C.get_center()).get_length()
    b = Line(A.get_center(), C.get_center()).get_length()
    c = Line(B.get_center(), A.get_center()).get_length()
    if length == -1:
        length = (2*a*c)/(a+c) * np.cos(Angle_from_three_points(A,B,C).get_value()/2)
    if Angle_from_three_points(A,B,C,adapt=False).get_value() > PI:
        I = Dot(C.get_center()).rotate(
                -Angle_from_three_points(A,B,C).get_value()/2,
                about_point=B.get_center()
            )
    else:
        I = Dot(C.get_center()).rotate(
            Angle_from_three_points(A, B, C).get_value() / 2,
            about_point=B.get_center()
        )
    tmp = Line(B.get_center(),I.get_center()).get_length()
    delta_x = (I.get_center()[0]-B.get_center()[0])*(length/tmp)
    delta_y = (I.get_center()[1]-B.get_center()[1])*(length/tmp)
    I = Dot(B.get_center()+np.array([delta_x,delta_y,0]),radius=dot_radius,color=dot_color)
    bisector = Line(B.get_center(),I.get_center(),color=color)
    if dot:
        return (bisector,I)
    else:
        return bisector

def Median(A: Dot, B: Dot, C: Dot, color=WHITE,
           dot=False, dot_radius=0.2,dot_color=WHITE):
    return Triangle_chevian(A,B,C,0.5,color,dot)

def Height(A: Dot, B: Dot, C: Dot, color=WHITE,
           dot=False, dot_radius=0.2,dot_color=WHITE):
    b = Line(A.get_center() ,C.get_center())
    H = Dot(b.get_projection(B.get_center()),radius=dot_radius,color=dot_color)
    if dot:
        return (Line(B.get_center(),H.get_center(),color), H)
    else:
        return Line(B.get_center(),H.get_center(),color)

def Symmedian(A: Dot, B: Dot, C: Dot, color=WHITE,
              dot=False, dot_radius=0.2,dot_color=WHITE):
    a = Line(B.get_center(), C.get_center()).get_length()
    c = Line(B.get_center(), A.get_center()).get_length()
    return Triangle_chevian(A,B,C,1-a**2/(c**2+a**2),color,dot,dot_radius,dot_color)

