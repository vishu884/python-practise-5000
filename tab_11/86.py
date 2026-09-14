#86.Write a program to sort a list of movie ratings tuples by a specific key using the key parameter.
a=[("asique2",1),("chand mera dil",3),("pushpa2",2),("kgf2",4)]
a.sort(key=lambda x:x[1])
print(a)