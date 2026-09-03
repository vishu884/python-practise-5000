# Count the frequency of a particular number in a list.
num=[10,20,10,30,40]
num1=int(input("enter the number"))
count=0
for nums in num :
    if nums==num1 :
        count+=1
print(count)