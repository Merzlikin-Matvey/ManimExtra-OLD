[![Текст с описанием картинки](logo/dark-logo.jpeg)](https://github.com/Merzlikin-Matvey/ManimExtra/blob/main/logo/dark-logo.jpeg)

Manim is an animation engine for explanatory math videos. It's used to create precise animations programmatically, as demonstrated in the videos of [3Blue1Brown](https://www.3blue1brown.com/).

> This repository is maintained by me and is not affiliated with Grant Sanderson, 3Blue1Brown or Manim Community. I wrote this version of Manim primarily for my own purposes. Most of the code was taken from the Manim Community repository

## Examples

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


## License

The software is triple-licensed under the MIT license, with copyright by 3blue1brown LLC (see LICENSE), by Manim Community Developers (see LICENSE.community) and Merzlikin Matvey (see LICENSE.merzlikin).
