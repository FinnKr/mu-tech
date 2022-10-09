import time
import sys
import functions

textSpeed = (0.01) # Sleep-Time between letters in Seconds [standard=0.1]
deniedWait = (1)  # Developer-Setting [standard=1]
password = "" # Access password [standard="1234"]
isNight = False

def init():
    access = False
    attempts = 3
    print("Hello there! Please enter the Password:")
    while access == False:
        r1 = input("Password:").lower()
        if r1 == password:
            access = True
        elif attempts > 1:
            attempts = attempts-1
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
    inp = input()
    if "yes" in inp.lower():
        functions.tell("Ahh I see . . . So we'll start with the basics", textSpeed)
        basicHelp()
    elif "no" in inp.lower():
        functions.tell("Oh . . . So why do you need help then?", textSpeed)
        inp = input()
        advHelp(inp)
    else:
        simpleInput(inp)
    return

def basicHelp():
    functions.tell("µ-tech is a text-based RPG, but i guess you knew that already . . .", textSpeed)
    functions.tell("You can place your orders via the command-line interface... Try it out", textSpeed)
    return

def advHelp(s):
    if "" in s.lower():
        pass                #case:1
    elif "" in s.lower():
        pass                #case:2
    else:
        simpleInput(s)      #case:default
    return

def getUp():
    functions.tell("You're trying to get up...", textSpeed)
    functions.tell("...", textSpeed)
    functions.tell("You're not strong enough yet...", textSpeed)
    functions.tell("Sleep or eat something first...", textSpeed)
    return

def eat():
    functions.tell("Hmmmm!", textSpeed)
    functions.tell("You're biting in the first apple you've eaten for years.", textSpeed)
    functions.tell("As you're eating, your strength comes back slowly", textSpeed)
    functions.tell("...", textSpeed)
    return

def sleep():
    if not isNight:
        functions.tell("You're trying to fall asleep but it's just too bright right now.", textSpeed)
        functions.tell("You should wait for the night.", textSpeed)
    else:
        functions.tell("You're falling asleep instantly as you're laying down", textSpeed)
        functions.tell("...", textSpeed)
        functions.tell(".....", textSpeed)
        functions.tell("zzzzZZZZhhh", textSpeed)
        isNight = False
    return

def waitForNight():
    isNight = True
    functions.tell("You're sitting on the ground until the night arrives.", textSpeed)
    return

def simpleInput(s):
    if "help" in s.lower(): showHelp()
    if "exit" in s.lower(): functions.tell("System shutting down... See you soon", textSpeed), exit()
    if "get up" in s.lower(): getUp()
    if "eat" in s.lower(): eat()
    if "sleep" in s.lower(): sleep()
    if "wait for night" in s.lower: waitForNight()
    return

def start():
    print("\nAccess granted!")
    print("Initialising script")
    functions.loading()
    functions.tell("Welcome to µ-tech", textSpeed)
    functions.tell("What can I do for you? If you need help just ask for it", textSpeed)
    inp = input()
    simpleInput(inp)
    return

init()