# # vowel
# def countVowel(str):
#     total = 0
#     vowel = set("aeiouAEIOU")
    
#     for i in str:
#         if i in vowel:
#             total += 1
#     print("Total no of vowels:",total)            
            
# str = input("Enter a string: ")
# countVowel(str)

# no of times a word appears
# def countOccurrences(str, word):
     
#     a = str.split(" ")
#     count = 0
#     for i in range(0, len(a)):
         
#         if (word == a[i]):
#            count = count + 1
            
#     return count      

# str = input("Enter a string: ")
# word = input("Enter a string to find: ")
# print(countOccurrences(str, word))

# # stirng uppercase
# list1 = list(input("Enter a list: "))
# print([x.upper() for x in list1])

# # nof lines
# with open(r"myfile.txt", 'r') as fp:
# 	lines = len(fp.readlines())
# 	print('Total Number of lines:', lines)
