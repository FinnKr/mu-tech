import time
import sys

def tell(s, textSpeed):
    for i in range(len(s)):
        sys.stdout.write(s[i])
        time.sleep(textSpeed)
        sys.stdout.flush()
    print()

# Create a loading bar
def loading(length = 5, speed = 20):
    """
    Call to create a loading bar with specified width and speed
    @params:
        length      - Required  : length of the loading bar (Int)
        speed       - Required  : speed of the loading process (Float)
    """
    if not (length >= 1 and isinstance(length, int)):
        raise Exception("The length needs to be an int greater than 1")
    elif not (speed > 0 and (isinstance(speed, int) or isinstance(speed, float))):
        raise Exception("The speed needs to be a float or int greater than 0")
    else:
        printProgressBar(0, length*2, prefix = "Progress:", suffix = "", length = length)
        for i in range(length*2):
            time.sleep(1/speed)
            if i == length*2-1:
                printProgressBar(i + 1, length*2, prefix = "Progress:", suffix = "Done", length = length)
            else:
                printProgressBar(i + 1, length*2, prefix = "Progress:", suffix = "", length = length)

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()