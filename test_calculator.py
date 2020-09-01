from math import factorial, sin
from calculator import add, fact, sinius, divide, exalted, multiply
import pytest

#Exercise 1
def test_add():
    x = 1
    y = 2
    assert add(x, y) == (x+y)

#Exercise 2
def test_add_float():
    x = 0.1
    y = 0.2
    assert abs((x+y) - add(x, y)) < 1e-9

#Exercise 3
def test_add_string():
    x = "Hello "
    y = "World"
    assert add(x, y) == (x+y)

#Exercise 4
def test_fact():
    n = 4
    assert fact(n) == factorial(n)

def test_sinius():
    N = 10
    x = 3
    assert abs(sinius(x, N) - sin(x)) < 1e-9

def test_divide():
    x = 1
    y = 2
    assert divide(x, y) == 0.5

def test_exalted():
    x = 2
    n = 4
    assert exalted(x, n) == 16

def test_multiply():
    x = 1
    y = 2
    assert multiply(x, y) == 2

#Exercise 5
def test_add_raises_TypeError():
    with pytest.raises(TypeError):
        add(2, "Hello")

def test_divide_raises_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)

#Exercise 6

#parametrized test for add
@pytest.mark.parametrize(
    "arg, expected_output", [[(1, 2), 3], [(4, 2), 6], [(-2, 2), 0]])
def test_add_multiply(arg, expected_output):
    assert add(arg[0], arg[1]) == expected_output

#parametrized test for add_float
@pytest.mark.parametrize(
    "arg, expected_output", [[(0.1, 0.2), 0.3], [(0.4, 0.2), 0.6], [(-0.2, 0.2), 0]])
def test_add_float_multiply(arg, expected_output):
    assert abs(add(arg[0], arg[1]) - expected_output) < 1e-9

#parametrized test for add_string
@pytest.mark.parametrize(
    "arg, expected_output", [[("Hello ", "World"), "Hello World"], [("World ", "Hello"), "World Hello"], [("He ", "Wo"), "He Wo"]])
def test_add_string_multiply(arg, expected_output):
    assert add(arg[0], arg[1]) == expected_output

#parametrized test for factorial
@pytest.mark.parametrize(
    "arg, expected_output", [[4, factorial(4)], [2, factorial(2)], [5, factorial(5)]])
def test_fact_multiply(arg, expected_output):
    assert fact(arg) == expected_output

#parametrized test for sin
@pytest.mark.parametrize(
    "arg, expected_output", [[(3, 10), sin(3)], [(2, 10), sin(2)], [(4, 20), sin(4)]])
def test_sinius_multiply(arg, expected_output):
    assert abs(sinius(arg[0], arg[1]) - expected_output) < 1e-9

#parametrized test for divide
@pytest.mark.parametrize(
    "arg, expected_output", [[(1, 2), 0.5], [(4, 2), 2], [(-2, 2), -1]])
def test_divide_multiply(arg, expected_output):
    assert divide(arg[0], arg[1]) == expected_output

#parametrized test for exalted
@pytest.mark.parametrize(
    "arg, expected_output", [[(2, 4), 16], [(4, 3), 64], [(-2, 2), 4]])
def test_exalted_multiply(arg, expected_output):
    assert exalted(arg[0], arg[1]) == expected_output

#parametrized test for multiply
@pytest.mark.parametrize(
    "arg, expected_output", [[(1, 2), 2], [(4, 3), 12], [(-2, 2), -4]])
def test_multiply_multiply(arg, expected_output):
    assert multiply(arg[0], arg[1]) == expected_output
