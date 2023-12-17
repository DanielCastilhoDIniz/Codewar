def even_or_odd(number):
    if number % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    return result


print(even_or_odd(0))


a = 10 % 2

print(a)


def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0:
        result1 = 'Even'
    else:
        result1 = 'Odd'
        
    if flower2 % 2 == 0:
        result2 = 'Even'
    else:
        result2 = 'Odd'
        
    if result1 != result2:
        love = True
    if result1 == result2:
        love = False
    return love


def lovefunc2( flower1, flower2 ):
    return bool((flower1+flower2)%2)

print(lovefunc2(7,8))

print(abs(-3))