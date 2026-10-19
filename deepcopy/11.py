#11.Write a program to demonstrate that modifying a nested element in a deep copy of temperature readings does NOT affect the original.
import copy
temperature=[10,20,30,40,[50,60,70,80]]
b=copy.deepcopy(temperature)
b[4][2]=200
print(temperature)
print(b)