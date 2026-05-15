import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

hour = int(time.strftime("%H"))
print(hour)

if(hour<12):
    print("good morning") 
elif(hour<16):
    print("Good afternoon")
else:
    print("Good evening")