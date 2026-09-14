#83.Write a program to sort a list of shopping cart items tuples by a specific key using the key parameter.
a=[("shoes",1),("cloth",2),("watch",3),("glasses",4)]
a.sort(key=len)
print(a)