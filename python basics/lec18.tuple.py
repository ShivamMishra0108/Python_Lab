
#   Tuples are immutable : They cant be modified if once created.

tuple = (1)
tupl = (1,)
tup = (4,64,788,49)

print(type(tuple))
print(type(tupl))
print(type(tup))
print(tup[0])


print(tup[1])
print(tup[-2])

tup2 = tup[1:4]
print(tup2)

if 788 in tup:
    print("Yes")

