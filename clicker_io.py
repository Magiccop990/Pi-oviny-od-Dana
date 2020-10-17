#imports
from colorama import Fore, Style
from tkinter import *
from pynput.keyboard import Listener
import time, multiprocessing
import tkinter as tk



#upgrade variables
Level = 0
upgrade_list = [
    "McDonalds",
    "KFC",
    "Subway",
    "Nay",
    "Datart",
    "Alza",
    "Panta Rey",
    "Brloh"
    ]

Level_list = {
    upgrade_list[0]:1,
    upgrade_list[1]:2, 
    upgrade_list[2]:3, 
    upgrade_list[3]:4, 
    upgrade_list[4]:5, 
    upgrade_list[5]:6, 
    upgrade_list[6]:7, 
    upgrade_list[7]:8
    }

upgrades = {
    upgrade_list[0]:1,
    upgrade_list[1]:2, 
    upgrade_list[2]:5, 
    upgrade_list[3]:25, 
    upgrade_list[4]:100, 
    upgrade_list[5]:500, 
    upgrade_list[6]:1500, 
    upgrade_list[7]:5000
    }

upgrades_cost = {
    upgrade_list[0]:500, 
    upgrade_list[1]:1500, 
    upgrade_list[2]:5000, 
    upgrade_list[3]:15000, 
    upgrade_list[4]:50000, 
    upgrade_list[5]:500000, 
    upgrade_list[6]:1000000, 
    upgrade_list[7]:1000000000
    }

income = upgrades[upgrade_list[Level]]
shop = None

#variables
cash = 0
num = 0
key = str("")
number = 0


#info for user
print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}press SPACE to earn\n{Fore.CYAN} [INFO] {Style.RESET_ALL}press ESC to exit\n{Fore.CYAN} [INFO] {Style.RESET_ALL}press TAB to upgrade\n{Fore.CYAN} [INFO] {Style.RESET_ALL}press CTRL to reset")


#main class
class main():
    def __init__(self, filename, filename2, cash, useless, key):
        global income, upgrade_list, upgrades, Level, upgrades_cost, shop, Level_list, number
        self.upgrade_list = upgrade_list
        self.upgrades = upgrades
        self.Level = Level
        self.income = income
        self.filename = filename
        self.cash = cash
        self.key = key
        self.upgrades_cost = upgrades_cost
        self.shop = shop
        self.filename2 = filename2
        self.Level_list = Level_list
        self.number = number
        main.Get_cash(self)

    #####FILE
        
    def File_write(self):
        cash = self.cash
        #cash
        filename = self.filename
        self.file_write = open(filename+".txt", "w")
        self.file_write.write(str(cash))
        self.file_write.close
        #shop
        shop = self.shop
        filename2 = self.filename2
        self.file_write2 = open(filename2 + ".txt", "w")
        try:
            self.file_write2.write(shop)
            self.file_write2.close()
        except:
            self.file_write2.write("")
            self.file_write2.close()
        else:
            pass

    def File_read(self):
        income = self.income
        cash = self.cash
        shop = self.shop
        Level_list = self.Level_list
        #cash
        filename = self.filename
        self.file_o = open(filename+".txt", "r")
        cash = int(self.file_o.readline())
        self.file_o.close()
        self.cash = cash
        print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}Current cash: {str(cash)} €")
        #shop
        filename2 = self.filename2
        self.file_s = open(filename2 + ".txt", "r")
        shop = str(self.file_s.readline())
        if shop != "":
            self.file_s.close()
            self.shop = shop
            print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}You own: {str(shop)}")
            Level = Level_list[shop]
            income = upgrades[upgrade_list[Level]]
            self.income = income
            print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}Your income is: {income} €")
            self.Level = Level
            self.shop = shop
        else:
            pass

        
        #####UPGRADES

    def PU(self):
        upgrades_cost = self.upgrades_cost
        income = self.income
        Level = self.Level
        cash = self.cash
        try:
            randvar = upgrades[upgrade_list[Level + 1]]
        except:
            print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}Wait... You already have all upgrades.")
        else:
            if cash >= upgrades_cost[upgrade_list[Level]]:
                print(f"{Fore.GREEN} [TASK] {Style.RESET_ALL}Outgoing transaction...")
                time.sleep(1)
                print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}This transaction cost you: {str(upgrades_cost[upgrade_list[Level]])} €")
                time.sleep(0.5)
                shop = main.search_by_val(self, upgrades_cost[upgrade_list[Level]])
                print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}You now own {shop}")
                time.sleep(0.5)
                cash -= upgrades_cost[upgrade_list[Level]]
                Level += 1
                income = upgrades[upgrade_list[Level]]
                print(f"{Fore.GREEN} [TASK] {Style.RESET_ALL}Setting your income to: {income} €...")
                time.sleep(0.5)
                print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}You now have {cash} €")
                time.sleep(0.5)
                self.Level = Level
                self.cash = cash
                self.income = income
                self.shop = shop
            else:
                print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}You dont have enought money to buy this. Cost({str(upgrades_cost[upgrade_list[Level]])} €)")

    def Get_cash(self):
        main.File_read(self=self)

    #####KEYS AND THEIR DEFINITIONS

    def press(self, key):
        cash = self.cash
        self.key = key
        upgrades_cost = self.upgrades_cost

        if key == key.space:
            cash += self.income
            self.cash = cash
            print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}Your cash: {cash} €")
            time.sleep(0.1)

        elif key == key.esc:
            main.File_write(self=self)
            print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}You now have: {cash} €")
            exit()

        elif key == key.alt_l:
            print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}Upgrade names:money {upgrade_list}, upgrade cost names:cost {upgrades_cost}")

        elif key == key.tab:
            print(f"{Fore.GREEN} [TASK] {Style.RESET_ALL}Searching for better business...")
            time.sleep(1)
            main.PU(self)

        elif key == key.ctrl_l:
            main.Reset(self)

        else:
            print(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}Sorry, this key ({key}) doesnt do anything")

    def search_by_val(self, val):
        for ky in self.upgrades_cost:
            if val == self.upgrades_cost[ky]:
                return ky

    def Reset(self):
        filename = self.filename
        filename2 = self.filename2
        file1 = open(filename2 + ".txt", "w")
        file1.write("")
        file1.close()
        file2 = open(filename + ".txt", "w")
        file2.write("0")
        file2.close()
        print(f"{Fore.CYAN} [INFO] {Style.RESET_ALL}Reseted")
        exit()

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
Keys = main(filename="clicker_cash", filename2="clicker_shop", cash=cash, key=key, useless=None)


#just for fun
def Main(bookshelf):
    print(bookshelf)

if __name__ == 'main':
    Main(f"{Fore.RED} [CASHIER] {Style.RESET_ALL}This is BOOKSHELF")


#listener join
Keys.Listener_join()
#just to get it to 240
