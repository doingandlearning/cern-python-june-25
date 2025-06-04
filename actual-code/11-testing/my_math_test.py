from my_math import add
import pytest

def test_adding_two_positive_numbers_correctly():
    # Arrange   - Given
    a = 10
    b = 4
    expected_result = 14

    # Act       - When
    actual_result = add(a, b)

    # Assert    - Then
    assert actual_result == expected_result

def test_adding_two_positive_numbers_correctly_two():
    assert add(10, 4) == 14


@pytest.mark.parametrize('input1,input2,expected', [
    (-1, 1, 0),
    (100, 1000, 1100),
    (0.1, 0.1, 0.2)
])
def test_adding_pairs_correctly_two(input1, input2, expected):
    assert add(input1, input2) == expected


def test_that_adding_lists_fails():
    with pytest.raises(TypeError):
        add([], [])


def test_that_adding_number_and_list_fails():
    with pytest.raises(TypeError):
        add(3, [])


def test_that_adding_list_and_number_fails():
    with pytest.raises(TypeError):
        add([], 5.5)









