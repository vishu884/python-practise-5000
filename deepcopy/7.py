#7.Write a program to demonstrate that modifying a nested element in a deep copy of student records does NOT affect the original.
import copy
student=[10,20,30,40,[50,60,70,80]]
b=copy.deepcopy(student)
b[2]=100
print(student)
print(b)