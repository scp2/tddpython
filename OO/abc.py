from abc import ABC

from collections.abc import MutableSequence
from numbers import Complex
from typing import ClassVar

class Playlist(MutableSequence):
    pass

class Number(Complex):
    pass


test = Playlist()
number = Number()
