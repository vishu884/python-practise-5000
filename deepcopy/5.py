#5.Write a program to create a deep copy of a nested list of temperature readings using copy.deepcopy().
import copy
temperature=[1,2,3,4,[5,6,7,8]]
b=copy.deepcopy(temperature)
print(temperature)
print(b)