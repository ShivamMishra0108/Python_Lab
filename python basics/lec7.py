# String methods in python

# Strings are immutable

# What we learn: uppercase, lowercase, rstrip, replace, split, count, capitalize, center, endswith, find, alnum, alpha,
#  islower, isupper, isprintable, isspace, istitle, swapcase, title

a = "!!!Shivam!!! !!!!! Shivam"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Shivam", "Vedu"))
print(a.split())

blog = "learning the pYTHon"

print(blog.capitalize())

str = "WELCOME TO PYTHON"

print(str.center(50))
print(len(str))
print(len(str.center(50)))
print(blog.count("n"))
print(blog.endswith("n"))
print(str.find("TO"))

str1 = "WelcomeToConsole100"
str2 = "HELLO!  #WELCOME @shivam"

print(str1.isalnum())
print(str2.isalnum())

print(str1.isalpha())
print(str2.isalpha())

s1 = "WELCOME"
s2 = "welcome"
s3 = "Hello Welcome \n"
s4 = "          "

print(s1.islower())
print(s2.islower())

print(s1.isupper())
print(s2.isupper())

print(s1.isprintable())
print(s3.isprintable())

print(s4.isspace())
print(s3.isspace())

print(s2.istitle())
print(s3.istitle())

print(s3.swapcase())

text = "his name is dan and he is an honest man"

print(text.title())