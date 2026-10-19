#3.Write a program to create a deep copy of a nested list of shopping cart items using copy.deepcopy().
import copy
shopping=[1,2,3,4,[5,6,7,8]]
b=copy.deepcopy(shopping)
print(shopping)
print(b)