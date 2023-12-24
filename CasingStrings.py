"""
aden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""
import timeit
t1 = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(string):
    inicio = timeit.default_timer()
    frase=''
    for word in string.split():
        frase = frase + " " + word.capitalize()
    
    fim = timeit.default_timer()
    tempo_execucao = fim - inicio
    return frase.strip(), tempo_execucao

print(to_jaden_case(t1))

#pythonic
def to_jaden_case2(string):
    inicio = timeit.default_timer()
    fim = timeit.default_timer()
    tempo_execucao = fim - inicio
    return ' '.join(word.capitalize() for word in string.split()), tempo_execucao


print(to_jaden_case2(t1))