# def count_positives_sum_negatives(arr):
#     aux = []
#     count_positives = 0
#     sum_negatives = 0
#     if arr != []:
#         for n in arr:

#             if n > 0:
#                 count_positives += 1
#             elif n < 0:
#                 sum_negatives += n
#         aux.append(count_positives)
#         aux.append(sum_negatives)

#     return aux

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


print(count_positives_sum_negatives(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([]))
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0]))
print(count_positives_sum_negatives(
    [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))


