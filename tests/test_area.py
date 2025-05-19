import unittest
from math import sqrt, isclose
from common.r3 import R3
from shadow.polyedr import Facet
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr
from tests.matchers import R3ApproxMatcher, R3CollinearMatcher

# Обычный квадрат 2х2 вне куба


def test_plane_outside_cube():
    test_file = "test_plane_outside.geom"
    with open(test_file, 'w') as f:
        f.write("10.0 0.0 0.0 0.0\n")
        f.write("4 1 4\n")
        f.write("1.0 1.0 1.0\n")
        f.write("1.0 -1.0 1.0\n")
        f.write("-1.0 -1.0 1.0\n")
        f.write("-1.0 1.0 1.0\n")
        f.write("4 1 2 3 4\n")
    poly = Polyedr(test_file)
    poly.area()
    expected_area = 400.0
    assert abs(poly.total_area - expected_area) < 1e-6
    import os
    os.remove(test_file)

# Многоугольник с рёбрами, не параллельными осям координат


def test_plane_inclined():
    test_file = "test_plane_inclined.geom"
    with open(test_file, 'w') as f:
        f.write("200.0	45.0	45.0	30.0\n")
        f.write("4 1 4\n")
        f.write("1.0 1.0 1.0\n")
        f.write("0.0 0.0 1.0\n")
        f.write("0.1 1.1 1.2\n")
        f.write("1.0 0.1 1.1\n")
        f.write("4 1 3 2 4\n")
    poly = Polyedr(test_file)
    poly.area()
    expected_area = 0.0
    assert abs(poly.total_area - expected_area) < 1e-6
    import os
    os.remove(test_file)

# Плоскости, одна из которых не является полностью видимой,
# а другая - имеет центр в единичном кубе


def test_ccc():
    test_file = "test_ccc.geom"
    with open(test_file, 'w') as f:
        f.write("40.0	120.0	30.0	-45.0\n")
        f.write("8	2	8\n")
        f.write("0.0 0.0 0.0\n")
        f.write("5.0 0.0 0.0\n")
        f.write("5.0 5.0 0.0\n")
        f.write("0.0 5.0 0.0\n")
        f.write("1.0 1.0 3.0\n")
        f.write("6.0 1.0 3.0\n")
        f.write("6.0 6.0 3.0\n")
        f.write("1.0 6.0 3.0\n")
        f.write("4	1    2    3    4\n")
        f.write("4	5    6    7    8\n")
    poly = Polyedr(test_file)
    poly.area()
    expected_area = 0.0
    assert abs(poly.total_area - expected_area) < 1e-6
    import os
    os.remove(test_file)

# Вертикальная плоскость не даст никакого вклада в площадь


def test_vertical_plane():
    test_file = "test_vertical_plane.geom"
    with open(test_file, 'w') as f:
        f.write("10.0	0.0	0.0	0.0\n")
        f.write("4 1 4\n")
        f.write("1.0 1.0 1.0\n")
        f.write("0.0 0.0 1.0\n")
        f.write("1.0 1.0 0.0\n")
        f.write("0.0 0.0 0.0\n")
        f.write("4 1 2 4 3\n")
    poly = Polyedr(test_file)
    poly.area()
    expected_area = 0.0
    assert abs(poly.total_area - expected_area) < 1e-6
    import os
    os.remove(test_file)
