#81.Count the total number of odd numbers in a list.
a=[1,2,3,4,5,6,7,8]
count=0
for n in a :
    if n%2!=0 :
      count+=1
print(count)