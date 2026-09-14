#84.Write a program to sort a list of bank transactions tuples by a specific key using the key parameter.
a=[("5000",1),("6000",3),("7000",2),("8000",4)]
a.sort(key=lambda x:x[1])
print(a)