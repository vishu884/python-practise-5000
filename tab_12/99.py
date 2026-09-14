#99.Write a program to unpack nested lists of user ages into separate variables.
age=[
    [10],
    [20],
    [30],
    [40]
]
a,*b=age
print(a)
print(b)