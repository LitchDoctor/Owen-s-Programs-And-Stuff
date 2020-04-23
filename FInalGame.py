from FinalGameFunctions import StringIt
from FinalGameFunctions import Record
from FinalGameFunctions import store
from FinalGameFunctions import battle
import time
path = "c:/users/ogw/pycharmprojects/schoolscripts/lib/FinalGameInfo"

f = open(path, "r")
PrevRec = int(StringIt(f.readlines(1)).strip())
PrevName = StringIt(f.readlines(1)).strip()
date = StringIt(f.readlines(1)).strip()
f.close()

Round = 1
knights = 15
production = 1
traps = False
kskill = 6
vskill = 6
print('''██╗  ██╗██╗███╗   ██╗ ██████╗ ██████╗  ██████╗ ███╗   ███╗
██║ ██╔╝██║████╗  ██║██╔════╝ ██╔══██╗██╔═══██╗████╗ ████║
█████╔╝ ██║██╔██╗ ██║██║  ███╗██║  ██║██║   ██║██╔████╔██║
██╔═██╗ ██║██║╚██╗██║██║   ██║██║  ██║██║   ██║██║╚██╔╝██║
██║  ██╗██║██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ''')
time.sleep(2)
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
time.sleep(2)
print("The previus record holder was", PrevName, "with", str(PrevRec), "round/s survived.\nThis record was achieved "+date)
time.sleep(2)
while knights > 0:
    time.sleep(1)
    knights, production, traps, kskill, vskill =store(knights,production,traps,kskill,vskill)
    if traps == True:
        print("You now have traps")
    knights = battle(knights,Round,6,6,False)
    if knights > 0:
        print("You have vanquish this round of vikings with",knights,"knights still alive.\n"
              "___________________________________________________________________________")
        Round = Round + 1
        knights = knights+production
    time.sleep(2)
print("All of your knights have been killed and your kingdom has fallen.\n"
      "_________________________________________________________________")
Record(Round,PrevRec,path)