import time
import keyboard

def open_app(app):
    keyboard.press_and_release('win')
    time.sleep(0.3)
    keyboard.write(f'{app}', delay=0.05)
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(1.1)



def notepad_initialize():
    # keyboard.write("notepad\n", delay=0.05)
    # time.sleep(1.0)
    keyboard.write("TAAS Booting Now...\n\n", delay=0.05)
    time.sleep(0.7)

    # "loading" thing
    for i in range(30):
        keyboard.write("/", delay=0.04)
    time.sleep(0.2)
    keyboard.press_and_release('home')
    keyboard.write("D")
    for i in range(30):
        keyboard.press_and_release('delete')
        time.sleep(0.09)
        keyboard.write("-")
    time.sleep(0.1)
    keyboard.write("0\n", delay=0.05)
    time.sleep(0.6)

    # Deploy thing
    keyboard.write("Initialization Achieved Successfully!\n\n\n", delay=0.05)
    time.sleep(1.3)
    keyboard.write("Welcome to TAAS, ", delay=0.3)
    time.sleep(0.5)
    keyboard.write("Starting in...\n", delay=0.1)
    for i in reversed(range(0, 6)):
        keyboard.write(f'{i}', delay=1)
        keyboard.press_and_release('backspace')
    time.sleep(0.2)
    keyboard.write(" \n\n\n", delay=0.2)


def settings_salad():
    keyboard.press_and_release('win+i')
 

if __name__ == "__main__":
    input("press ENTER to start...")
    open_app('notepad')
    print("OPEN APP WORKING")
    notepad_initialize()
    print("Notepad Boot Working.")
    # settings_salad()