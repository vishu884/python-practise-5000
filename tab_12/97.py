#97.Write a program to unpack nested lists of game scores into separate variables.
score=[
    [100],
    [200],
    [300]
]
a,*b=score
print(a)
print(b)