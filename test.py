from tkinter import *
import os

# --------------------------------------------------------------
class ButEnt:
    def __init__(self):
        self.but = Button(root)
        self.but = Button(root, command = lambda: threading.Thread(target = self.printerr).start())
        self.but["text"] = "execute!"
        self.but.bind("<Button-1>", self.printerr)

    def printerr(self): #add event in case of unithreading
        os.system("cls")
        comand = ent.get()
        try:
            os.system(comand)
        except KeyboardInterrupt:
            print("") 
            
def entr(self):
    exc = ent.get()
    os.system(exc)
    # temp = sys.stdout
    # tex.insert(INSERT, temp)

root = Tk()

ent = Entry(root, width=54, bd=3)
ent.bind("<Return>", entr)

tex = Text(root,width=31,
           font="Verdana 12",
           wrap=WORD) 
           
scr = Scrollbar(root, orient=VERTICAL, command=tex.yview)
tex.configure(yscrollcommand=scr.set)

tex.grid(row=0, column=0)
scr.grid(row=0, column=1, ipady = 190)
ent.grid(row=1, column=0, columnspan = 2)

root.mainloop()

# ------------------------------------------------------------

# from tkinter import *

# def whilefunc1():
    # n = 1
    # while (n <= 100000):
        # print(n)
        # n = n + 1

# def whilefunc2():
    # n = 100001
    # while (n <= 200000):
        # print(n)
        # n = n + 1

# root = Tk()
# root.geometry("200x200")

# but1 = Button(root, text="press me", command = lambda: threading.Thread(target = whilefunc1).start())
# but1.pack()
# but2 = Button(root, text="me 2!!", command = lambda: threading.Thread(target = whilefunc2).start())
# but2.pack()

# root.mainloop()

# --------------------------------------------------------------

# import getpass
# import telnetlib

# HOST = "10.10.10.127"
# user = "work"
# password = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until(b"login: ")
# tn.write(user.encode('ascii') + b"\n")
# if password:
    # tn.read_until(b"Password: ")
    # tn.write(password.encode('ascii') + b"\n")

# tn.mt_interact()