import time
import sys
import win32console

def tell(s, textSpeed):
    for i in range(len(s)):
        sys.stdout.write(s[i])
        time.sleep(textSpeed)
        sys.stdout.flush()
    print()

def loading(length=20, speed=0.2):
    j=0
    for i in range(length):
        output_handle = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
        info = output_handle.GetConsoleScreenBufferInfo()
        pos = info["CursorPosition"]
        a="/-\\|"
        output_handle.WriteConsoleOutputCharacter( a[j], pos )
        sys.stdout.write(".")
        time.sleep(speed)
        sys.stdout.flush()
        j=j+1
        if j==4: j=0
    print("\n")