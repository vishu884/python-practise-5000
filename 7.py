# Find the minimum number in a list without using min().
num=[10,20,30,40]
number=40
for nums in num :
    if nums < number :
        number=nums
print(number)
    