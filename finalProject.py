#Name : Joseph Cormier
#Class : CSCI 141
#Assignment : final project, some silly game
#heres where I write something cheeky when im not tired
#i fully accept the fact that this is coded like garbage

#so we can make random encounter
import random


#players stored as [hp,gold,attack]
def displayPlayer(player): 
    print("Player Status")
    print("HP =     ",player[0])
    print("Gold =   ",player[1])
    print("Attack = ",player[2])
    
    
#enemies will be stored as [name,HP,gold dropped,attack damage]    
def displayEnemy(enemy): #enemies will be stored as [name,HP,gold dropped,attack damage]
    print(enemy[0],"status")
    print("HP =     ",enemy[1])
    print("Gold =   ",enemy[2])
    print("Attack = ",enemy[3])
    
    
#for combat encounters we take the player stats and the enemy stats
def combat(playerInCombat,enemyList):
    combatOption = "playcombat"
    while combatOption!="return":
        #display player and enemy stats
        enemyTemp = enemyList
        print("")
        displayPlayer(playerInCombat)
        print("")
        displayEnemy(enemyTemp)
        print("")
        #ask user what they would like to do
        combatOption = input("Would you like to 'attack' or 'return' to town? : ")
        if combatOption=="attack":
            print("You attack the ",enemyTemp[0],"! : (",enemyTemp[0]," HP -",playerInCombat[2],")",sep="")
            #enemy takes damage, lower hp by player attack
            enemyTemp[1] = enemyTemp[1] - playerInCombat[2]
            print("The ",enemyTemp[0]," hits back! : (Player HP -",enemyTemp[3],")",sep="")
            #player takes damage, lower hp by enemy attack
            playerInCombat[0] = playerInCombat[0] - enemyTemp[3]
        elif combatOption=="return":
            print("you go home")
        else:
            print("please answer with a given option")
        #in the case that the enemy was defeated
        if enemyTemp[1] <= 0:
            print(enemyTemp[0],"defeated! You got",enemyTemp[2],"gold!")
            #increase player gold by enemy gold
            playerInCombat[1] = playerInCombat[1] + enemyTemp[2]
            return playerInCombat
        #player has died, automatically returns to town to end game 
        elif playerInCombat[0] <= 0:
            return playerInCombat
        
        
#players need to be able to choose if they want to go to the shop, cave, or forest
#run function based on choice
def enterPath(path,playerInPath,round):
    if path=="shop":
        playerInPath = shop(playerInPath,round)
    elif path=="quit":
        print("Quitting game")
    elif path=="forest":
        playerInPath = forest(playerInPath,round)
    elif path=="cave":
        playerInPath = cave(playerInPath,round)
    elif path=="cheatcode":
        print("cheat code activated")
        playerInPath = [100000,100000,100000]
        return playerInPath
    else:
        print("no path chosen")
    return playerInPath


#if player enters forest randomly selct an enemy and begin a combat encounter
def forest(playerInForest,round):
    enemyList = [["Bandit",10,5,5],["Thief",10,5,5],["Buff Bandit",20,10,10],["Banished Merchant",5,2000,0],["Wandering Demon",1000,10000,250]]
    randomEncounter = random.randrange(0,len(enemyList))
    combat(playerInForest,enemyList[randomEncounter])
    return playerInForest


#if player enters the cave they can only face on enemy
def cave(playerInCave,round):
    print("You enter the cold and dark cave, and come face to face with an indescribable terror")
    enemyList = ["True Horror",25000,100000000000,10000]
    combat(playerInCave,enemyList)
    return(playerInCave)


#if player makes a purchase at the shop this function will change their stats and cause an actual effect
def purchase(playerInPurchase,buy,mult,multMon):
    if playerInPurchase[1]>0:     
        if buy=="health":
            #test to make sure player won't go below 0 with the purchase
            if (playerInPurchase[1]-(1*multMon))>=0:
                playerInPurchase[0] = playerInPurchase[0] + 10*mult
                playerInPurchase[1] = playerInPurchase[1] - 1*multMon
                return playerInPurchase
            else:
                print("Not enough money!")
        elif buy=="gear":
            #test to make sure player won't go below 0 with the purchase
            if (playerInPurchase[1]-(1*multMon))>=0:
                playerInPurchase[2] = playerInPurchase[2] + 5*mult
                playerInPurchase[1] = playerInPurchase[1] - 1*multMon
                return playerInPurchase
            else:
                print("Not enough money!")
        elif buy=="quit":
            print("Leaving shop")
            return playerInPurchase
        else:
            print("please answer with a given option")
    else:
        print("You have no money!")
    return playerInPurchase


#if player chooses to go to the shop   
def shop(playerInShop,round):
    buy = "empty"
    #let player know about deals every 7 and 10 days
    print("\nSales at the end of every week and every 10th day")
    #if its a 7th day players get double the value on purchases
    if round%7==0:
        while buy!="quit":
            print("\nWE HAVE A SALE TODAY, 2 FOR THE PRICE OF ONE! What would you like to buy? 'health'? (+20 hp, -10 gold) or 'gear'? (+10 attack, -10 gold)")
            buy = input("Or type 'quit' to leave the shop : ")
            playerInShop = purchase(playerInShop,buy,2,10)
            displayPlayer(playerInShop)
    #if its the 10th day players can purchase massive power boosts, at a price
    elif round%10==0:
        while buy!="quit":
            print("\nPURCHASE YOUR ULTIMATE POWER! What would you like to buy? 'health'? (+5000 hp, -1000 gold) or 'gear'? (+250 attack, -1000 gold)")
            buy = input("Or type 'quit' to leave the shop : ")
            playerInShop = purchase(playerInShop,buy,500,1000)
            displayPlayer(playerInShop)
    #otherwise players buy small increments of stats
    else:
        while buy!="quit":
            print("\nWhat would you like to buy? 'health'? (+10 hp, -10 gold) or 'gear'? (+5 attack, -10 gold)")
            buy = input("Or type 'quit' to leave the shop : ")
            playerInShop = purchase(playerInShop,buy,1,10)
            displayPlayer(playerInShop)
    return playerInShop


#main game loop
def main():
    #Player stats, figure i might as well put them here so they're reset each time the player runs main
    playerList = [100, #HP
                  10, #Gold
                  5] #Attack
    round = 0 #to keep a running total of game rounds for possible features
    path = "undecided" #if this is "quit" when the player asks if they want to end the game it will close the game
    
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to text adventure!")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    while path != "quit":
        round = round+1 #increase round counter so we start at round 1 for the first round/day and continue it every loop
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Day",round)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        displayPlayer(playerList)
        print("\nWhat would you like to do? 'shop', hunt in the 'forest', or explore the ancient divine 'cave'?")
        path = input("Or type 'quit' to stop playing (no data will be saved, no method to save at this time) : ")
        #here we will run a function that will choose a function for the players path based on what they choose
        playerList = enterPath(path,playerList,round)
        if playerList[0]<=0:
            print("\nAfter scraping your way back to rest, you pass away from your injuries in your sleep (game over)")
            path = "quit"
        elif playerList[1]>=100000000000:
            print("\nYou have defeated an ancient evil, or are simply so rich and powerful it wouldn't dare appear before you")
            print("The rest of your days are lived out happily and in peace")
            path = "quit"
        input("\npress enter to continue\n")
        
        
#funfunfun
main()