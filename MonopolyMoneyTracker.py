# Import regular expression module
import re

# Create empty dictionary and variables
playerList = {}

print("Enter the player names and type \"Done\" when you are finished.")
while True:
    #ask users for their name
    playerName = input("\nWhat is your name? ")

    #store the responses in a dictionary
    if playerName == "":
        print("You didn't type anything. If you're done, type \"Done\".")
        pass
    elif playerName == "Done" or playerName == "done":
        print("\nDone with input")
        break
    elif playerName not in playerList:
        playerList[playerName] = 15000000
    else:
        print("That name already exists. Try again.")

print ("\nPLEASE READ:")
print ("Type \"Exit\" if you want to exit the programme.")
print ("Use k or K to represent 1,000.")
print ("Use m or M to represent 1,000,000.")
print ("e.g. 1.2M\n")

def quitPlaying():
    print('Are you sure? Type "Yeah, I am so done." if you want to exit.')
    confirmExit = input()
    if confirmExit == "Yeah, I am so done.":
        print("I'm pretty tired myself. Bye!")
    else:
        print("Naaaaaaaaah you secretly want to keep playing.\n")

while True:
    # Prints out how much money everyone has
    print("\nHere's how much money everyone has:")
    for key, value in playerList.items():
        print('%s: $%s' % (key, '{:,}'.format(value)))

    # Asks how much money is being transferred
    while True:
        print ("Type in an amount you would like to DEPOSIT/WITHDRAW.")
        amount = input()
        # If they type Exit, then they exit the program
        if amount == "Exit" or amount == "exit":
           quitPlaying()
        # Validate for the correct input
        elif re.match("[1-9](\d{1,3})?(\.\d{1,3})?[m|M|k|K]", amount):
            amountNum = float(amount[:-1])
            amountLetter = amount[-1]
            if amountLetter == "m" or amountLetter == "M":
                calculatedAmount = int(amountNum * 1000000)
            if amountLetter == "k" or amountLetter == "K":
                calculatedAmount = int(amountNum * 1000)
            break
        else:
            print ("That is an invalid input.")

    # Asks from whom the money is being withdrawn from
    while True:
        transferFrom = input("\nWho are you withdrawing $%s from? Press ENTER if none.\n" % '{:,}'.format(calculatedAmount))
        if transferFrom == '':
            break
        # If they type Exit, then they exit the program
        elif transferFrom == "Exit" or amount == "exit":
           quitPlaying()
        elif transferFrom in playerList:
            if playerList[transferFrom] < calculatedAmount:
                print ("%s does not have enough money." % transferFrom)
                break
            else:
                playerList[transferFrom] = playerList[transferFrom] - calculatedAmount
                break
        else:
            print("%s does not exist" % (transferFrom))

    # Asks to whom the money is being deposited to
    while True:
        transferTo = input("\nWho are you depositing $%s to? Press ENTER if none.\n" % '{:,}'.format(calculatedAmount))
        if transferTo == '':
            break
        # If they type Exit, then they exit the program
        elif transferTo == "Exit" or amount == "exit":
           quitPlaying()
        elif transferTo in playerList:
            playerList[transferTo] = playerList[transferTo] + calculatedAmount
            break
        else:
            print("%s does not exist" % (transferTo))
