#95.Write a program to sort a list of traffic signals tuples by a specific key using the key parameter.
a=[("red",1),("green",3),("yellow",2)]
a.sort(key=lambda x:x[1])
print(a)