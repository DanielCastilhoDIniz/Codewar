from random import randint

def getMaximumDistinctCount(a, b, k):
    swap_indices = []
    
    for _ in range(k):
        # Garantir que os elementos estejam dentro dos limites válidos
        index_a = randint(0, len(a) - 1)
        index_b = randint(0, len(b) - 1)
        swap_indices.append((index_a, index_b))
        
        a[index_a], b[index_b] = b[index_b], a[index_a]
        
    return len(set(a))

# Exemplo de uso
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
k = 2

resultado = getMaximumDistinctCount(a, b, k)
print(resultado)




