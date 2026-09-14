#99.Write a program to sort a list of user ages tuples by a specific key using the key parameter.
a=[("10",1),("20",3),("30",2),("30",4)]
a.sort(key=lambda x:x[1])
print(a)