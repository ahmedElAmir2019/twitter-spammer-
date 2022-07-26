import pyautogui as pag
def random_spammer ():
    import pyautogui as pag , time
    time.sleep(5)
    baby = open("baby", 'r')
    while True:
        for word in baby:
            pag.typewrite(word)
            pag.press("enter")
def non_random_spammer():
    import pyautogui as pag, time
    time.sleep(5)
    baby = open("baby", 'r')
    for i in range (0,11000):
        s ="aash"
        pag.typewrite(s)
        pag.press("enter")

def spammer ():
    y=input("do you want a specific words or not: ")
    if y == "yes" or y=="Yes"or y=="YES"or y=="y"or y=="Y":
        z=input("please enter the word or statment which you want us to spam :")
        non_random_spammer(z)
    else :
        random_spammer()


non_random_spammer()
#non_random_spammer()
#screen_shot=pag.screenshot()
#screen_shot.save("Desktop\\ss.png")
#
#
#
#
#