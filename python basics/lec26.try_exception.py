# a = input("Enter the number:")

# print(f"The table of the {a} is:")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}" )

# except:
#     print("Entered Invalid Input")


# print("Some lines of code")
# print("End of the code")

try:
    num  = int(input("Enter an integer:"))
    a = [6,3]
    print(a[num])

except ValueError:
    print("Number entered is not en integer")

except IndexError:
    print("Index Error")