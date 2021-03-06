import sys

# Create empty dictionary and variables
playerList = {}

print("Enter the player names and press Ctrl + C when done.")
try:
    while True:
        #ask users for their name
        playerName = raw_input("\nWhat is your name? ")
        
        #store the responses in a dictionary
        if playerName == "":
            print("You didn't type anything. If you're done, press Ctrl + C.")
            pass
        elif playerName not in playerList:
            playerList[playerName] = 15000000
        else:
            print("That name already exists. Try again.")

except KeyboardInterrupt:
    print("\nDone with input")

print("Press Ctrl + C if you want to exit the programme.")

def quitPlaying():
    print('Are you sure? Type "Yeah, I am so done." if you want to exit.')
    confirmExit = raw_input()
    if confirmExit == "Yeah, I am so done.":
        print("I'm pretty tired myself. Bye!")
        sys.exit(0)
    else:
        print("Naaaaaaaaah you secretly want to keep playing.\n")

while True:
    # Prints out how much money everyone has
    print("\nHere's how much money everyone has:")
    for key, value in playerList.iteritems():
        print('%s: $%s' % (key, '{:,}'.format(value)))
    
    # Asks how much money is being transferred
    while True:
        print ("Type in an amount you would like to DEPOSIT/WITHDRAW.")
        try:
            amount = int(input())
            break 
        except KeyboardInterrupt:
            quitPlaying()
        except:
            print ("It is not a integer.")
    
    # Asks from whom the money is being withdrawn from
    while True:
        try:
            transferFrom = raw_input("\nWho are you withdrawing from? Press ENTER if none.\n")
            if transferFrom == '':
                break
            elif transferFrom in playerList:
                if playerList[transferFrom] < amount:
                    print ("%s does not have enough money." % transferFrom)
                    break
                else:
                    playerList[transferFrom] = playerList[transferFrom] - amount
                    break
            else:
                print("%s does not exist" % (transferFrom))
        except KeyboardInterrupt:
            quitPlaying()

    # Asks to whom the money is being deposited to
    if transferFrom == '' or playerList[transferFrom] > amount:
        while True:
            try:
                transferTo = raw_input("\nWho are you depositing to? Press ENTER if none.\n")
                if transferTo == '':
                    break
                elif transferTo in playerList:
                    playerList[transferTo] = playerList[transferTo] + amount
                    break
                else:
                    print("%s does not exist" % (transferTo))
            except KeyboardInterrupt:
                quitPlaying()