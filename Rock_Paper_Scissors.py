#Rock beats Scissors
#Scissors beat paper
#paper beats Rock

import random
myScore = 0
opponentScore = 0
gameDict = {'S': "Scissors", 'P': "Paper",'R': "Rock"}

def finalScore():
    if myScore > opponentScore:
        print("Yayy!! I win!")
    elif myScore < opponentScore:
        print("Aww!! opponent wins!")
    elif myScore == opponentScore:
        print("It's a Tie!")
    print("--------GAME FINISHED----------")

def startGame():
    print("-----------GAME STARTS----------")
    try:
        round = int(input("Please enter the number of rounds you want:"))
    
        if round <= 0:
            raise ValueError
        loop = 1
        while(loop <= round):
            try:
                global myScore
                global opponentScore
                global gameDict
                myinput = input("[R]ock, [P]aper, [S]cissors?")
                if myinput.upper()!='R' and myinput.upper()!='S' and myinput.upper()!='P':
                    raise ValueError
                choices = ['R','P','S']
                opponent_input = random.choice(choices)
                print("Oppenent input:",opponent_input)
                if myinput.upper() == opponent_input:
                    print("Tie!")
                    print("Points to none...")
                    print("---------------------------------")
                elif myinput.upper()=='R' and opponent_input=='S':
                    myScore += 1
                    print("Rock beats Scissors!")
                    print("Points to me...")
                    print("---------------------------------")
                elif myinput.upper()=='S' and opponent_input=='P':
                    myScore+=1
                    print("Scissors beat Paper!")
                    print("Points to me...")
                    print("---------------------------------")
                elif myinput.upper()=='P' and opponent_input=='R':
                    myScore+=1
                    print("Paper beat Rock!")
                    print("Points to me...")
                    print("---------------------------------")
                else:
                    opponentScore += 1
                    print(gameDict[opponent_input],"beat",gameDict[myinput.upper()],"!")
                    print("Points to opponent...")
                    print("---------------------------------")
                loop += 1
            except ValueError as ve:
                print("Please enter (R/S/P).")
        finalScore()
    except ValueError as ve:
        print("Invalid Input.")
        print("-----------GAME FINISHED----------")
        

if __name__=='__main__':
    startGame()