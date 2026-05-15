# List: Can contains elements of different datatypes.

# marks = [4,5,6, "Shivam", True]

# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3])
# print(marks[5-3])
# print(marks[len(marks)-3])
# print(marks[2])

# if "Shivam" in marks:
#     print("Yes")
# else:
#     print("No")

list = [2,4,5,78,54,33,66,54,]

print(list)
print(type(list))
list.append(7)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

# print(list.index(1))
# print(list.index(0))

m = [999, 1000, 1100]
list.extend(m)
print(list)