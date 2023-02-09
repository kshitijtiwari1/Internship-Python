# # # Bank program
# # balance = 1000
# # withdraw_amount = int(input("Enter the amount to withdraw: "))

# # if balance<500:
# #     print("Your account balance is ",balance, "Please keep your account balance above Rs.500 to avoid unwanted charges.")

# # if withdraw_amount>balance:
# #     print("Insufficient balance.")
    
# # print("Remaining balance is: ", balance-withdraw_amount)

# # greatest of 3 numbers
# # num1 = int(input("Enter a number: "))
# # num2 = int(input("Enter another number: "))
# # num3 = int(input("Enter another number: "))

# # if num1==num2==num3:
# #     print("All are equal")
    
# # elif num1>num2 and num1>num3:
# #     print("greatest number is:", num1)
    
# # elif num2>num1 and num2>num3:
# #     print("greatest number is:", num2)
    
# # else:
# #     print("greatest number is:", num3)
    
# # even or odd
# # n = input("Enter a number: ")
# # isInt = True

# # try:
# #     int(n)
# # except ValueError:
# #     isInt = False
    
# # if isInt:
# #     print('Input value is an integer')

# # else:
# #     print('Not an integer')
 
# # Grade marks   
# # score = float(input("Enter the score: "))
# # if score>=90:
# #     print("Grade A+")
    
# # elif score>=80 and score<90:
# #     print("Grade A")
    
# # elif score>=70 and score<80:
# #     print("Grade B+")
    
# # elif score>100:
# #     print("Invalid")
    
# # elif score>=60 and score<70:
# #     print("Grade B+")
    
# # elif score>=50 and score<60:
# #     print("Grade B+")

# # else:
# #     print("Failed")

# # Range input
# # n = int(input("Range:"))
# # for i in range(n):
# #     print(i,end='')
    
#  # table
# # num = int(input("Enter number: "))
# # stop_num = int(input("stop number: "))
# # for i in range(1, stop_num):
# #    print(num, 'x', i, '=', num*i)

# # factorial 
# # n = int(input("Enter a number: "))
# # factorial = 1

# # if n==0 or n==1:
# #     print("Factorial is 1")

# # elif n<0:
# #     print("Invalid")
    
# # else:
# #     for i in range(1, n+1):
# #         factorial=factorial*i
# #     print("Factorial of",n, "is",factorial)
    
# # factorial 2
# # n = int(input("Enter a number: "))
# # factorial = 1
# # i = 1

# # while i<=n:
# #     factorial=factorial*i
# #     i+=1
    
# # print("Factorial of",n, "is",factorial)

# # even number sum
# # start = int(input("Enter a start number: "))
# # stop = int(input("Enter a stop number: "))
# # total = 0
# # for i in range(start, stop+1):
# #     if i%2==0:
# #         total = total+i
# # print(total)

# # odd number sum
# # python code to print first n fibonacci numbers

# # fibonacci numbers
# def fibonacci_numbers(num):
# 	if num == 0:
# 		return 0
# 	elif num == 1:
# 		return 1
# 	else:
# 		return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)

# n = int(input("number: "))
# for i in range(0, n):
# 	print(fibonacci_numbers(i), end=" ")

# pattern
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
# def triangle(n):
	
# 	# number of spaces
# 	k = n - 1

# 	# outer loop to handle number of rows
# 	for i in range(0, n):
	
# 		# inner loop to handle number spaces
# 		# values changing acc. to requirement
# 		for j in range(0, k):
# 			print(end=" ")
	
# 		# decrementing k after each loop
# 		k = k - 1
	
# 		# inner loop to handle number of columns
# 		# values changing acc. to outer loop
# 		for j in range(0, i+1):
		
# 			# printing stars
# 			print("* ", end="")
	
# 		# ending line after each row
# 		print("\r")

# # Driver Code
# n = 5
# triangle(n)

# Function to demonstrate printing pattern of numbers
# def contnum(n):
# 	num = 0

# 	for i in range(0, n):
# 		for j in range(0, i+1):		
# 			print(num, end=" ")
# 			num = num + 1
# 		print("\r")

# n = 4
# contnum(n)