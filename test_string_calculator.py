from string_calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


# Next steps to add, one at a time, each driven by a failing test first:
#
# def test_single_number_returns_that_number():
#     assert add("1") == 1
#
# def test_two_numbers_returns_sum():
#     assert add("1,2") == 3
#
# def test_unknown_amount_of_numbers():
#     assert add("1,2,3,4,5") == 15
#
# def test_negative_number_raises_exception():
#     import pytest
#     with pytest.raises(ValueError):
#         add("1,-2,3")
#
# def test_negative_number_message_includes_the_number():
#     import pytest
#     with pytest.raises(ValueError, match="-2"):
#         add("1,-2,3")
#
# def test_all_negative_numbers_are_listed_in_the_exception():
#     import pytest
#     with pytest.raises(ValueError, match="-2,-3"):
#         add("1,-2,-3")
