def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        factorial_num = 1
        for i in range(num, 0, -1):
            factorial_num = factorial_num * i
    
    return factorial_num

print(factorial(4))
