# 26.Take an index and value from the user and insert the value at that index.
a=[10,20,30,40,50]
indx=int(input("enter the index:"))
val=int(input("enter the value"))
a.insert(indx,val)
print(a)