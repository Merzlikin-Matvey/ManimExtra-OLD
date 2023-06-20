from __future__ import annotations

import pkg_resources

from ManimExtra import __name__, __version__


def test_version():
    assert __version__ == pkg_resources.get_distribution(__name__).version
