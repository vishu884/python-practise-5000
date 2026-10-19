#6.Write a program to create a deep copy of a nested list of movie ratings using copy.deepcopy().
import copy
movie=[1,2,3,4,[5,6,7,8]]
b=copy.deepcopy(movie)
print(movie)
print(b)