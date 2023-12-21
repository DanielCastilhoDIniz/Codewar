def solution(pairs):
    aux = ''
    for i in pairs.items():
         aux = aux + (f' {i[0]} = {i[1]},')
    return aux


pairs = {'a': 1, 'b': 2}

#solução pythonica
def solution(pairs):
    return ','.join(f'{k} = {v}' for k,v in pairs.items())


print(solution(pairs={'a': 1, 'b': 2}))