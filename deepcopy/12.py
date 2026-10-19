#12.Write a program to demonstrate that modifying a nested element in a deep copy of movie ratings does NOT affect the original.
import copy
movie=[10,20,30,40,[50,60,70,80]]
b=copy.deepcopy(movie)
b[4][2]=200
print(movie)
print(b)