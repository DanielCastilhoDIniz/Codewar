"""
We need a function count_sel() that receives an array or list of integers (positive and negative) and may give us the following information in the order and structure presented bellow:

[(1), (2), (3), [[(4)], 5]]

(1) - Total amount of received integers.

(2) - Total amount of different values the array has.

(3) - Total amount of values that occur only once.

(4) and (5) both in a list

(4) - It is (or they are) the element(s) that has (or have) the maximum occurrence. If there are more than one, the elements should be sorted (by their value obviously)

(5) - Maximum occurrence of the integer(s)
"""


def count_sel(lst):
    result = []
    result.append(len(lst))
    result.append(len(set(lst)))
    result.append(len([x for x in lst if lst.count(x) == 1]))
    result.append(list(set([x for x in lst if lst.count(x) > 2])))


    return result


print(count_sel([-3, -2, -1, 3, 4, 4, 4, -5, -5, 5, -1, -5]))




lisa = [-3, -2, -1, 3, 4, -5, -5, 5, -1, -5]
