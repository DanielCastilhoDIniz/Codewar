import re


def reverse_words(text):
      
    
    palavras = re.split(r'(\s+)', text)
    palavras_invertidas = [''.join(reversed(palavra)) if not re.match(r'\s+', palavra) else palavra for palavra in palavras]
    resultado = ''.join(palavras_invertidas)

    return resultado

    # revertida = [''.join(reversed(palavra)) if not re.match(
    #     r'\s+', palavra) else palavra for palavra in re.split(r'\s+', text)]
    # return ''.join(revertida)


print(reverse_words('The quick brown fox jumps   over the lazy dog.'))

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

print(reverse_words('The quick brown fox jumps   over the lazy dog.'))





