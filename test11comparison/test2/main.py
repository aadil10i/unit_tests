def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = (mustang_height == edward_height)
    is_alphonse_edward_same = (alphonse_height == edward_height)
    is_winry_alphonse_same = (winry_height == alphonse_height)

    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same




# def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
#     if (mustang_height == edward_height):
#         is_mustang_edward_same = True
#         if (alphonse_height == edward_height):
#             is_alphonse_edward_same = True
#             if (winry_height == alphonse_height):
#                 is_winry_alphonse_same = True
#         else: return False

#     return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

# results = compare_heights(5, 5, 7, 5)
# print(results)

