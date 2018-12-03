#Name : Joseph Cormier
#Class : CSCI 141
#Assignment : 
#heres where I write something cheeky when im not tired

def displayPlayer(player): 
    print("Player Status")
    print("HP =     ",player[0])
    print("Gold =   ",player[1])
    print("Attack = ",player[2])
    
def displayEnemy(enemy): #enemies will be stored as ['name','HP','gold dropped','attack damage']
    print(enemy[0], "status")
    print("HP =     ",enemy[1])
    print("Gold =   ",enemy[2])
    print("Attack = ",enemy[3])

def enterPath(path,playerList,round):
    if path == "shop":
        playerList = shop(playerList,round)
    elif path == "quit":
        print("Quitting game")
    else:
        print("no path chosen")
    return playerList
    
def shop(playerList,round):
    print("check")
    if playerList[1] >= 10:
        print("You've got some money")
        return playerList
    else:
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
        input()


main()