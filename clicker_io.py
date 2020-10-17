#imports
from colorama import Fore, Style
from tkinter import *
from pynput.keyboard import Listener
import time, multiprocessing
import tkinter as tk


#upgrade variables
Level = 0
upgrade_list = ["McDonalds", "KFC", "Subway"]
upgrades = {upgrade_list[0]:1, upgrade_list[1]:2, upgrade_list[2]:5}
upgrades_cost = {upgrade_list[0]:500, upgrade_list[1]:1500, upgrade_list[2]:5000}
income = upgrades[upgrade_list[Level]]


#variables
cash = 0
num = 0
key = str("")


#info for user
print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}press SPACE to earn\n{Fore.CYAN} [INFO] {Style.RESET_ALL}press ESC to exit\n{Fore.CYAN} [INFO] {Style.RESET_ALL}press TAB to upgrade")


#main class
class main():
    def __init__(self, filename, cash, useless, key):
        global income, upgrade_list, upgrades, Level, upgrades_cost
        self.upgrade_list = upgrade_list
        self.upgrades = upgrades
        self.Level = Level
        self.income = income
        self.filename = filename
        self.cash = cash
        self.key = key
        self.upgrades_cost = upgrades_cost
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
        print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}Current cash: {str(cash)} €")
        
        #####UPGRADES

    def PU(self):
        upgrades_cost = self.upgrades_cost
        income = self.income
        Level = self.Level
        cash = self.cash
        try:
            randvar = upgrades[upgrade_list[Level + 1]]
        except:
            print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}Wait... You already have all upgrades.")
        else:
            if cash >= upgrades_cost[upgrade_list[Level]]:
                print(f"{Fore.GREEN} [TASK] {Style.RESET_ALL}Outgoing transaction...")
                time.sleep(1)
                print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}This transaction cost you: {str(upgrades_cost[upgrade_list[Level]])} €")
                time.sleep(0.5)
                cash -= upgrades_cost[upgrade_list[Level]]
                Level += 1
                income = upgrades[upgrade_list[Level]]
                print(f"{Fore.GREEN} [TASK] {Style.RESET_ALL}Setting your income to: {income} €...")
                time.sleep(0.5)
                print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}You now have {cash} €")
                time.sleep(0.5)
                self.Level = Level
                self.cash = cash
                self.income = income
            else:
                print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}You dont have enought money to buy this. Cost({str(upgrades_cost[upgrade_list[Level]])} €)")

    def Get_cash(self):
        main.File_read(self=self)

    #####KEYS AND THEIR DEFINITIONS

    def press(self, key):
        cash = self.cash
        self.key = key
        income = self.income
        upgrades_cost = self.upgrades_cost

        if key == key.space:
            cash += income
            self.cash = cash
            print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}Your cash: {cash} €")
            time.sleep(0.1)

        elif key == key.esc:
            main.File_write(self=self)
            print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}You now have: {cash} €")
            exit()

        elif key == key.alt_l:
            print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}Upgrade names:money {upgrade_list}, upgrade cost names:cost {upgrades_cost}")

        elif key == key.tab:
            print(f"{Fore.GREEN} [TASK] {Style.RESET_ALL}Searching for better business...")
            time.sleep(1)
            main.PU(self)

        else:
            print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}Sorry, this key ({key}) doesnt do anything")

    def search_by_val(self, val):
        for shop in self.upgrade_list:
            if val == self.names[shop]:
                return shop

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


#main in variable
Keys = main(filename="clicker_io", cash=cash, key=key, useless=None)


#just for fun
def Main(bookshelf):
    print(bookshelf)

if __name__ == 'main':
    Main(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}This is BOOKSHELF")


#listener join
Keys.Listener_join()
