# #  program to print even numbers in a list 
# def evennumbers(list, n=0):
# 	# base case
# 	if n == len(list):
# 		exit()
# 	if list[n] % 2 == 0:
# 		print(list[n], end=" ")
# 	# calling function recursively
# 	evennumbers(list, n+1)

# list1 = [10, 21, 4, 45, 66, 93]
# print("Even numbers in the list:", end=" ")
# evennumbers(list1)

#  largest function
# def largestItem(list1):
#     length = len(list1)
#     num = 0
#     for i in range(length):
#         if(i == 0 or list1[i] > num):
#             num = list1[i]
#         return num

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# new list
# def new_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(new_list([1,2,3,3,3,3,4,5]))

# multiply numbers in list
# def multiply_numbers(num):  
#     total = 1
#     for x in num:
#         total *= x  
#     return total  
# print(multiply_numbers((45, 12, 83, 71, -53)))