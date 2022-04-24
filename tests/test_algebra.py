from algebra import add
import pytest


@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (2, 3, 5),
        (-1, 4, 3),
        (-3,-3,-6),
    ],
)
def test_add(num1, num2, result):
    assert add(num1, num2) == result
