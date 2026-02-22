import random 
c=random.randint(1,100)
print("ready to guess??")
print("u have 7 attempts")
attempts=0
while True:
    i=int(input("enter the number:"))
    attempts +=1
    if  i == c:
     print("right,u win!!")
     break
    elif attempts==7:
        print("game over , u lose")
        print("the number was",c)
        break
    elif i<c:
     print("too low:( ,try again")
    elif i>c:
     print("too high:( ,try again")
    else:
     print("INVALID")
