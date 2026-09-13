import itertools as it

digits = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

# def roman_to_int(roman: str) -> int:
#     buffer = list(roman)
#     values = [0]
#
#     while buffer:
#         value = digits[buffer.pop()]
#
#         if value < values[-1]:
#             value *= -1
#
#         values.append(value)
#
#     return sum(values)

# def roman_to_int(roman: str) -> int:
#     values = [digits[x] for x in roman]
#     paired = zip(values, values[1:] + [0] )
#
#     return sum(-a if a < b else a for a, b in paired)

def roman_to_int(roman: str) -> int:
    a_value, b_value  = it.tee(
        map(
            lambda x: digits[x],
            list(roman)
        )
    )

    paired = zip(a_value,
                 it.chain(
                     it.islice(
                         b_value,
                         1,
                         None
                     ),
                     [0])
                 )

    return sum(-a if a < b else a for a, b in paired)
