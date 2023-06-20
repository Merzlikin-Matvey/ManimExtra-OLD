"""Plugin Managing Utility"""

from __future__ import annotations

import pkg_resources

from ManimExtra import console

__all__ = ["list_plugins"]


def get_plugins():
    plugins = {
        entry_point.name: entry_point.load()
        for entry_point in pkg_resources.iter_entry_points("ManimExtra.plugins")
    }
    return plugins


def list_plugins():
    console.print("[green bold]Plugins:[/green bold]", justify="left")

    plugins = get_plugins()
    for plugin in plugins:
        console.print(f" • {plugin}")
