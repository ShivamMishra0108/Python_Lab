
# WE dont need break; statement in python

x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("the x i zero")

    case 4:
        print("x is four")
    
    case _ if x!=90:
        print(x, "x is not 90")

    case _ if x!=80:
        print(x, "x is not 80")

    case _:
        print(x)
        


