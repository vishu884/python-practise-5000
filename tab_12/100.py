#100.Write a program to unpack nested lists of delivery addresses into separate variables.
address=[
    ["gopalapur"],
    ["jaunpur"],
    ["varanasi"]
]
*a,b=address
print(a)
print(b)