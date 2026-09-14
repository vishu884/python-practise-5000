#77.Find the largest number in a list without using max().
a=[10,20,30,40,50,60,70,80]
b=0
for n in a :
    if b<n :
      b=n
print(b)

