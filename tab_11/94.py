#94.Write a program to sort a list of product inventory tuples by a specific key using the key parameter.
a=[("watch",1),("gogle",3),("cloth",2),("shoes",4)]
a.sort(key=lambda x:x[1])
print(a)