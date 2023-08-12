import pyautogui as auto
from time import sleep
import keyboard

def CheckForBattle(): 
    book = auto.locateOnScreen("img/book.png", confidence=0.7, grayscale=True)
    if (book):
        print("not in battle, waiting...")
        sleep(2)
        return False
    else:
        return True

def checkSlot():
    slot2 = auto.locateOnScreen("img/slot2.png", confidence= 0.7, grayscale=True)
    if (slot2):
        return True
    else:
        return False

def PassRound():
    passbutton = auto.locateOnScreen("img/pass.png", confidence= 0.9, grayscale=True)

    if (passbutton):
        button = auto.center(passbutton)
        auto.click(button)
        sleep(0.2)
        auto.click(button)
        print("passing")
        

def SelectSpell():
    spell = auto.locateOnScreen("img/unenchanted.png", confidence= 0.7, grayscale=True)

    if (spell):
        button = auto.center(spell)
        auto.click(button)
        sleep(0.1)
        auto.click(button)
        auto.move(0,200)
        CastSpell()

def SelectEnchant():
    enchant = auto.locateOnScreen("img/enchant.png", confidence= 0.7, grayscale=True)
    if (enchant):
        auto.move(0,300, duration=1)
        sleep(0.5)
    if (enchant):
        button = auto.center(enchant)
        auto.click(button)
        sleep(0.1)
        auto.click(button)
        sleep(0.3)
        auto.move(0,200)
        SelectSpell()

    CheckForBattle()
    sleep(3)

def CastSpell():
    enchanted = auto.locateOnScreen("img/enchanted.png", confidence= 0.7, grayscale=True)

    if (enchanted):
        button = auto.center(enchanted)
        auto.click(button)
        sleep(0.2)
        auto.click(button)
        print("casting")

def Wander():
    with auto.hold("D"):
        auto.sleep(2)

def CheckMana():
        mana = auto.locateOnScreen("img/mana.png", confidence=0.9, grayscale=True)
        potion = auto.locateOnScreen("img/potion.png", confidence=0.9, grayscale=True)

        if (mana):
            print("need mana")
            if (potion):
                button = auto.center(potion)
                auto.click(button)
                sleep(0.2)
                auto.click(button)
                auto.move(0,200)
                sleep(0.2)

                emptypotions = auto.locateOnScreen("img/emptypotions.png", confidence=0.7, grayscale=True)

                if (emptypotions): 
                    getPotions()

def getPotions():
        marklocation = auto.locateOnScreen("img/marklocation.png", confidence=0.9, grayscale=True)
        if (marklocation):
            button = auto.center(marklocation)
            auto.click(button)
            sleep(0.2)
            auto.click(button)
        home = auto.locateOnScreen("img/home.png", confidence=0.7, grayscale=True)
        if (home):
            button = auto.center(home)
            auto.click(button)
            sleep(0.2)
            auto.click(button)
            sleep(5)
            with auto.hold("S"):
                auto.sleep(2)
            sleep(5)
            with auto.hold("W"):
                auto.sleep(1)
            with auto.hold("D"):
                auto.sleep(0.6)
            with auto.hold("W"):
                auto.sleep(4.5)
            with auto.hold("D"):
                auto.sleep(0.3)
            with auto.hold("W"):
                auto.sleep(2.5)
            auto.sleep(0.5)
            auto.press('x')
            auto.sleep(0.5)
            
            allpotions = auto.locateOnScreen("img/fillpotions.png", confidence=0.9, grayscale=True)
            auto.sleep(0.5)
            if (allpotions):
                button = auto.center(allpotions)
                auto.click(button)
                sleep(0.2)
                auto.click(button)

                buy = auto.locateOnScreen("img/buy.png", confidence=0.7, grayscale=True)
                auto.sleep(0.5)
                if (buy):
                    button = auto.center(buy)
                    auto.click(button)
                    sleep(0.2)
                    auto.click(button)
                    
                    close = auto.locateOnScreen("img/close.png", confidence=0.7, grayscale=True)
                    if (close):
                        button = auto.center(close)
                        auto.click(button)
                        sleep(0.2)
                        auto.click(button)
                        sleep(0.2)
                        
                        teleportmark = auto.locateOnScreen("img/teleportmark.png", confidence=0.9, grayscale=True)
                        if (teleportmark):
                            button = auto.center(teleportmark)
                            sleep(0.2)
                            auto.click(button)
                            sleep(0.3)
                            auto.click(button)
                                     
def main():
    print("starting the autofarm, change windows now")
    while True:
        print("checking for battle")
        battle = CheckForBattle()
        if (battle):
            print("battle started")
            slot2 = checkSlot()
            if slot2:
                SelectEnchant()
            else:
                PassRound()
                
        else:
            ("print wandering")
            Wander()
            CheckMana()
            CheckForBattle()
            
main()

