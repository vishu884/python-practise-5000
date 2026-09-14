# 80.Count the total number of even numbers in a list.
a=[10,20,30,40,50,60,70,80]
count=0
for  n  in a :
    if n % 2 ==0:
        count+=1
print(count)