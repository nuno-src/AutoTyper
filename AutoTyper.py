import mouse
import keyboard
import time
import random


char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]

c = 68
m = 75
l = 120



while True:

    time.sleep(15)
    keyboard.write(random.choice(char_list))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write(random.sample(char_list, 2))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write("qwert")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write("qw")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(l)
    keyboard.write("qw")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write("e")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write("as")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(c)
    keyboard.write("as")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(c)
    keyboard.write(random.choice(char_list))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(50)

