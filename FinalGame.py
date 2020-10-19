from FinalGameFunctions import *
import time
import sys
path = "./FinalGameInfo.ogw"

PrevRec = 0
PrevName = ""
date = ""

with open(path, "r") as f:
    PrevRec = int(StringIt(f.readlines(1)).strip())
    PrevName = StringIt(f.readlines(1)).strip()
    date = StringIt(f.readlines(1)).strip()
    f.close()

delay = getDelay(sys.argv)

Round = 1
knights = 15
production = 1
traps = 0
kskill = 6
vskill = 6
print('''██╗  ██╗██╗███╗   ██╗ ██████╗ ██████╗  ██████╗ ███╗   ███╗
██║ ██╔╝██║████╗  ██║██╔════╝ ██╔══██╗██╔═══██╗████╗ ████║
█████╔╝ ██║██╔██╗ ██║██║  ███╗██║  ██║██║   ██║██╔████╔██║
██╔═██╗ ██║██║╚██╗██║██║   ██║██║  ██║██║   ██║██║╚██╔╝██║
██║  ██╗██║██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ''')
time.sleep(2 * delay)
print('''             /\_[]_/\          |\              //
            |] _||_ [|          \ \           _!_
      ___    \/ || \/            \ \         /___\ 
     /___\      ||                \ \        [+++]
   (| 0 0 |)    ||                 \ \    _ _\^^^/_ _
 __/{\ U /}\_ __/vvv                 \ \/ (    '-'  ( )
/ \  {~}   / _|_P|                    /( \/ | {&}   /\ \ 
| /\  ~   /_/   []                    \  / \     / _  > )
|_| (____)                             "`   >:::;-'`""'-.
\_]/______\                                /::: /         \ 
   _\_||_/_                               /  /| |   {&}   |
  (_,_||_,_)                             (  / ( \         /
                                         / /   \ '-.___.-'
                                       _/ /     \ \ 
                                      /___|    /___| 
    ''')
time.sleep(2 * delay)
print("The previus record holder was", PrevName, "with", str(PrevRec), "round/s survived.\nThis record was achieved "+date)
time.sleep(2 * delay)
while knights > 0:
    time.sleep(delay)
    knights, production, traps, kskill, vskill =store(knights,production,traps,kskill,vskill)
    if traps == True:
        print("You now have traps")
    knights = battle(knights,Round,6,6,False)
    if knights > 0:
        print("___________________________________________________________________________\n"
              "You have vanquish this round of vikings with",knights,"knights still alive.\n"
              "___________________________________________________________________________")
        Round = Round + 1
        knights = knights + production
    vskill = 6 + round(0.1 * Round)
    time.sleep(2 * delay)
print("_________________________________________________________________\n"
      "All of your knights have been killed and your kingdom has fallen.\n"
      "_________________________________________________________________")
Record(Round,PrevRec,path)
