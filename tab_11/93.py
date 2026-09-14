#93.Write a program to sort a list of stock prices tuples by a specific key using the key parameter.
a=[("1000",1),("2000",3),("3000",2),("4000",4)]
a.sort(key=lambda x:x[1])
print(a)