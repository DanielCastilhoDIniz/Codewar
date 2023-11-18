def digitize(n):

    a = [int(x) for x in reversed(str(n))]
    
    return a

print((digitize(123456789)))