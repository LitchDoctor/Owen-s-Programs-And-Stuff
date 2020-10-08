import time
import datetime
import random
import sys
from os import system, name 

from ShopOptions import *

barracks = Barracks()
weaponry = Weaponry()
trapFactory = TrapFactory()
raMirror = RaMirror()

shopOptions = [barracks, weaponry, trapFactory, raMirror]

alphabet = "abcdefghijklmnopqrstuvwxyz"

def getDelay(args):
    return 0.25 if "-f" in args or "--fast" in args else 1

def clear(): 
    if name == 'nt': 
        _ = system('cls') 

    else: 
        _ = system('clear') 

delay = getDelay(sys.argv)

def StringIt(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def Record(score,PrevRec,path):
    if score > PrevRec:
        print("Congratulations, you survived",str(score),"rounds and set a new record. What do you want to be showcased as?")
        NewName = input(":")
        f = open(path, "w")
        f.write(str(score) + "\n")
        f.write(NewName+"\n")
        x = str(datetime.datetime.now())
        y = int(x[11:13])
        if int(y) > 12:
            y = y - 12
            x = x[:11] + str(y) + x[13:]
            f.write(("on "+ x[0:4] + "/" + x[6:7] + "/" + x[9:10]+ " at "+ x[11:16] + "pm."))
        else:
            f.write(("on "+ x[0:4] + "/" + x[6:7] + "/" + x[9:10]+ " at "+ x[11:16] + "am."))

    else:
        print("You only got to round "+str(score)+" and did not beat the previous record of "+str(PrevRec)+" rounds.")
def store (knights, production, traps, kskill, vskill):
    choice = "none"
    while choice != "":
        print("                    Welcome to the store.")
        clear()
        # Table columns
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("    Item        cost        effect")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        time.sleep(delay)

        # Display store options

        maxShopStringLength = 0
        maxCostStringLength = 0

        for shopOption in shopOptions:
            maxShopStringLength = max([maxShopStringLength, len(shopOption.getShopString()) + 1])
            maxCostStringLength = max([maxCostStringLength, len(str(shopOption.getCost())) + 1])

        option = 0

        for shopOption in shopOptions:
            displayString = "(" + alphabet[option] + "):"
            displayString += shopOption.getShopString()
            displayString += " " * (maxShopStringLength - len(shopOption.getShopString())) + "| "
            displayString += str(shopOption.getCost())
            displayString += " " * (maxCostStringLength - len(str(shopOption.getCost()))) + "| "
            displayString += shopOption.getDescription()

            option += 1

            print(displayString)
        
        # Get user choice
        print("To purchase an item, input the letter on the left. \nTo exit the shop, enter nothing. If you enter anything else, the shop will reload.")
        time.sleep(2 * delay)
        print("_____________________________________________________________")
        choice = input("You have " + str(knights) + " knights to spend, what do you want to purchase?\n: ")
        clear()
        
        if choice == "":
            break
        if choice not in alphabet:
            print("                      INVALID INPUT")
            time.sleep(delay)
            pass

        choice = alphabet.index(choice)

        if choice > len(shopOptions):
            print("                      NOT AN OPTION")
            time.sleep(delay)
            pass

        # Evaluate user choice, buy items

        purchasedOption = shopOptions[choice]

        if purchasedOption.canPurchase(knights):
            knights -= purchasedOption.getCost()
            purchasedOption.purchase()

            if purchasedOption.getProduction() != -1:
                production = purchasedOption.getProduction()
            
            if purchasedOption.getKSkill() != -1:
                kskill = purchasedOption.getKSkill()
            
            if purchasedOption.getVikingsTrapped() != -1:
                traps = purchasedOption.getVikingsTrapped()
            
            if purchasedOption.getSubtractedSkill() != -1:
                vskill -= purchasedOption.getSubtractedSkill()
        else:
            print("You cannot purchase the", purchasedOption.getName() + ".")
            pass
        
        purchaseString = "You have successfully purchased a " + purchasedOption.getName()
        
    print("                         Leaving shop")
    return(knights,  production,  traps,  kskill,  vskill)

def battle(knights, Round, kskill, vskill, traps):
    kattack = 0
    vattack = 0

    vikings = random.randint(0, round(0.1 * knights * Round))

    clear()

    print("A horde of", vikings, "vikings approach, and your,", knights, "knights rush to the defense...")
    
    time.sleep(delay)
    
    vikings = vikings - random.randint(0, traps)
    vDead = 0
    kDead = 0
    
    while vikings > vDead and knights > kDead:
        kAlive = knights - kDead
        vAlive = vikings - vDead
        print("  ▐   " * kAlive + "(>| " * vAlive)
        print("  ▐   " * kAlive + "  | " * vAlive)
        print("«=╬=» " * kAlive + "  | " * vAlive)
        print("  ⌡   " * kAlive + "  ! " * vAlive)
        print("\ ▐ / " * kDead + "(>| ")
        print(" \▐/  " * kDead + " \|/")
        print("«=X=» " * kDead + "  X ")
        print(" /⌡\  " * kDead + " /!\\")
        print("Knights Alive:", knights - kDead)
        print("Knights Slain:", kDead)
        print("Vikings Alive:", vikings - vDead)
        print("Vikings Slain:", vDead)
        time.sleep(.5 * delay)
        kattack = random.randint(0, kskill)
        vattack = random.randint(0, vskill)
        
        if vattack > kattack:
            kDead += 1
            print("A knight has been slain!")
        
        if kattack > vattack:
            vDead += 1
            print("A viking has been slain!")
        time.sleep(.5 * delay)
        clear()
    
    return(knights - kDead)
1