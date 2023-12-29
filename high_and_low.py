# def high_and_low(numbers):

#     aux = [int(x) for x in numbers.split()]
#     high = aux[0]
#     low = aux[0]
#     for i in aux:
#         if i > high:
#             high = i
#         if i < low:
#             low = i
#     return f"{high} {low}"
""" maior e menor inteiro de uma lista"""
def high_and_low(numbers):

    aux = [int(x) for x in numbers.split()]
    return f"{max(aux)} {min(aux)}"


print(high_and_low("-8 -3 -5 -42 -1  -9 -4 -7 -4 -42"))
