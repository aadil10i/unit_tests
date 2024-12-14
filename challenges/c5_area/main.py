def area_sum(rectangles):
    total_area = 0
    for rectangle in rectangles:
        height = rectangle['height']
        width = rectangle['width']
        
        total_area += height * width 
    return total_area
