# Module 8 - Problem Set No. 14 Problem 2

## Bot Army

This problem will have you complete a program. 

The code is to be used to build an army of Bots. 

Each of the bots will be assigned a **botId** attribute and will recieve a random **healthScore** between 0 and 100 when each bot is instantiated. 

The bots will be created using the **Bot** class. This class has been provided for you.

The **Bot** class also has a **setHealth method** that is used to generate a random number between -100 and 100 which is then added to the **healthScore** for the bot.

The main function will create the **botArmy list**, and then generate **healthScores** for each bot 100 times. You will need to use a nested loop for this.

You are then to loop through the botArmy list and call the **setHealth method** of the **Bot** class.

Then loop through the botArmy list and if the bot objects  **healthScore** property is less than zero, create a new property named **dead** and assign it the value **True**. Else, set
it to **False**.

Lastly, print out each bot's Id, healthScore, and the value of the dead property.