#96.Write a program to sort a list of restaurant orders tuples by a specific key using the key parameter.
a=[("tea",1),("coffie",3),("pasata",2)("meggie",4)]
a.sort(key=lambda x:x[1])
print(a)