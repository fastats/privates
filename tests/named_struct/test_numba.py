
import sys
from unittest import skipUnless as skip_unless

import numpy as np
try:
    import numba
    from numba import jitclass

    from numba.types import (
        intp, float64
    )
except ImportError:
    numba = None

from privates import NamedStruct

FAIL_MSG = "Numba not found"


class Point(NamedStruct):
    x: float64
    y: float64

    def distance_from_origin(self):
        return np.sqrt(self.x**2 + self.y**2)


class Rectangle(Point):
    width: float64
    height: float64

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


@skip_unless(numba, FAIL_MSG)
def test_create_api():
    global Rectangle

    norm = Rectangle(x=0, y=1, height=5, width=6)
    assert norm.x == 0
    assert norm[0] == 0
    assert norm.y == 1
    assert norm[1] == 1
    assert norm.height == 5
    # assert norm[2] == 5  # TODO : need Struct.init
    assert norm.width == 6
    # assert norm[3] == 6
    assert norm.distance_from_origin() == 1
    assert norm.area() == 30

    r = Rectangle.create(x=0, y=1, height=5, width=6)
    assert r.x == 0
    assert r.y == 1
    assert r.height == 5
    assert r.width == 6
    assert r.area() == 30
    assert r.distance_from_origin() == 1.0

    r2 = Rectangle.create(x=0, y=1, height=6, width=7)
    assert r2.area() == 42
    assert r2.distance_from_origin() == 1.0

    r3 =  Rectangle.create(x=3.0, y=4.0, height=3, width=4)
    assert r3.area() == 12
    assert r3.distance_from_origin() == 5.0