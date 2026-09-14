#90.Write a program to sort a list of library books tuples by a specific key using the key parameter.
a=[("english",1),("hindi",3),("math",2),("science",4)]
a.sort(key=lambda x:x[1])
print(a)