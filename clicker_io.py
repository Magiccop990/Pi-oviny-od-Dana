from tkinter import *
from pynput.keyboard import Listener
import time, multiprocessing
import tkinter as tk


#upgrade variables
Level = 0
upgrade_list = ["McDonalds", "KFC", "Subway"]
upgrades = {upgrade_list[0]:1, upgrade_list[1]:2, upgrade_list[2]:5}
income = upgrades[upgrade_list[Level]]

#variables
cash = 0
num = 0
key = str("")

#info
print("press SPACE to earn\npress ESC to exit\npress CTRL to upgrade")


#main class
class main():
    def __init__(self, filename, cash, useless, key):
        global income, upgrade_list, upgrades, Level
        self.upgrade_list = upgrade_list
        self.upgrades = upgrades
        self.Level = Level
        self.income = income
        self.filename = filename
        self.cash = cash
        self.key = key
        main.Get_cash(self)

    #####FILE
        
    def File_write(self):
        cash = self.cash
        filename = self.filename
        self.file_write = open(filename+".txt", "w")
        self.file_write.write(str(cash))
        self.file_write.close

    def File_read(self):
        cash = self.cash
        filename = self.filename
        self.file_o = open(filename+".txt", "r")
        cash = int(self.file_o.readline())
        self.file_o.close()
        self.cash = cash
        print("Current cash: " + str(cash))
        
        #window

    def Windower(self):
        cash = self.cash
        upgrade_list = self.upgrade_list
        upgrades = self.upgrades
        Level = self.Level
        #return 


    def Get_cash(self):
        main.File_read(self=self)

    #####KEYS AND THEIR DEFINITIONS

    def press(self, key):
        cash = self.cash
        self.key = key
        income = self.income

        if key == key.space:
            cash += income
            self.cash = cash
            print(f"Your cash: {cash} €")
            time.sleep(0.1)

        elif key == key.esc:
            main.File_write(self=self)
            print(f"You now have: {cash} €")
            exit()

        elif key == key.ctrl_l:
            main.Windower(self)

    def release(self, key):
        income = self.income

    def on_press(self, key):
        cash = self.cash
        main.press(self=self, key=key)

    def on_release(self, key):
        main.release(self=self, key=key)

    def Listener_join(self):
        with Listener(on_press=Keys.on_press, on_release=Keys.on_release) as listener:
            listener.join()


Keys = main(filename="clicker_io", cash=cash, key=key, useless=None)

"""
if __name__ == 'main':
    Main()"""

Keys.Listener_join()
