# class TotalSalary:
#     def __init__(self, salary):
#         self.total_salary = salary
        
#     def __add__(self, x):
#         print("Total Salary is:", x)
#         return TotalSalary(self.total_salary + x.salary)
        

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name        
#         self.salary = salary    
        
#         def __add__(self, x):
#             print(x)
#             return TotalSalary(self.salary + x.salary)    

# d1 = Employee("John", 1000)
# d2 = Employee("kshitij", 1000)
# d3 = Employee("harsh", 1000)
# d4 = Employee("Jhim", 1000)
# d5 = Employee("ram", 1000)
# d6 = Employee("sham", 4000)

# salary = d1 + d2 + d3 + d4 + d5 + d6
# print(salary.total_salary)