from __future__ import annotations

__all__ = [
    "Fancy_label"
]

from .creation import Write
from ManimExtra.mobject.text.tex_mobject import Tex
from ManimExtra.constants import UP
from ManimExtra.animation.composition import AnimationGroup


def Fancy_label(text: Tex, mode='normal'):
    mode = mode.lower()
    modes = ['vlow', 'low', 'normal', 'fast', 'vfast']

    if mode not in modes:
        mode = 'normal'

    symbols = 0
    for i in range(len(text.get_tex_string().split('$'))):
        if i % 2 == 0:
            symbols += len(text.get_tex_string().split('$')[i])
        else:
            symbols += len(text.get_tex_string().split('$')[i]) / 1.5

    time = symbols / (5.8*modes.index(mode)) + 0.2

    return AnimationGroup(Write(text.to_edge(UP).set_z_index(999)), run_time=time)
