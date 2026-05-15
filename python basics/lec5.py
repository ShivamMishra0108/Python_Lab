

# USER INPUT: python always takes input as a String

a = input("Enter your name")
print("My name is", a)

p = input("ENTER FIRST NUMBER: ")
q = input("ENTER SECOND NUMBER: ")

print("The sum is: ", p+q)

print("The sum is: ", int(p) + int(q))


# String: In python String is  like an array of characters

name = "Shivam"

Letter = '''Hello there!
                    How are you I am Shivam as you know i am learning 
                    python with you 
                    thankyou 
                    Yours friend'''

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print("Using for loop\n")

for character in name:
    print(character)


print("\n using for loop for letter\n")

for character in Letter:
    print(character)