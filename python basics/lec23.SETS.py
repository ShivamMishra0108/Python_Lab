   # SET:

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1.union(s2))
print(s1, s2)
print(type(s1))

c1 = {"JBP", "katni", "dindori", "nagpur", "sagar"}
c2 = {"katni", "sagar", "JBP", "rewa" }
c3 = {"dindori", "nagpur", "sagar"}

cities = c1.difference(c2)
print(cities)

city = c1.intersection(c2)
print(city)

print(c1.issuperset(c3))
print(c3.issubset(c1))