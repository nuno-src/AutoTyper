import mouse
import keyboard
import time
import random


char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]

words = ["qwe", "qwer", "wreq", "ewrq", "weqr", "asd", "as", "zxc", "xzvc" "asdf", "qw", "qqq", "gfjh", "enytu", "ertyj", "luiuykt",
    "wefyguqjn", "dsds", "gfhghf","sfbthyt","wqef","uyil","dsaf","dghk","asdas","etyj","yuit","jhfk", "jkçl","jklç", "jçkl", "wwww",
    "sadf","hgkj","tyru", "bnm","vbnm", "vbmn", "vcbn", "bnvm","uoiy","uyio"]


# variaveis de tempo
c = 71
m = 82
l = 122
ll = 215


print('''

    _         _        _____
   / \  _   _| |_ ___ |_   __   _ _ __   ___ _ __
  / _ \| | | | __/ _ \  | || | | | '_ \ / _ | '__|
 / ___ | |_| | || (_) | | || |_| | |_) |  __| |
/_/   \_\__,_|\__\___/  |_| \__, | .__/ \___|_|
                            |___/|_|




''')

print("Total words in the list: ", len(words))

print("\nThe Auto Typer is running...")


def countDown(s):
    print(f"Starting typing in {s} seconds...")
    for i in range(s, 0, -1):
        print(i)
        time.sleep(1)


countDown(15)


while True:


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
    print("\nRestarting cycle...")

