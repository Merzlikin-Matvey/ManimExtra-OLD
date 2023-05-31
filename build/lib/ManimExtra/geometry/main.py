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

def Angle_bisector(A: Dot, B: Dot, C: Dot, length=1, adapt=True):
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
    I = Dot(B.get_center()+np.array([delta_x,delta_y,0]))
    bisector = Line(B.get_center(),I.get_center())
    return bisector