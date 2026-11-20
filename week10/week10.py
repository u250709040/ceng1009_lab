# myList = [76, 92 , 3 , "hello", True , 4, 76]
#
# print(myList)
# myList.append('apple')
# myList.append(76)
# print(myList)
#
# myList.insert(3, "cat")
# print(myList)
#
# myList.insert(0,99)
# print(myList)
#
# print(myList.index("hello"))
#
# print(myList.count(76))
#
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)
#
# myList.pop(3)
# print(myList)

# def sum_of_squares(numbers):
#     sum = 0
#     for number in numbers:
#         sum += number ** 2
#     return sum
#
#
#
# my_list = [1, 2, 3, 4, 5]
# print(sum_of_squares(my_list))
#
# def sum_evens(num_list):
#     sum = 0
#     for num in num_list:
#         if num % 2 == 0:
#             sum += num
#     return sum
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_evens(my_list))


# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# print (count_five_letter(["hello", "world", "ali", "play"]))

# def sum_until_even(num_list):
#     total = 0
#     for num in num_list:
#         if num % 2 == 0:
#             break
#         total += num
#     return total
#
# print(sum_until_even([1,3,3,7,5,5,6,7]))

# def sum_until_even(num_list):
#     total = 0
#     for num in num_list:
#         if num == "sam":
#             break
#         total += num
#     return total
#
# print(sum_until_even([1,3,3,7,5, "sam" ,5,6,7]))

# def replace(s, old, new):
#     pieces = s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("passed")
#     else:
#         print("failed")
#
# test(replace("Mississippi", "i", "I"), "MIssIssIppI")

# def find_max_val_in(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(find_max_val_in(num_list))


# def find_max_val_in(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# my_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# print(find_max_val_in(my_list))