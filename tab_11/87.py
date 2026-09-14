#87.Write a program to sort a list of cricket scores tuples by a specific key using the key parameter.
a=[("100",1),("200",3),("300",2),("400",4)]
a.sort(key=lambda x:x[1])
print(a)