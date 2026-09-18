from caesar_cipher import encode, decode


def test_encode_single_letter_no_wrap():
    assert encode("a", 1) == "b"


# Next steps to add, one at a time, each driven by a failing test first:
#
# def test_encode_single_letter_with_wraparound():
#     assert encode("z", 1) == "a"
#
# def test_encode_word():
#     assert encode("abc", 1) == "bcd"
#
# def test_encode_preserves_case():
#     assert encode("ABC", 1) == "BCD"
#
# def test_encode_leaves_non_letters_untouched():
#     assert encode("a b, c!", 1) == "b c, d!"
#
# def test_encode_with_shift_larger_than_alphabet_wraps_correctly():
#     assert encode("a", 27) == "b"  # 27 % 26 == 1
#
# def test_encode_with_negative_shift():
#     assert encode("b", -1) == "a"
#
# def test_decode_single_letter():
#     assert decode("b", 1) == "a"
#
# def test_decode_undoes_encode_for_a_sentence():
#     original = "Attack at Dawn!"
#     assert decode(encode(original, 5), 5) == original
