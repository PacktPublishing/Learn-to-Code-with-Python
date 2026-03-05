# def sum_of_positive_numbers(values):
#     total = 0

#     for value in values:
#         if value > 0:
#             total += value

#     return total

def sum_of_positive_numbers(values):
    total = 0

    for value in values:
        if value < 0:
            continue

        total += value

    return total

print(sum_of_positive_numbers([1, 2, -3, 4]))