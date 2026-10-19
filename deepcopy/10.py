#10.Write a program to demonstrate that modifying a nested element in a deep copy of bank transactions does NOT affect the original.
import copy
bank=[10,20,30,40,[50,60,70,80]]
b=copy.deepcopy(bank)
b[4][2]=100
print(bank)
print(b)