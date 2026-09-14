#85.Write a program to sort a list of bank transactions tuples by a specific key using the key parameter.
a=[("10"),("30"),("20"),("40")]
a.sort(key=len)
print(a)