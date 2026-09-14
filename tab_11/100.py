#100.Write a program to sort a list of delivery addresses tuples by a specific key using the key parameter.
a=[("mariyahu",1),("gopalapur",3),("jaunpur",2),("varanasi",4)]
a.sort(key=lambda x:x[1])
print(a)