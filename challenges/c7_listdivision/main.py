def divide_list(nums, divisor):
    new_list = []
    for num in nums:
        new_num = num / divisor
        new_list.append(new_num) 
    
    return new_list

print(divide_list([1, 2, 3], 5))
