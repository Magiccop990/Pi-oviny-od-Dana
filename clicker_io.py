from tkinter import *
from pynput.keyboard import Listener
import time
import tkinter as tk


print("press SPACE to earn")
cash = 0

class File(file):
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

class Window(ui):
    def __init__(self):
        cash = self.money
        win = Tk()
        win.title("CLICKER.IO")
        win.geometry("200x100")
        main_label = Label(win, text=cash, width=5)
        main_label.place(x=90,y=10)
        main_frame = LabelFrame(win, width=5, height=2)
        main_frame.place(x=90, y=10)
        
    def main_update(self):
        cash = self.money
        main_label.configurate(text=cash)


class Keys(listener_commands):
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
            Window.main_update(self)
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


Keys.Get_cash(useless=None)




with Listener(on_press=Keys.on_press, on_release=Keys.on_release) as listener:
    listener.join()
