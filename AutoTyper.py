import mouse
import keyboard
import time
import random


char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]

words = ["qwe", "qwer", "asd", "as", "zxc", "asdf", "qw", "qqq", "gfjh", "enytu", "ertyj", "luiuykt","wefyguqjn",
 "dsds", "gfhghf","sfbthyt","wqef","uyil","weqr","dsaf","ewrq","zxc","dghk","asdas","etyj","yuit","jhfk"]


# variaveis de tempo
c = 70
m = 82
l = 122
ll = 215


print('''

    _         _        _____
   / \  _   _| |_ ___ |_   __   _ _ __   ___ _ __
  / _ \| | | | __/ _ \  | || | | | '_ \ / _ | '__|
 / ___ | |_| | || (_)   | || |_| | |_) |  __| |
/_/   \_\__,_|\__\___/  |_| \__, | .__/ \___|_|
                            |___/|_|




''')



print("The Auto Typer is running...")

while True:

    time.sleep(15)
    keyboard.write(random.choice(words))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(c)
    keyboard.write("dfghf")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write("qwer")
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
    time.sleep(ll)
    keyboard.write("asd")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write(random.choice(words))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(c)
    keyboard.write(random.choice(char_list))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write(random.sample(char_list, 2))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write("er")
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write(random.choice(words))
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
    print("Restarting cycle...")

