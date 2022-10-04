from FinalGameFunctions import *
import time
import sys
import re
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

DARK_GRAY="\033[1;30m"
GREEN="\033[0;32m"
RED="\033[0;31m"
RESET="\033[0m"

Round = 1
knights = 15
production = 1
traps = 0
kskill = 6
vskill = 6
splash = '''██╗  ██╗██╗███╗   ██╗ ██████╗ ██████╗  ██████╗ ███╗   ███╗
██║ ██╔╝██║████╗  ██║██╔════╝ ██╔══██╗██╔═══██╗████╗ ████║
█████╔╝ ██║██╔██╗ ██║██║  ███╗██║  ██║██║   ██║██╔████╔██║
██╔═██╗ ██║██║╚██╗██║██║   ██║██║  ██║██║   ██║██║╚██╔╝██║
██║  ██╗██║██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝'''

print(re.sub(r"(?<!█)(█)", GREEN + "█", re.sub(r"█(?!█)", "█" + DARK_GRAY, splash)) + RESET)

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
        text = "You have vanquished this round of vikings with " + str(knights) + " knights still alive."
        print(DARK_GRAY + "╭" + "─" * (len(text) + 2) + "╮\n"
              "│ " + GREEN + text + DARK_GRAY + " │\n"
              "╰" + "─" * (len(text) + 2) + "╯" + RESET)
        Round = Round + 1
        knights = knights + production
    vskill = 6 + round(0.1 * Round)
    time.sleep(2 * delay)
print(DARK_GRAY + "╭───────────────────────────────────────────────────────────────────╮\n"
      "│ " + RED + "All of your knights have been killed and your kingdom has fallen. "+ DARK_GRAY + "│\n"
      "╰───────────────────────────────────────────────────────────────────╯" + RESET)
Record(Round,PrevRec,path)
