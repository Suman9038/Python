import random
'''
1 for snake
-1 for water 
0 for gun

'''
computer = random.choice([-1, 0, 1])
UserInput = int(input("Enter your choice: "))
#UserDict = {"s": 1, "w": -1, "g": 0}
Dict = {1: "Snake", -1: "Water", 0: "Gun"}

#you = UserDict[UserInput]

# By now we have 2 numbers (variables), you and computer

print(f"You choose {Dict[UserInput]}\nComputer chose {Dict[computer]}")

if(computer == UserInput):
    print("Its a draw")

else:
    if(computer ==-1 and UserInput == 1): 
        print("You win!")

    elif(computer ==-1 and UserInput == 0):
        print("You Lose!")

    elif(computer == 1 and UserInput == -1):
        print("You lose!")

    elif(computer ==1 and UserInput == 0):
        print("You Win!")

    elif(computer ==0 and UserInput == -1):
        print("You Win!")

    elif(computer == 0 and UserInput == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")