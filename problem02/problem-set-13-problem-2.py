# Module 8 - Problem Set No. 14 - Problem 2
# YOUR NAME

import random


class Bot:
    # when new Bots get created
    # the playerId gets passed in
    def __init__(self, botId):
        # set id to the playerId
        self.__playerId = botId

        # set healthScore to a random number between 0 and 100
        self.__healthScore = random.randint(0, 100)

    def getPlayerId(self):
        return self.__playerId

    def getHealth(self):
        return self.__healthScore

    def setHealth(self):
        # generates a random health score between -100 and 100
        randomHealthScore = random.randint(-100, 100)

        # add the exisiting healthScore to the newly generated score
        newHealthScore = self.__healthScore + randomHealthScore

        # set the healthScore to this new score
        self.__healthScore = newHealthScore

# main function


def main():
    pass  # remove this line

    # create botArmy list
    # Your code goes here

    # Create a bot army with 100 bots and add to botArmy list
    # Your code goes here

    # create nested loops to set the health 100 times
    # Your code goes here

    # Loop through the botArmy
    # Your code goes here

    # If health score < 0 then set the dead property to True. If it is above 0
    # then set dead to False
    # Your code goes here

    # Display the bot army, the healthScore and dead properties
    # Your code goes here

    # begin the program


main()
