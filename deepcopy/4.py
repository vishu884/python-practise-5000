#4.Write a program to create a deep copy of a nested list of bank transactions using copy.deepcopy().
import copy
bank=[1,2,3,4,[5,6,7,8]]
b=copy.deepcopy(bank)
print(bank)
print(b)