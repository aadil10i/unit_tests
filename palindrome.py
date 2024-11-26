def checkPalin(num):
    new_num = str(num).split("")
    new_rev = new_num[::1]
    if new_num == new_rev:
        return True
    else:
        return False

my_num = 121
checked_palin = checkPalin(my_num)
print(checked_palin)