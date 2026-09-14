#89.Write a program to sort a list of electricity bills tuples by a specific key using the key parameter.
a=[("1000",1),("3000",3),("2000",2),("4000",4)]
a.sort(key=lambda x:x[1])
print(a)