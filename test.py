# def find_spec_partition(n, k, com):
#     x,r = divmod(n,k)
#     return {'max': [x+1]*r + [x]*(k-r),
#             'min': [n+1-k] + [1]*(k-1)}[com]

# # Exemplo de uso
# print(find_spec_partition(10, 4, 'max'))  # Saída esperada: [3, 3, 2, 2]
# print(find_spec_partition(10, 4, 'min'))  # Saída esperada: [7, 1, 1, 1]

print(divmod(10,4))
print([3]*2 + [2]*2)