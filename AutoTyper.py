import mouse
import keyboard
import time
import random


char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]

words = ["asd", "as","asdf", "qwe", "qwer", "wreq", "ewrq", "weqr", "qw", "qqq", "gfjh", "enytu", "ertyj", "luiuykt",
    "wefyguqjn", "dsds", "gfhghf","sfbthyt","wqef","uyil","dsaf","dghk","asdas","etyj","yuit","jhfk", "jkçl","jklç", "jçkl", "wwww",
    "sadf","hgkj","hjkg", "tyru", "bnm","vbnm", "vbmn", "vcbn", "bnvm","uoiy","uyio","xzvc", "zxc"]



# variaveis de tempo
c = 71
m = 82
l = 122
ll = 215



# Verificar duplicados na lista words
uwords = []

for i in words:
    if i not in uwords:
        uwords.append(i)
    





print('''

    _         _        _____
   / \  _   _| |_ ___ |_   __   _ _ __   ___ _ __
  / _ \| | | | __/ _ \  | || | | | '_ \ / _ | '__|
 / ___ | |_| | || (_) | | || |_| | |_) |  __| |
/_/   \_\__,_|\__\___/  |_| \__, | .__/ \___|_|
                            |___/|_|




''')

print("Total words in the list: ", len(words))
print("Duplicate words found: ", len(words)-len(uwords))
print("\nThe Auto Typer is running...")



def random_printing():
    r = random.choice(words)
    print(f"printing {r} in 3 seconds...")
    time.sleep(3)
    keyboard.write(r)
    time.sleep(1)
    keyboard.press("Enter")


def static_printing(word):
    print(f"printing {word} in 3 seconds...")
    time.sleep(3)
    keyboard.write(word)
    time.sleep(1)
    keyboard.press("Enter")


def countDown(s):
    print(f"Starting typing in {s} seconds...")
    for i in range(s, 0, -1):
        print(i)
        time.sleep(1)


countDown(15)


while True:


    random_printing()
    time.sleep(c)
    static_printing("dfghf")
    time.sleep(m)
    static_printing("qwer")
    time.sleep(m)
    static_printing("qw")
    time.sleep(l)
    static_printing("qw")
    time.sleep(ll)
    static_printing("asd")
    time.sleep(m)
    random_printing()
    time.sleep(c)
    keyboard.write(random.choice(char_list))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    keyboard.write(random.sample(char_list, 2))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(m)
    static_printing("er")
    time.sleep(m)
    random_printing()
    time.sleep(c)
    static_printing("as")
    time.sleep(c)
    keyboard.write(random.choice(char_list))
    time.sleep(1)
    keyboard.press("Enter")
    time.sleep(62)
    print("\nRestarting cycle...")

