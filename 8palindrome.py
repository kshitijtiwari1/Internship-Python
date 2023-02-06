x = str(input("Enter a number:"))
w = ""
for i in x:
	w = i + w

if x == w:
	print("Yes")
else:
	print("No")