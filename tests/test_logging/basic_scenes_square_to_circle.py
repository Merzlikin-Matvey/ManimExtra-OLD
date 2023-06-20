from __future__ import annotations

from ManimExtra import *

# This module is used in the CLI tests in tests_CLi.py.


class SquareToCircle(Scene):
    def construct(self):
        self.play(Transform(Square(), Circle()))
