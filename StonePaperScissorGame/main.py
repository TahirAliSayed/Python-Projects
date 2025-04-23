import random
#0: Stone
#1: Paper
#2: Scissor

random_number = random.choice([1,2,3])
computer = random_number 
print('''
#1: Stone
#2: Paper
#3: Scissor''')
you = int(input("Enter your choice: "))
gameDict = {
    1: "stone", 2: "paper", 3:"scissor"
}
playerAns = gameDict[you]
compAns = gameDict[computer]
print(f'Your Choice: {playerAns}\nComputers Choice: {compAns}\n')
if(compAns == playerAns):
    print("Its a draw")
else:
    if (compAns == gameDict[1] and playerAns == gameDict[2] ):
        print("YOU WON!!")
    elif (compAns == gameDict[1] and playerAns == gameDict[3] ):
        print("YOU LOST!!")
    elif (compAns == gameDict[2] and playerAns == gameDict[1] ):
        print("YOU LOST!!")
    elif (compAns == gameDict[2] and playerAns == gameDict[3] ):
        print("YOU WON!!")
    elif (compAns == gameDict[3] and playerAns == gameDict[1] ):
        print("YOU WON!!")
    elif (compAns == gameDict[3] and playerAns == gameDict[2] ):
        print("YOU LOST!!")
    elif():
        print("Something went wrong!!")

