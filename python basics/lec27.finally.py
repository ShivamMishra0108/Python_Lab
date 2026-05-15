def funx1():
    try:
     l = [4,3,7,8,5,6]
     i = int(input("Enter the index:"))
     print(l[i])
     return 1
    
    except:
     print("Some error occured")
     return 0

    finally:
     print("I am always executed")

x = funx1()
print(x)
