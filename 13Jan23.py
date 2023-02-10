#  text file open and write
# file = open("intro.txt",'w')
# file.write(input("Enter a line to write:"))
# file.close()

# # different input lines
# file = open('MyFile.txt','w')
# newline = '\n'
# file.write(input("Enter 1st line: "))
# file.write(newline)
# file.write(input("Enter 2nd line: "))
# file.write(newline)
# file.write(input("Enter 3rd line: "))
# file.close()

# # merge files
# f1 = open("intro.txt","r")
# data1 = f1.read()
# f2 = open("MyFile.txt","r")
# data2 = f2.read()
# f3 = open("merge.txt","w")
# f3.write(data1)
# f3.write(data2)

# append file
# f = open('intro.txt','a')
# f.write(input("Enter text: "))

# read content in reverse
# for i in reversed(list(open("intro.txt","r"))):
#         print(i.rstrip())