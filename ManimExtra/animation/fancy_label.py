from __future__ import annotations

__all__ = [
    "Fancy_label"
]

from .creation import Write
from ManimExtra.mobject.text.tex_mobject import Tex
from ManimExtra.constants import *
from ManimExtra.animation.composition import AnimationGroup


def Fancy_label(text: Tex, mode='normal', buff=MED_LARGE_BUFF):
    mode = mode.lower()
    modes = ['vlow', 'low', 'normal', 'fast', 'vfast']

    if mode not in modes:
        mode = 'normal'


    symbols = len(text.get_tex_string())
    time = (symbols / (9+modes.index(mode))) + 0.25

    return AnimationGroup(Write(text.to_edge(UP, buff=buff).set_z_index(999)), run_time=time)
