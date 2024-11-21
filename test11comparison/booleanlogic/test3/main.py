def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    
    return "no charges yet"

test = check_mount_rental(4, 3)
print(test)

# this condition has no else, can be incoporated
