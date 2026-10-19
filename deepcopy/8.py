#8.Write a program to demonstrate that modifying a nested element in a deep copy of employee data does NOT affect the original.
import copy
employe=[10,20,30,40,[50,60,70,80]]
b=copy.deepcopy(employe)
b[4][2]=500
print(employe)
print(b)
