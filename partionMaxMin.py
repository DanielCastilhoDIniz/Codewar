"""

Given a certain integer n, n > 0and a number of partitions, k, k > 0; we want to know the partition which has the maximum or minimum product of its terms.

The function find_spec_partition() , will receive three arguments, n, k, and a command: 'max' or 'min'

The function should output the partition that has maximum or minimum value product (it depends on the given command) as an array with its terms in decreasing order.

Let's see some cases (Python and Ruby)

find_spec_partition(10, 4, 'max') == [3, 3, 2, 2]
find_spec_partition(10, 4, 'min') == [7, 1, 1, 1]
and Javascript:

findSpecPartition(10, 4, 'max') == [3, 3, 2, 2]
findSpecPartition(10, 4, 'min') == [7, 1, 1, 1]
The partitions of 10 with 4 terms with their products are:

(4, 3, 2, 1): 24
(4, 2, 2, 2): 32
(6, 2, 1, 1): 12
(3, 3, 3, 1): 27
(4, 4, 1, 1): 16
(5, 2, 2, 1): 20 
(7, 1, 1, 1): 7   <------- min. productvalue
(3, 3, 2, 2): 36  <------- max.product value
(5, 3, 1, 1): 15
Enjoy it!
"""
from itertools import combinations_with_replacement
from math import prod
import timeit


def find_spec_partition(n, k, com):
    compare_func = max if com == 'max' else min
    # inicio = timeit.default_timer()
    combinations = (comb for comb in combinations_with_replacement(
        range(1, n), k) if sum(comb) == n)
    parts = {combination: prod(combination) for combination in combinations}  

    # fim = timeit.default_timer()
    # tempo_execucao = fim - inicio
    result =list( compare_func(parts))
    return  result[::-1]
    
  
    

# a =  [4,2, 2, 3, 3]
# print((a[:-1]))

# print(find_spec_partition(10, 4, 'max'))


# # Exemplos de uso
# print(find_spec_partition(10, 4, 'max'))  # Saída esperada: [3, 3, 2, 2]
# print(find_spec_partition(10, 4, 'min'))  # Saída esperada: [7, 1, 1, 1]
# from itertools import combinations
# from collections import Counter


# def find_spec_partition(n, k, com):
#     """
#     Finds the partition of n into k terms with the maximum or minimum product.

#     Args:
#         n: The integer to partition.
#         k: The number of terms in the partition.
#         com: A string indicating whether to find the maximum ('max') or minimum ('min') product.

#     Returns:
#         A list of integers representing the partition with the desired product, in decreasing order.
#     """

#     compara_funcao = max if com == 'max' else min

#     # Efficiently generate combinations without repetitions
#     combination = combinations(range(1, n + 1), k)

#     # Filter combinations that sum to n and calculate their products
#     products = [Counter(combination).values() for combination in combinations if sum(combination) == n]

#     # Find the combination with the desired product
#     result = compara_funcao(products)[0]

#     # Sort the result in decreasing order
#     return sorted(result, reverse=True)

print(find_spec_partition(10, 4, 'max'))
print(find_spec_partition(10, 4, 'min'))


# Pythonico
def find_spec_partition(n, k, com):
    x,r = divmod(n,k)
    return {'max': [x+1]*r + [x]*(k-r),
            'min': [n+1-k] + [1]*(k-1)}[com]

# Exemplo de uso
print(find_spec_partition(10, 4, 'max'))  # Saída esperada: [3, 3, 2, 2]
print(find_spec_partition(10, 4, 'min'))  # Saída esperada: [7, 1, 1, 1]