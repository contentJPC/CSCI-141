#Name : Joseph Cormier
#Class : CSCI 141
#Assignment : final project, some silly game
#heres where I write something cheeky when im not tired

def displayPlayer(player): 
    print("Player Status")
    print("HP =     ",player[0])
    print("Gold =   ",player[1])
    print("Attack = ",player[2])
    
def displayEnemy(enemy): #enemies will be stored as ['name','HP','gold dropped','attack damage']
    print(enemy[0],"status")
    print("HP =     ",enemy[1])
    print("Gold =   ",enemy[2])
    print("Attack = ",enemy[3])

def enterPath(path,playerList,round):
    if path=="shop":
        playerList = shop(playerList,round)
    elif path=="quit":
        print("Quitting game")
    elif path=="forest":
        forest(playerList,round)
    elif path=="cave":
        cave(playerList,round)
    else:
        print("no path chosen")
    return playerList

def forest(playerList,round):
    enemyList = [["Bandit",10,5,5],["Theif",10,5,5],]
    playing = "true"
    while playing!="quit":
        
        displayEnemy(enemyList[0])
        print("forest function")
        return playerList
    
def cave(playerList,round):
    print("cave function")
    returnPlayerList
    
def purchase(playerList,buy,mult):
    if playerList[1]>0:     
        if buy=="health":
            playerList[0] = playerList[0] + 10*mult
            playerList[1] = playerList[1] - 1
        elif buy=="gear":
            playerList[2] = playerList[2] + 5*mult
            playerList[1] = playerList[1] - 1
        else:
            print("could not understand")
    else:
        print("You have no money!")
    return playerList
    
def shop(playerList,round):
    buy = "empty"
    if round%7==0:
        while buy!="quit":
            print("\nWE HAVE A SALE TODAY, 2 FOR THE PRICE OF ONE! What would you like to buy? 'health'? (+20 hp, -1 gold) or 'gear'? (+10 attack, -1 gold)")
            buy = input("Or type 'quit' to leave the shop : ")
            playerList = purchase(playerList,buy,2)
            displayPlayer(playerList)
    else:
        while buy!="quit":
            print("\nWhat would you like to buy? 'health'? (+10 hp, -1 gold) or 'gear'? (+5 attack, -1 gold)")
            buy = input("Or type 'quit' to leave the shop : ")
            playerList = purchase(playerList,buy,1)
            displayPlayer(playerList)
    return playerList

def main():
    #Player stats, figure i might as well put them here so they're reset each time the player runs main
    playerList = [100, #HP
                  10, #Gold
                  5] #Attack
    round = 0 #to keep a running total of game rounds for possible features
    path = "undecided" #if this is "quit" when the player asks if they want to end the game it will close the game
    
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to text adventure!")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    while path != "quit":
        round = round+1 #increase round counter so we start at round 1 for the first round/day and continue it every loop
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Day",round)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
        displayPlayer(playerList)
        print("")
        print("What would you like to do? 'shop', hunt in the 'forest', or explore the 'cave'?")
        path = input("Or type 'quit' to stop playing (no data will be saved, no method to save at this time) : ")
        #here we will run a function that will choose a function for the players path based on what they choose
        playerList = enterPath(path,playerList,round)
        if playerList[0]<=0:
            print("After scraping your way back to rest, you pass away from you injuries in your sleep (game over)")
            path = "quit"
        input("press enter to continue")


main()