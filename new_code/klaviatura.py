import pyautogui
from pynput import keyboard
import py_win_keyboard_layout
import time
import klaviatura
import ctypes
from keyboard import press_and_release
from time import sleep
import pyautogui, pyperclip
from pynput import mouse 


def paste(text: str):    
    pyperclip.copy(text)
    press_and_release('ctrl + v')


def typePs(text: str, interval=0.0):    
    buffer = pyperclip.paste()
    if not interval:
        paste(text)
    else:
        for char in text:
            paste(char)
            sleep(interval)
    pyperclip.copy(buffer)

def active():
       list = []
       with open("comands.txt", "r", encoding='utf-8') as my_file: 
              while True:
                     line = my_file.readline() #читает линии
                     if not line:
                            break
                     # print(line.strip())
                     list.append(line.strip())
       for i in range(len(list)):
            if str(list[i][0]) == 'x':
                    s1=list[i].replace("x", "")
                    b = s1.split()
                    b = ''.join(b)
                    ls = (b.split(","))
                    # print((ls[0]),(ls[1]))
                    pyautogui.moveTo(int(ls[0]),int(ls[1]),0.8)
            elif str(list[i][0]) == 'c':
                    pyautogui.click()
            elif str(list[i][0]) == 'R':
                    pyautogui.mouseDown(button='right')
            elif str(list[i][0]) == 'd':
                    # print(list[i])
                    s1=list[i].replace("dx", "")
                    b = s1.split()
                    b = ''.join(b)
                    s2=b.replace("x", "")
                    # part1,part2 = s2.split('/')
                    parts = s2.split(';')
                    part1, part2 = parts[0], parts[1]
                    ls2 = (part2.split(",")),(part1.split(","))
                    # print(ls2)
                    anws = int(ls2[0][0])-int(ls2[1][0]),int(ls2[0][1])-int(ls2[1][1])
                    pyautogui.drag(anws,duration=0.9),time.sleep(1)
            elif str(list[i][0]) == 't' and str(list[i][1]) == ';':
                    s1=list[i].replace("t;", "")
                    typePs(s1 + '\n', 0.2)
            elif str(list[i][0]) == 's' and str(list[i][1]) == ':':
                    s1=list[i].replace("s:", "")
                    s1=s1.replace("Key.", "").replace("_l", "")
                    st = s1
                    st = st.split(',')
                    print(len(st))
                    for i in range(len(st)):
                            print(st[i])
                            if st[i] == 'f3':
                                 pyautogui.click()
                            if st[i][0] == 'x':
                                s=st[i].replace("x:", "")
                                x1 = (s.partition(';')[0])
                                x2 = (s.partition(';')[2])
                                pyautogui.moveTo(int(x1),int(x2),0.8)
                            else: 
                                print(st[i])
                                pyautogui.keyDown(f'{st[i]}')

            elif str(list[i][0]) == 'n' and str(list[i][1]) == ':':
                    s1=list[i].replace("n:", "")
                    Slist = (s1.split(','))
                    for i in range(len(Slist)):
                            if len(Slist[i]) > 0:
                                    print(Slist[i])
                                    if Slist[i] == 'vverh':
                                            pyautogui.scroll(125)
                                    if Slist[i] == 'vniz':
                                            pyautogui.scroll(-125)
            elif str(list[i][0]) == 'p':
                    s1=list[i].replace("p", "")
                    pause = int(s1[i][0])
                    time.sleep(pause)
            else:
                    print('1')
            

def rus():
    layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                           "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))

    pyautogui.hotkey("shift", "alt")
    list = []
    def on_press(key):
        try:
            list.append((f"{key.char}"))
        except AttributeError:
            list.append(f"{key}")

    def on_release(key):
        if key == keyboard.Key.f3:
            mass = []
            for i in range(len(list)):
                if len(list[i]) > 2:
                    pass
                if list[i] == 'Key.space':
                    mass.append(' ')
                if len(list[i]) == 1:
                    mass.append(list[i].translate(layout))
            mass = (''.join(mass)) 
            with open("comands.txt", "a", encoding='utf-8') as my_file:
                print(len(mass))
                if len(mass) > 1:
                    my_file.write('t;' + mass + '\n')
            return False

    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
    pyautogui.hotkey("shift", "alt")



