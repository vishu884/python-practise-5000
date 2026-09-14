# 78.Find the smallest number in a list without using min().
a=[10,20,30,40,50,60,70,80]
b=80
for n in a :
     if b > n :
        b=n
print(b)