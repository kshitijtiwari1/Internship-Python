# #1.Write a Python program to remove duplicates from a list​

# # mylist = ["sadf", "b", "sadf", "c", "c"]
# # mylist = list(dict.fromkeys(mylist))
# # print(mylist) 

# # Python3 code to demonstrate working of
# # Swap tuple elements in list of tuples

# # initializing list
# test_list = [(3, 4), (6, 5), (7, 8)]

# # printing original list
# print("The original list is : " + str(test_list))

# # Swap tuple elements in list of tuples
# # Using list comprehension
# res = [(sub[1], sub[0]) for sub in test_list]
		
# # printing result
# print("The swapped tuple list is : " + str(res))

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(1))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)

# num = [7,8, 120, 25, 44, 20, 27]
# num = [x for x in num if x%2!=0]
# print(num)

# def match_words(words):
#   ctr = 0

#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       ctr += 1
#   return ctr

# print(match_words(['abc', 'xyz', 'aba', '1221']))

#Write a Python program to convert list to list of dictionaries.​
#Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]​

# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])