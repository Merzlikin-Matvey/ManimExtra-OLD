![Текст с описанием картинки](logo/extra/dark_logo.jpg)

Manim is an animation engine for explanatory math videos. It's used to create precise animations programmatically, as demonstrated in the videos of [3Blue1Brown](https://www.3blue1brown.com/).

> This repository is maintained by me and is not affiliated with Grant Sanderson, 3Blue1Brown or Manim Community. I wrote this version of Manim primarily for my own purposes. Most of the code was taken from the Manim Community repository

## Usage

Manim is an extremely versatile package. The following is an example `Scene` you can construct:

```python
from ManimExtra import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

In order to view the output of this scene, save the code in a file called `example.py`. Then, run the following in a terminal window:

```
ManimExtra -qh example.py SquareToCircle
```


## Command line arguments

The general usage of ManimExtra is as follows:

```ManimExtra``` The command calling ManimExtra

Next, the video quality is set  
```-qk``` 4k 60fps  
```-qh``` FullHD 60fps     
```-ql``` 480p 15fps   

```file.py``` The name of the file where the project is located

```MyScene``` The name of the scene in this file

## Documentation
My version of MinimExtra largely repeats the original version of Manim from Manim Community. The documentation of their version can be read about the link: https://docs.manim.community/en/stable/#        

A brief description of the functions that are added to my version of the project

***
## Classes
### ```Cevian```(A, B, C - np.ndarray, alpha - float) -> Line
> The Line connecting the vertex of the triangle _B_ and the point on the opposite side _AC_. This point divides the side into segments that relate to each other as _alpha_


### ```Median```(A, B, C - np.ndarray) -> Cevian
> The median of the triangle coming out of the vertex _B_


### ```Bisector```(A, B, C - np.ndarray) -> Cevian 
> The bisector of the triangle coming out of the vertex _B_


### ```Altitude```(A, B, C - np.ndarray) -> Cevian
> The altitude of the triangle coming out of the vertex _B_


### Example 
```python
from ManimExtra import * 

class scene(Scene):
    def construct(self):
        A = Dot(2*DOWN+3*LEFT).set_z_index(10)
        B = Dot(2*UP).set_z_index(10)
        C = Dot(2*DOWN+4*RIGHT).set_z_index(10)
        self.add(A,B,C)
        
        a = Line(B.get_center(), C.get_center(), color = BLUE)
        b = Line(A.get_center(), C.get_center(), color = BLUE)
        c = Line(A.get_center(), B.get_center(), color = BLUE)

        self.add(a,b,c)

        cevian = Cevian(A.get_center(),B.get_center(),C.get_center(),0.3,color=RED)
        self.add(cevian, Dot(cevian.dot))

        

```

### ```InscribedCircle```(A, B, C - np.ndarray) -> Circle
> The inscribed circle of the triangle ABC

### ```CircumscribedCircle```(A, B, C - np.ndarray) -> Circle
> The circumscribed circle of the triangle ABC

### ```NinePointCircle```(A, B, C - np.ndarray) -> CircumscribedCircle
> Euler circle of triangle ABC

```python
from ManimExtra import * 

class scene(Scene):
    def construct(self):
        A = Dot(DOWN+2*LEFT).set_z_index(10)
        B = Dot(2*UP).set_z_index(10)
        C = Dot(DOWN+3*RIGHT).set_z_index(10)

        a = Line(B.get_center(),C.get_center(), color=BLUE)
        b = Line(A.get_center(),C.get_center(), color=BLUE)
        c = Line(B.get_center(),A.get_center(), color=BLUE)

        self.add(A,B,C,a,b,c)
        circle = InscribedCircle(A.get_center(),B.get_center(),C.get_center())
        self.add(circle,Dot(circle.get_center()))

        
```


***
## Functions

### ```intersection_lines```(line_1, line_2 - Line) -> Dot
> Returns their intersection Dot

### ```intersection_circles```(circle_1, circle_2 - Circle) -> VGroup(Dot)
> Returns a VGroup of 2 Dots if they intersect, 1 point if they touch, an empty set otherwise

### 

## License

The software is triple-licensed under the MIT license, with copyright by 3blue1brown LLC (see LICENSE), by Manim Community Developers (see LICENSE.community) and Merzlikin Matvey (see LICENSE.merzlikin).
