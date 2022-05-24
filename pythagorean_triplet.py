def triplets_with_sum(number):
    return [
        [a, b, c]
        for a in range(1, number // 3)
        if (
            a
            < (b := (number**2 - 2 * number * a) // (2 * number - 2 * a))
            < (c := number - a - b)
            and (a**2 + b**2 == c**2)
        )
    ]


# def triplets_with_sum(number):
#     m = np.arange(number)
#     n = np.arange(number)

#     a = np.subtract.outer(m**2, n**2)
#     b = 2 * np.multiply(m, n)
#     c = np.add.outer(m**2, n**2)

#     return np.where((a + b + c) == number)


# def triplets_with_sum(number):
#     """for this problem we have two conditions:
#     a + b + c = N      and      a**2 + b**2 = c**2
#     doing a little bit of math, we have that:
#     a = (N**2 - 2*b*N)/(2*(N - b))
#     b = (N**2 - 2*a*N)/(2*(N - a))"""
#     answer = []

#     for num in range(1, number // 3):
#         a = num
#         b = (number * number - 2 * number * a) // (2 * number - 2 * a)
#         c = number - a - b
#         if a < b < c and (a**2 + b**2 == c**2):
#             answer.append([a, b, c])
#     return answer


# def triplets_with_sum(number):
#     result = []
#     for a in range(1, number // 3):
#         for b in range(max(a + 1, number // 2 - a - 1), (number - a) // 2 + 1):
#             c = number - a - b
#             if a * a + b * b == c * c:
#                 result.append([a, b, c])
#     return result


# def triplets_with_sum(number):

#     triplets = []
#     for b in range(number):
#         for a in range(1, b):
#             c = math.sqrt(a**2 + b**2)
#             if a + b + c == number:
#                 triplets.append([a, b, c])
#     return triplets
