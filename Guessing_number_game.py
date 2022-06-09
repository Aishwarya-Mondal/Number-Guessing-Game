#user will guess a number between 1-10
#Hint: if input>number: "Actual Number is lower"
#      if input<number: "Actual Number is greater"
#If User wins: "Congratulations! You won!! Rounds:n, Number of Attempts:x"

import random
round = 0 #number of rounds
attempts = [] #score in each round
n_attempts = 0
def showAttempts(round):
    if len(attempts)<=0:
        print("You have not yet started!")
    else:
        print("Number of Attempts:",attempts[round])

def startGame():
    user_input = input("Do you want to start the game(yes/no)?")
    if user_input.lower()=="no":
        print("Okay! Have a nice day!")
    else:
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
        num = int(random.randint(lower,upper))
        while user_input.lower()=="yes":
            
            try:
                global round
                u_num = int(input("Enter your guess: "))
                if u_num<1 or u_num>10:
                    raise ValueError
                if u_num == num:
                    global n_attempts
                    n_attempts+=1
                    global attempts
                    attempts.append(n_attempts)
                    print("Congratulations! You won!!")
                    print("Round: ",round+1)
                    showAttempts(round)
                    user_input = input("Do you want to go for next round(yes/no)?")
                    if user_input.lower() == "no":
                        print("Okay! Have a nice day!")
                        break
                    else:
                        round += 1
                elif u_num < num:
                    
                    n_attempts +=1
                    print("Actual number is greater!")
                elif u_num > num:
                    
                    n_attempts +=1
                    print("Actual number is smaller!")
                
            except ValueError as err:
                print("Please provide number in range")


if __name__== '__main__':
    startGame()
