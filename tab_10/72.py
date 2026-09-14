# 72.Replace the middle elements using slicing assignment.
a=[10,20,30,40,50,60,70,80]
b=len(a)
c=b//2
a[0:c]=[100]
print(a)