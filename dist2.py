from random import randint
n = 5
a =[2,3,3,2,2]
b =[1,3,2,4,1]
k = 2

# swap_indices = []
# for _ in range(k):
#    swap_indices.append(randint(0, n))
# a[swap_indices[0]] = b[swap_indices[1]]
# b[swap_indices[1]] = a[swap_indices[0]]

# print(set(a))
# for element in a:
#     if element not in a:
#         an

# print(a,b)
# print(swap_indices)
# # print(an)
# print(len(set(a)))    
# print((set(a)))    

from random import randint
def getMaximumDistinctCount(a, b, k):
    swap_indices = []
    for _ in range(k):
        swap_indices.append(randint(0, len(a))-1)
    a[swap_indices[0]] = b[swap_indices[1]]
    b[swap_indices[1]] = a[swap_indices[0]]
    return len(set(a)), a, swap_indices


print(getMaximumDistinctCount([2,3,3,2,2],[1,3,2,4,1],2))
