import mouse
import keyboard
import time
import random

test_list = ["asd","qwe", "zxc"]

char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]

words = ["asd", "as","asdf", "qwe", "qwer", "wreq", "ewrq", "weqr", "qw", "qqq", "gfjh", "enytu", "ertyj", "luiuykt",
    "wefyguqjn", "dsds", "gfhghf","sfbthyt","wqef","uyil","dsaf","dghk","asdas","etyj","yuit","jhfk", "jkçl","jklç", "jçkl", "jkçhçkjlk",
    "çkljhjççjkl", "wwww", "sadf","hgkj","hjkg", "tyru", "bnm","vbnm", "vbmn", "vcbn", "bnvm","uoiy","uyio","xzvc", "zxc"]

words2 = ["gfhghf", "hgkj","hjkg", "jkhl", "khjl", "jklçj", "lkçlçj", "jhfk", "jkçl","jklç", "jçkl","klkj", "jkçhlkj", "kljççlk", "jkçhçkjlk", "kjlçlkºj","hgjlkçl", "hkjçlkjhkj",
    "çkljhjççjkl", "fxgjxhddh", "bnvmv", "bnm", "vbnm", "vbmn", "vcbn", "bnvm","vnbmnbv", "kjlççkljº","jljkºllçk", "jklçklj", "kjlçkjl", "klçlj",
    "bmnvvm", "mnbv", "jklçjklç", "hgjkgkljh", "jhkll","kjlºjk", "kjlçjklç", "lkçjlçlkj", "hlkhkjçkl", "ljllç", "khjlºç", "jlkhçl",
    "çklklºç", "klçkjºlç", "kçlº", "kljçjkl", "çlkjjçlj", "lkçjlçjlçj", "kjhhkjlk", "kljçkjl", "kkjlçjkl", "kjlçjkl","klçjjçklç",
    "kjlçk", "kçjhhç", "jljllkç", "kjçj", "jhklh", "kljçjklk", "klçkjçjklçgjljk", "kjhgkljçjgjhl", "kjlçhjk", "vnbmnnbv", "jhkkjhllhj",
    "jkhlhjlk", "jklçlkj", "jklkhlkhl", "kljçjklç", "jlkçkjçj", "kjçkjlçkjçkj", "jhklhjklh", "jhjkjkh", "ghjkg"]

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
    
    
uwords2 = []
for w in words2:
    if w not in uwords2:
        uwords2.append(w)




print('''

    _         _        _____
   / \  _   _| |_ ___ |_   __   _ _ __   ___ _ __
  / _ \| | | | __/ _ \  | || | | | '_ \ / _ | '__|
 / ___ | |_| | || (_) | | || |_| | |_) |  __| |
/_/   \_\__,_|\__\___/  |_| \__, | .__/ \___|_|
                            |___/|_|




''')


print("\nThe Auto Typer is running...")


used_words = []

def random_printing(list):
    while True:
        try:
            r = random.choice(list)
            if r not in used_words:
                print(f"printing {r} in 5 seconds...")
                time.sleep(5)
                keyboard.write(r)
                time.sleep(1)
                keyboard.press("Enter")
                used_words.append(r)
                break
        except:
            pass





def static_printing(word):
    print(f"printing {word} in 5 seconds...")
    time.sleep(5)
    keyboard.write(word)
    time.sleep(1)
    keyboard.press("Enter")


def countDown(s):
    print(f"Starting typing in {s} seconds...")
    for i in range(s, 0, -1):
        print(i)
        time.sleep(1)



def test():

    while True:
        random_printing(test_list)
        time.sleep(5)
        random_printing(test_list)
        time.sleep(5)
        random_printing(test_list)
        used_words.clear()
        time.sleep(5)
        random_printing(test_list)
        time.sleep(5)
        random_printing(test_list)
        used_words.clear()


def o1():

    while True:

        random_printing(words)
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
        random_printing(words)
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
        random_printing(words)
        time.sleep(c)
        static_printing("as")
        time.sleep(c)
        keyboard.write(random.choice(char_list))
        time.sleep(1)
        keyboard.press("Enter")
        time.sleep(62)
        print("\nRestarting cycle...")




def o2():

    while True:
    
        random_printing(uwords2)
        time.sleep(c)
        random_printing(uwords2)
        time.sleep(m)
        random_printing(uwords2)
        time.sleep(m)
        random_printing(uwords2)
        time.sleep(l)
        random_printing(uwords2)
        time.sleep(ll)
        random_printing(uwords2)
        time.sleep(m)
        random_printing(uwords2)
        time.sleep(m)
        random_printing(uwords2)
        time.sleep(m)
        random_printing(uwords2)
        time.sleep(m)
        random_printing(uwords2)
        time.sleep(c)
        random_printing(uwords2)
        time.sleep(c)
        random_printing(uwords2)
        time.sleep(l)
        random_printing(uwords2)
        time.sleep(m)
        random_printing(uwords2)
        time.sleep(65)
        print("\nRestarting cycle...")
        used_words.clear()


if __name__ == '__main__':

    opc = ""
    while opc != "exit":


        print("\n===================================================")
        print("                     Choose an option")
        print("===================================================")
        print("  [1] - option 1 ")
        print("  [2] - option 2 (recomended)")
        print("  [exit]")
        print("===================================================")


        opc = input("Choose an option: ")

        if opc == "1":
            print("Total words in the list: ", len(words))
            print("Duplicate words found: ", len(words)-len(uwords))
            countDown(15)
            o1()
        elif opc == "2":
            print("Total words in the list: ", len(words2))
            print("Duplicate words found: ", len(words2)-len(uwords2))
            countDown(15)
            o2()
        elif opc == "3":
            test()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")
            
            