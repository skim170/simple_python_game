from random import * # Imported Library for Random Number Generator (RNG)

import time # Imported Library for time.sleep hold function

# Variables
numberofGame = 0 # Keeps track of the current game number
playerOneScore = 0 # Keeps track of Player One's score
playerTwoScore = 0 # Keeps track of PLayer Two's score
roundCount = [1, 2, 3] # Array housing 3 variables, keeps track of the current round 

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[1;31m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[1;33m'

def gettingNumber(question): # Defines a function used to get the player' s input number 

    while True:

        try:

            enterValue = int(input(question)) # Sets enetervalue var equal to an integer returned from the user input. Also passes in question variable

        

            if enterValue >=1 and enterValue <=3: # Checks to see if the user's input int is between 1 and 3 

                break

            else:

                print('Enter a number between 1 to 3') # If not, it prompts them again to enter an integer within the correct range

        except:

            print('You did not enter a number. Please enter a number!') # If the user input isn't an int, it prompts the user to enter a number 

    return enterValue

#winningScore = randint(20,40)

#print ('Game Start, You will play to: ',winningScore)

print ('Welcome to our Game: "Dont say that number! \nFollow the on-screen prompts to increment the game number without matching or exceeding the' , bcolors.RED , ' number of DOOM!' , bcolors.END , '\nGood Luck!\n')

for roundCount in roundCount: # Establishes a loop iterating over every value within the roundCount array
    if (playerOneScore >= 2): # First checks to see if either player has a score greater than or equal to 2 (Best of 3 wins)
        print ( bcolors.CYAN , 'Player One Wins!!' , bcolors.END) # Will print a win message if either player has 2 points 
        break
    elif (playerTwoScore >= 2):
        print  (bcolors.GREEN , 'Player Two Wins!!' , bcolors.END)
        break

    numberofGame = 0 # Resets the game number at the beginning of each round 

    winningScore = randint(20,40) # Selects a random number between 20 and 40 to play to 

    print ('\nRound: ', roundCount, bcolors.RED , 'The Number of DOOM is: ', winningScore,'\n' , bcolors.END) # Prints the current Round and what the players are playing to 

    while True:


        time.sleep(1) # Breaks afor a second between each turn 

        enterValue = gettingNumber('\n[Player 1] How many numbers will you say? (1~3): ') # Calls the gettingNumber function passing in a question and storing 
        # its return value in enterValue variable

        for number in range(enterValue):

            print( bcolors.BOLD , '{}!'.format(numberofGame # Simple loop to print a display of the current game number, iterates as many times as the user enters
    + 1 + number) , bcolors.END)




        numberofGame += enterValue # Increments the game number appropriately




        if (numberofGame >= winningScore): # Checks if the game number has met or exceeded the max score 
            
            time.sleep(0.5)
            print ('\nPlayer 2 Wins Round ',roundCount) # Displays a message declaring the round winner, and overall game score
            playerTwoScore = playerTwoScore + 1 # Incrementes player score
            time.sleep(0.5)
            print ('Current Score,' , bcolors.CYAN, 'Player 1: ',playerOneScore, bcolors.END, bcolors.GREEN, '  Player 2: ',playerTwoScore, bcolors.END)
            time.sleep(0.5)

            break





# Below is the same code repeated for player two, each round will pass turns back and forth between both players, giving them matching prompts and information

        time.sleep(1) 

        

        # enterValue = randint(1,3)

        enterValue = gettingNumber('\n[Player 2] How many numbers will you say? (1~3): ')




        for number in range(enterValue):

            print( bcolors.BOLD , '{}!'.format(numberofGame
    + 1 + number) , bcolors.END)




        numberofGame += enterValue




        if (numberofGame >= winningScore):

            time.sleep(0.5)
            print ('\nPlayer 1 Wins Round ',roundCount)
            playerOneScore = playerOneScore + 1
            time.sleep(0.5)
            print ('Current Score,' , bcolors.CYAN + ' Player 1: ',playerOneScore, bcolors.END , bcolors.GREEN , '  Player 2: ',playerTwoScore, bcolors.END)
            time.sleep(0.5)

            break


    if (playerOneScore >= 2): # Repeats the game-win check at the end of the loop to catch the game win whenever it takes place.
        print (bcolors.YELLOW , 'Player One Wins the Game!!' , bcolors.END)
        break
    elif (playerTwoScore >= 2):
        print (bcolors.YELLOW , 'Player Two Wins the Game!!' , bcolors.END)
        break

print ('Game Over')