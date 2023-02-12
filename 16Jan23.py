# merge dictionary
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}

# merged_dict = dict1 | dict2 | dict3
# print(merged_dict)

# product of unique numbers
# def unique_product(list_data):
#     temp = list(set(list_data))
#     p = 1
#     for i in temp:
#         p *= i
#     return p
# nums = [10, 20, 30, 40, 20, 50, 60, 40]
# print("Original List : ",nums)
# print("Product of the unique numbers of the said list: ",unique_product(nums))

# list
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1.reverse()

# print(list1)

# max value key
# dict1 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# print(max(dict1, key = dict1.get))

#  read input
data = [
    {
        "name": "John",
        "age": 30,
    },
    {
        "name": "David",
        "age": 28,
    },
    {
        "name": "Miller",
        "age": 29,
    },
    {
        "name": "David Miller",
        "age": 32,
    },
    {
        "name": "John Doe",
        "age": 30,
    },
]

x = input("Enter a name:")

for i in data:
    for value in i.values():
       if x == i.values()
       print(x)