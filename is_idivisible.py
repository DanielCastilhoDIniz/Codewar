def is_divisible(*args):
    for num in args:
       if args[0] % num != 0:
           return False     
    return True
    
print(is_divisible(48,3,4,2,5))

# pythonic 
# def is_divisible(n, *args):
#     return all(not n % i for i in args)