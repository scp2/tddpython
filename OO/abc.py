from abc import ABC

from collections.abc import MutableSequence, Sized
from numbers import Complex
from typing import ClassVar


class Playlist(MutableSequence):
    pass

class Number(Complex):
    pass


test = Playlist() # TypeError: Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
number = Number() # TypeError: Can't instantiate abstract class Number with abstract methods __abs__, __add__, __complex__, __eq__, __mul__, __neg__, __pos__, __pow__, __radd__, __rmul__, __rpow__, __rtruediv__, __truediv__, conjugate, imag, real

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

lista = MinhaListagem()
print(lista)