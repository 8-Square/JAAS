import time
import keyboard
import webbrowser

def open_app(app, numdelay: float):
    keyboard.press_and_release('win')
    time.sleep(0.3)
    keyboard.write(f'{app}', delay=numdelay)
    time.sleep(0.6)
    keyboard.press_and_release('enter')
    time.sleep(1.7)

def intermission():
    time.sleep(0.02)
    keyboard.press_and_release('alt+F4')

def custom_loop(key, number: int, stime):
    for i in range(number):
        keyboard.press_and_release(key)
        time.sleep(stime)







def notepad_initialize():
    # keyboard.write("notepad\n", delay=0.05)
    # time.sleep(1.0)
    keyboard.write("JAAS Booting Now...\n\n", delay=0.05)
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

    # START thing
    keyboard.write("Initialization Achieved Successfully!\n\n\n", delay=0.05)
    time.sleep(1.3)
    keyboard.write("Welcome to JAAS, ", delay=0.2)
    time.sleep(0.5)
    keyboard.write("\n\n\nPress Enter To Start or Escape to Quit ", delay=0.09)
    key_pressed = keyboard.read_key()
    if key_pressed == 'escape':
        print("EXITING")
        exit()
    elif key_pressed == 'enter':
        print("ENTERED")
        pass
    time.sleep(0.02)
    keyboard.write("Starting in... \n", delay=0.1)
    time.sleep(0.3)
    for i in reversed(range(1, 6)):
        keyboard.write(f'{i}', delay=1)
        time.sleep(0.01)
        keyboard.press_and_release('backspace')
    keyboard.write("0", delay=0.06)
    time.sleep(0.2)



def scale_changes():
    # Get to the scale setting
    keyboard.press_and_release('shift+tab')
    time.sleep(0.005)
    keyboard.press_and_release('shift+tab, enter')
    time.sleep(0.6)
    # change to x175
    custom_loop('down', 2, 0.007)
    time.sleep(0.002)
    keyboard.press_and_release('enter')

def resolution_changes():
    custom_loop('down', 3, 0.007)
    time.sleep(1.9)
    # open_app('change the resolution of the display', 0.01)
    # keyboard.press_and_release('down, down, down, down, down, down, enter')
    # time.sleep(1.5)
    keyboard.press_and_release('tab, enter')

def display_changes():
    keyboard.press_and_release('tab, tab, tab, enter')
    time.sleep(0.7)
    keyboard.press_and_release('down, down, down, enter')
    time.sleep(1.88)            

    keyboard.press_and_release('tab, enter')


def settings_salad():
    time.sleep(0.02)
    resolution_changes()
    time.sleep(1)
    scale_changes()
    time.sleep(3)
    display_changes()
    time.sleep(0.04)



def magnify():
    time.sleep(0.02)
    keyboard.press_and_release('win+plus')
    time.sleep(0.2)
    custom_loop('win+plus', 6, 0.02)

def inverted():
    time.sleep(0.02)
    custom_loop('ctrl+alt+i', 5, 0.05)
    time.sleep(0.2)
    
def screen_salad():
    time.sleep(0.02)
    magnify()
    time.sleep(1.0)
    inverted()

def aftermath():
    time.sleep(0.02)
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')




if __name__ == "__main__":
    input("press ENTER to start...")
    open_app('notepad', 0.09)
    # print("OPEN APP WORKING")
    notepad_initialize()
    # intermission()
    # print("Notepad Boot Working.")
    # open_app('change the resolution of the display', 0.04)
    # settings_salad()
    # intermission()
    # screen_salad()
    # aftermath()