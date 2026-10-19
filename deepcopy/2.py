#2.Write a program to create a deep copy of a nested list of employee data using copy.deepcopy().
import copy
emp=[1,2,3,4,[5,6,7,8]]
b=copy.deepcopy(emp)
print(emp)
print(b)