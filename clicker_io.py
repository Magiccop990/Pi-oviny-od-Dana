from tkinter import *
from pynput.keyboard import Listener
import time


print("press SPACE to earn")
cash = 0

class File():
    def filename_get(self, filename):
        self.filename = filename
    def File_write(self):
        money = self.money
        filename = self.filename
        file_write = open(filename+".txt", "w")
        file_write.write(str(money))
        file_write.close
    def File_read(self):
        global cash
        filename = self.filename
        file_read = open(filename+".txt", "r")
        cash = int(file_read.readline())
        print("Current cash: " + str(cash))
        file_read.close()


class Keys_get():
    def Get_cash(self, useless):
        File.filename_get(self=self, filename="clicker_io")
        File.File_read(self=self)
    def press(self, key, money):
        global cash
        self.money = money
        self.key = key
        #print(f"Pressed: {key}")
        if key == key.space:
            print("cash +1")
            cash += 1
            #print(cash)
        elif key == key.esc:
            File.File_write(self=self)
            print(f"You now have {cash} €")
            exit()
    def release(self, key):
        pass
    def on_press(self, key):
        global cash
        Keys_get.press(self=self, key=key, money=cash)
    def on_release(self, key):
        Keys_get.release(self=self, key=key)


Keys = Keys_get()
Keys.Get_cash(useless=None)




with Listener(on_press=Keys.on_press, on_release=Keys.on_release) as listener:
    listener.join()
