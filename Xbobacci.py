"""
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]
"""

# 1°solução


def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    else:
        for n in range(1, n-2, 1):
            soma = +(signature[n-1] + signature[n] + signature[n+1])
            signature.append(soma)
        return signature


print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 10))
print(tribonacci([1, 1, 1], 10))
print(tribonacci([3, 2, 1], 10))
print(tribonacci([1, 1, 1], 0))
print(tribonacci([1, 1, 1], 1))

a = [0, 0, 1]

print(a[-3:])


# solução ótima


def tribonacci2(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


print(tribonacci2([0, 0, 1], 10))
print(tribonacci2([0, 1, 1], 10))
print(tribonacci2([1, 1, 1], 10))
print(tribonacci2([3, 2, 1], 10))
print(tribonacci2([1, 1, 1], 0))
print(tribonacci2([1, 1, 1], 1))
