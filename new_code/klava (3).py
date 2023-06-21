
from pynput import mouse
import keyboard
import pyautogui
import time
pyautogui.PAUSE = 0.5

import klaviatura

time.sleep(0.5)


while True:
       if keyboard.is_pressed('f2'):
              print('Раздел "манипулятор"')
              time.sleep(1)
              while True:
                     x, y = pyautogui.position()
                     positionStr = 'x'+ str(x).rjust(4) +','+str(y).rjust(4)
                     time.sleep(0.2)
                     with open("comands.txt", "a", encoding='utf-8') as my_file:
                                   if keyboard.is_pressed('f2'):
                                          my_file.write(f'{positionStr}' + '\n'),time.sleep(1)
                                          print(f'Нажата f2 на {positionStr}, координаты записаны')
                                   elif  keyboard.is_pressed('f3'):
                                          my_file.write('cliced' + '\n'),time.sleep(1)
                                          print(f"Нажата f3 на {positionStr}, клик левой кнопкой мыши")
                                   elif  keyboard.is_pressed('f10'):
                                          my_file.write('Rcliced' + '\n'),time.sleep(1)
                                          print(f"Нажата f10 на {positionStr}, клик правой кнопкой мыши")
                                   elif keyboard.is_pressed('f5'):
                                          my_file.write('d'+positionStr+';'),time.sleep(1) 
                                          print(f"Нажата f5, переместите курсор в следующую точку и нажмите f2")
                                   elif keyboard.is_pressed('f6'):
                                          print(f"Нажата f6, прокрутка колесика мыши")
                                          klaviatura.scroll()
                                   elif keyboard.is_pressed('f12') or keyboard.is_pressed('f11'):
                                          print('Выход из раздела "мышь"')
                                          time.sleep(1)
                                          break
                                   elif keyboard.is_pressed('f4'):
                                          klaviatura.specKM()
                                   elif keyboard.is_pressed('f7'):
                                          my_file.write('p2' + '\n'),time.sleep(1)
                                          print("Нажата f7, пауза при воспроизведении составит 2 секунды")
                                   elif keyboard.is_pressed('f8'):
                                          my_file.write('p3' + '\n'),time.sleep(1)
                                          print("Нажата f8, пауза при воспроизведении составит 3 секунды")
                                   elif keyboard.is_pressed('f9'):
                                          my_file.write('p4' + '\n'),time.sleep(1)
                                          print("Нажата f9, пауза при воспроизведении составит 4 секунды")
       elif keyboard.is_pressed('f3'):
              time.sleep(1)
              print('Раздел "клавиатура"')
              while True:
                     with open("comands.txt", "a", encoding='utf-8') as my_file:
                                   if keyboard.is_pressed('f2'):
                                          print("Нажата f2, ввод на английском языке")
                                          klaviatura.eng()
                                          time.sleep(1)
                                   elif keyboard.is_pressed('f3'):
                                          print("Нажата f3, ввод на русском языке")
                                          klaviatura.rus()
                                          time.sleep(1)
                                   elif keyboard.is_pressed('f4'):
                                          print("Нажата f4, работа со специальными клавишами")
                                          klaviatura.specK()
                                   elif keyboard.is_pressed('f12') or keyboard.is_pressed('f11'):
                                          print('Выход из раздела "клавиатура"')
                                          time.sleep(1)
                                          break
                                   elif keyboard.is_pressed('f7'):
                                          my_file.write('p2' '\n'),time.sleep(1)
                                          print("Нажата f7, пауза при воспроизведении составит 2 секунды")
                                   elif keyboard.is_pressed('f8'):
                                          my_file.write('p3' + '\n'),time.sleep(1)
                                          print("Нажата f8, пауза при воспроизведении составит 3 секунды")
                                   elif keyboard.is_pressed('f9'):
                                          my_file.write('p4' + '\n'),time.sleep(1)
                                          print("Нажата f9, пауза при воспроизведении составит 4 секунды")
                                   elif keyboard.is_pressed('f10'):
                                          pass
                                          # print(pause)
       elif  keyboard.is_pressed('f12') or keyboard.is_pressed('f11'): 
              print('Выход из программы')
              break 
       elif keyboard.is_pressed('f9'): #
              with open("comands.txt", "w") as my_file:
                     print('Очистка файла'),time.sleep(2)
       elif keyboard.is_pressed('f10'):
              print("Воспроизведение сценария")
              time.sleep(1)
              klaviatura.active()
              
