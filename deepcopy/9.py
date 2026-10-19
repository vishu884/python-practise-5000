#9.Write a program to demonstrate that modifying a nested element in a deep copy of shopping cart items does NOT affect the original.
import copy
shopping=[10,20,30,40,[50,60,70,80]]
b=copy.deepcopy(shopping)
b[4][2]=200
print(shopping)
print(b)