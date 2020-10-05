import time
import sys
import functions

textSpeed=(0.1) #Sleep-Time between letters in Seconds [standard=0.1]
deniedWait=(1)  #Developer-Setting [standard=1]
password="general kenobi" #Access password [standard="1234"]

def init():
    access=False
    attempts=3
    print("Hello there! Please enter the Password:")
    while access==False:
        r1=input("Password:").lower()
        if r1==password:
            access=True
        elif attempts>1:
            attempts=attempts-1
            print("\nAccess denied! Try again (" + str(attempts) + " attemps remaining)")
        else:
            print("Access denied! Device locked for 30 Seconds")
            sec = 31    #seconds + 1
            digits = len(str(sec - 1))
            delete = "\b" * (digits)
            for i in range(sec):
                print("{0}{1:{2}}".format(delete, i, digits), end="")
                sys.stdout.flush()
                time.sleep(deniedWait)
            print()
    start()

def showHelp():
    functions.tell("Is this your first time using µ-tech?", textSpeed)
    inp=input()
    if "yes" in inp.lower():
        functions.tell("Ahh I see . . . So we'll start with the basics", textSpeed)
        basicHelp()
    elif "no" in inp.lower():
        functions.tell("Oh . . . So why do you need help then?", textSpeed)
        advHelp(input())
    else:
        simpleInput(inp)

def basicHelp():
    pass

def advHelp(s):
    if "" in s.lower():
        pass                #case:1
    elif "" in s.lower():
        pass                #case:2
    else:
        simpleInput(s)      #case:default

def simpleInput(s):
    if "help" in s.lower(): showHelp()
    if "exit" in s.lower(): functions.tell("System shutting down... See you soon", textSpeed), exit()

def start():
    print("\nAccess granted!")
    print("Initialising script")
    functions.loading()
    functions.tell("Welcome to µ-tech", textSpeed)
    functions.tell("What can I do for you? If you need help just ask for it", textSpeed)
    inp=input()
    simpleInput(inp)
    
init()