#IMPORTS
import speech_recognition as sr
from tkinter import *
import os, time, datetime, pyttsx3, speedtest, webbrowser
from pynput.keyboard import Key, Controller

#WINDOW
win = Tk()
win.title("Speech Recognition")
win.geometry("150x60")
win.wm_attributes("-alpha", 1)

#VARIABLES
num = 0
a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
g = ""
keyboard = Controller()

#SPEAKING
engine = pyttsx3.init()

#INTERNET SPEED DEF
def internetspeedtest():
        print("Calculating...\nPlease wait...")
        test = speedtest.Speedtest()
        download = test.download()
        upload = test.upload() 
        up = upload/1024
        do = download/1024
        upl = up/1024
        dow = do/1024
        print(f"Download Speed :  {dow} Mbps")
        print(f"Upload Speed : {upl} Mbps")


#DEFINITIONS
def SR():
        global text
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Spech now: ")
                audio = r.listen(source=source) 
                p = r.recognize_google(audio)
                print(p)
                text = list(p.split())
                print(text)
                words()

def SRU(useless):
        SR()

def listtostr():
        global a, b, c, d, e, f, g, text, Z

        num = len(text)
        Q = " "
        if num>=1:
                a = str(text[0])
        if num>=2:
                b = str(text[1])
        if num>=3:
                c = str(text[2])
        if num>=4:
                d = str(text[3])
        if num>=5:
                e = str(text[4])
        if num>=6:
                f = str(text[5])
        if num>=7:
                g = str(text[6])

        Z = a + Q + b + Q + c + Q + d + Q + e + Q + f + Q + g

        print(Z)

def makeButSR():
        buttonSR = Button(win, text="Recognize Speech", command=SR, height=5, width=20)
        buttonSR.grid(row=0, column=0)
        buttonSR.pack()


def deleteStart():
        button1.pack_forget()
        makeButSR()


#BUTTON
button1 = Button(win, text="Start", command=deleteStart, height=5, width=20)
button1.grid(row=0, column=0)
button1.pack()

#WORDS
def words():
        global text
        if "shut" in text:
                if "down" in text:
                        if "yourself" in text:
                                print("Alexa is shuting down...")
                                engine.say("Ok. Alexa is shuting down...")
                                engine.runAndWait()
                                win.destroy()
                                exit()
        if "shut" in text:
                if "down" in text:
                        if "PC" in text:
                                engine.say("Ok. Your PC is shuting down...")
                                engine.runAndWait()
                                os.system("shutdown /s /t 1")
        elif "internet" in text:
                if "speed" in text:
                        internetspeedtest()
        elif "web" in text:
                if "browser" in text:
                        if "open" in text:
                                num=text.index("open")
                                num+=1
                                urlS=text[num]
                                url="www." + urlS + ".sk"
                                print(f"URL {url} opening...")
                                engine.say(f"URL {url} is opening...")
                                engine.runAndWait()
                                webbrowser.open(url)
        elif "say" in text:
                num=text.index("say")
                while num!=-1:
                        del text[num]
                        num-=1
                listtostr()
                engine.say(Z)
                engine.runAndWait()
        elif "control" in text:
                num=text.index("control")
                while num!=-1:
                        del text[num]
                        num-=1
                engine.say("Ok.")
                engine.runAndWait()
                listtostr()
                keyboard.type(Z)
        elif "thanks" in text:
                engine.say("No Problem ")
                print("No Problem :)")
                engine.runAndWait()
        elif "WhatsApp" in text:
                engine.say("Ok, but some things you havo to enter manualy...")
                engine.runAndWait()
                import whatsapp
        elif "alarm" in text:
                engine.say("Ok, but some things you havo to enter manualy...")
                engine.runAndWait()
                import ALARM


win.bind_all("<Return>", SRU)
win.mainloop()
