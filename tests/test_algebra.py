from mathematics.algebra import add
import pytest

#TDD test drive development, BDD - behavioral drive development

# def test_true():
#     assert True

# class TestAdd:
#     def test_add_two_inits(self):
#         assert algebra.add(1, 3) == 4
#         assert algebra.add(-3, -3) == -6

@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (2, 3, 5),
        (-1, 4, 3),
        (-3, -3, -6),
    ],
)
def test_add(num1, num2, result):
    assert add(num1, num2) == result



@pytest.mark.parametrize(
    "num1,num2,num3,result1,result2",
    [
        (2, 3, 5, 4, 4),
        (-1, 4, 3, 5, 6),
        (-3, -3, -6, 6, ),
    ],
)
def test_roots(num1, num2, result):
    assert add(num1, num2) == result

