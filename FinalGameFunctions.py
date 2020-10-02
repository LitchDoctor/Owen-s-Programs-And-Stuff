import time
import datetime
import random
import sys

def getDelay(args):
    return 0.25 if "-f" in args else 1

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
    print("                    Welcome to the store.")
    while choice != "":
        if choice != "none" and choice != "a" and choice != "b" and choice != "c" and choice != "d":
            print("                      INVALID INPUT")
            time.sleep(delay)
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        time.sleep(delay)
        print("    Item        cost        effect")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        if production == 1:
            print("(a):Barracks      5         knight production = 2")
        if kskill == 6:
            print("(b):Weaponry      15        Improves knight effectiveness")
        if traps == False:
            print("(c):Trap Center   25        kills 10 vikings each round")
        if vskill == 6:
            print("(d):Ra Mirror     30        Blinds enemy, decreasing strength")
        if production == 1 or kskill == 6 or traps == False or vskill == 6:
            print("To purchase an item, input the letter on the left. To exit the\n"
              "shop, enter nothing. If you enter anything else, the shop will reload.")
            time.sleep(2 * delay)
            print("_____________________________________________________________")
            choice = input("You have "+str(knights)+" knights to spend, what do you want to purchase?\n: ")
        else:
            print("You have purchased everything in the shop proceeding to battle")
            print("_____________________________________________________________")
            time.sleep(2 * delay)
            return (knights, production, traps, kskill, vskill)
        if choice == "a":
            if knights > 5 and production == 1:
                knights = knights-5
                production = 2
                time.sleep(delay)
                print("You have successfully purchased a barracks.")
                print("___________________________________________")
                time.sleep(delay)
                print("You now have", str(knights), "knights remaining.")
            elif knights < 6:
                print("Purchasing the Armory would reduce your knights below 1 ending your empire.")
        if choice == "b":
            if knights > 15 and kskill == 6:
                knights = knights-15
                kskill = 7
                time.sleep(delay)
                print("You have successfully purchased a weaponry.")
                print("__________________________________________")
                time.sleep(delay)
                print("You now have", str(knights), "knights remaining.")
            elif knights < 16:
                print("Purchasing the Weaponry would reduce your knights below 1 ending your empire.")
        if choice == "c":
            if knights > 25 and traps == False:
                knights = knights-25
                traps = True
                time.sleep(delay)
                print("You have successfully purchased a trap center.")
                print("______________________________________________")
                time.sleep(delay)
                print("You now have", str(knights), "knights remaining.")
            elif knights < 26:
                print("Purchasing the Trap Factory would reduce your knights below 1 ending your empire.")
        if choice == "d":
            if knights > 30 and vskill == 6:
                knights = knights-30
                vskill = 5
                time.sleep(delay)
                print("You have successfully purchased a ra mirror.")
                print("____________________________________________")
                time.sleep(delay)
                print("You now have", str(knights), "knights remaining.")
            elif knights < 31:
                print("Purchasing the Ra Mirror would reduce your knights below 1 ending your empire.")
    print("                         Leaving shop")
    return(knights,  production,  traps,  kskill,  vskill)

def battle(knights, Round, kskill, vskill, traps):
    kattack = 0
    vattack = 0
    vikings = round(Round*0.6)
    print("A horde of",vikings,"vikings approach, and your,",knights,"knights rush to the defense...")
    time.sleep(delay)
    print("  ▐   "*knights +"(>|"*vikings)
    print("  ▐   "*knights +"  |"*vikings)
    print("«=╬=» "*knights +"  |"*vikings)
    print("  ⌡   "*knights +"  !"*vikings)
    if traps == True:
        vikings = vikings-10
    while vikings > 0 and knights > 0:
        time.sleep(.5 * delay)
        kattack = random.randint(0,kskill)
        vattack = random.randint(0,vskill)
        if vattack > kattack:
            knights = knights-1
            print("A knight has been slain!")
        if kattack > vattack:
            vikings = vikings -1
            print("A viking has been slain!")
    return(knights)