# # time.sleep(1)
def eng():
    time.sleep(1)
    list = []
    def on_press(key):
        try:
            list.append((f"{key.char}"))
                # print(x1)
        except AttributeError:
                # x2 = f"{key}"
            list.append(f"{key}")
            # print(x2)

    def on_release(key):
        # print(f'{key} released')
        if key == keyboard.Key.f2:
            mass = []
            for i in range(len(list)):
                if len(list[i]) > 2:
                    # mass.append(list[i])
                    # print(list[i])
                    pass
                if list[i] == 'Key.space':
                    mass.append(' ')
                if len(list[i]) == 1:
                    mass.append(list[i])
            mass = (''.join(mass)) 
            with open("comands.txt", "a", encoding='utf-8') as my_file:
                # print(list)
                # print(mass[i])
                print(len(mass))
                if len(mass) > 1:
                    my_file.write('t;' + mass + '\n')


            return False
    # # x = []
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()



def specK():
    time.sleep(1)
    list = []
    def on_press(key):
        try:
            list.append((f"{key.char}"))
                # print(x1)
        except AttributeError:
                # x2 = f"{key}"
            list.append(f"{key}")
            # print(x2)

    def on_release(key):
        # print(f'{key} released')
        if key == keyboard.Key.f4:
            mass = []
            for i in range(len(list)):
                if len(list[i]) > 2:
                    if list[i] != 'Key.f4':
                        mass.append(list[i])
                if list[i] == 'Key.space':
                    mass.append(' ')
                if len(list[i]) == 1:      
                        mass.append(list[i])


            mass = (','.join(mass)) 
            with open("comands.txt", "a", encoding='utf-8') as my_file:
                print(len(mass))
                if len(mass) > 1:
                    my_file.write('s:' + mass + '\n')


            return False
    # # x = []
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

def scroll():
    xlist = []
    def on_click(x, y, button, pressed):
    # print(f"{'Nazhato' if pressed else 'Otpuscheno'} na {(x, y)}")
        pass
        if not pressed:
            return False 

    def on_scroll(x, y, dx, dy):
    # print(f"Procrucheno {'vniz' if dy < 0 else 'vverh'} na {(x, y)}")
        xP = 'vniz' if dy < 0 else 'vverh'
        xlist.append(xP)
    with mouse.Listener(on_click = on_click, on_scroll = on_scroll) as listener: 
        listener.join()
    with open("comands.txt", "a", encoding='utf-8') as my_file:
                if len(xlist) > 1:
                    my_file.write('n:') 
                    for i in range(len(xlist)):
                        my_file.write(str(xlist[i]+','))
                    time.sleep(1)
                    my_file.write('\n')




def coord():
        x, y = pyautogui.position()
        positionStr = 'x:'+ str(x).rjust(4) +';'+str(y).rjust(4)
        time.sleep(0.01)
        return(positionStr)

def specKM():

    time.sleep(1)
    list = []
    def on_press(key):
        try:
            list.append((f"{key.char}"))
                # print(x1)
        except AttributeError:
                # x2 = f"{key}"
            list.append(f"{key}")
            # print(x2)

    def on_release(key):
        mass = []
        x = coord()

        if key == keyboard.Key.f4:

            for i in range(len(list)):
                if len(list[i]) > 2:
                    if list[i] != 'Key.f4':

                        mass.append(list[i])
                if list[i] == 'Key.space':
                    mass.append(' ')
                if list[i] == 'Key.f2':
                    mass.append(x)
                if len(list[i]) == 1:
                        mass.append(list[i])



            mass = (','.join(mass)) 
            with open("comands.txt", "a", encoding='utf-8') as my_file:
                print((mass))
                my_str2 = mass.replace('Key.f2', f'{x}')
                if len(mass) > 1:
                    my_file.write('s:' + my_str2 + '\n')


            return False
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
