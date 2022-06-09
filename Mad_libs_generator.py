#Generates the story based on the user input. User has to provide noun, pronoun,adjectives etc.

num = int(input("Number of stories you want to create: "))
iter = 0
while iter < num:
    name = input("Enter your name: ")
    adjective = input("Enter an adjective:")
    noun = input("Enter a noun: ")
    pronoun = input("Enter a pronoun(him/her/it/he/she): ")
    preposition = input("Enter a preposition(on/in):")

    print("--------------------------------------")
    print("Hello ",name,"!. You are a",adjective,"person.")
    print("Do you see that",noun,preposition,"the table.")
    print("Please throw",pronoun,"outside.")
    print("--------------------------------------")

    iter += 1