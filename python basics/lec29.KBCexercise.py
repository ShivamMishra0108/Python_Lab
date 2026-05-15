questions = [["which language was used to build fb","french","python","java","none",3],
["which language was used to build fb","french","python","java","none",3],
["which language was used to build fb","french","python","java","none",3],
["which language was used to build fb","french","python","java","none",3],
["which language was used to build fb","french","python","java","none",3]]

levels = [1000,2000,5000,10000,20000,50000,]
money  = 0

for i in range(0,len(questions)):

    print("Question for Rs.",levels[i])
    print(questions[i][0])
    print(f"a.{questions[i][1]}       b.{questions[i][2]}")
    print(f"c.{questions[i][3]}       d.{questions[i][4]}")

    reply = int(input(f"Enter your answer (1-4):"))
    if(reply == questions[i][5]):
        print(f"Correct Answer! Congrats You Won Rs.{levels[i]}")
        # if(i==0):
        #     money = 1000
        # elif(i==1):
        #     money = 2000
        # elif(i==2):
        #     money = 5000
        # elif(i==3):
        #     money = 10000
        # elif(i==4):
        #     money = 20000
        money = levels[i]

    else:
        print("Wrong Answer!")
        money = levels[i-1]

    print("Your takehome money is:",money)
3