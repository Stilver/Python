from tkinter import *
import os
import time
import threading
import getpass
import telnetlib

class Butn:
    def __init__(self, width, text, command):
        self.but = Button(root, command = lambda: threading.Thread(target = self.printer).start())
        # self.but = Button(root)          
        self.but["width"] = width
        self.but["text"] = text 
        # self.but.bind("<Button-1>", self.printer)         
        self.command = command        

    def printer(self): #add event in case of unithreading
        os.system("cls")
        try:
            os.system(self.command)
        except KeyboardInterrupt:
            print("")   
            
class Ipconf:
    def __init__(self, width, text, command):
        self.but = Button(root, command = lambda: threading.Thread(target = self.printing).start())   
        self.but["width"] = width
        self.but["text"] = text     
        self.command = command        

    def printing(self): #add event in case of unithreading
        os.system("cls")
        os.system(self.command)

class ButEnt:
    def __init__(self):
        # self.but = Button(root)
        self.but = Button(root, command = lambda: threading.Thread(target = self.printerr).start())
        self.but["text"] = "execute!"
        # self.but.bind("<Button-1>", self.printerr)

    def printerr(self): #add event in case of unithreading
        os.system("cls")
        comand = ent.get()
        try:
            os.system(comand)
        except KeyboardInterrupt:
            print("") 

root = Tk()
root.title("COOLTOOL")
root.wm_geometry("+%d+%d" % (800, 200))
#Buttons
master = Butn(20, "MASTER 10.10.10.1", "telnet 10.10.10.1")
slave = Butn(20, "SLAVE 10.10.10.2", "telnet 10.10.10.2")
master2 = Butn(20, "MASTER 1.1.10.1", "telnet 1.1.10.1")
slave2 = Butn(20, "SLAVE 1.1.20.2", "telnet 1.1.20.2") 
switch = Butn(42, "SWITCH 10.1.30.10", "telnet 10.1.30.10")
centos = Butn(42, "CENTOS 10.10.10.127", "telnet 10.10.10.127")

ipconf = Ipconf(42, "IPCONFIG", "ipconfig")

MS = Butn(42, "10.10.10.3", 'netsh interface ip set address name="Ethernet" static 10.10.10.3 255.255.255.0 10.10.10.31')  
NMS = Butn(20, "1.1.10.11; 1.1.10.1", 'netsh interface ip set address name="Ethernet" static 1.1.10.11 255.255.255.0 1.1.10.1')  
NMSS = Butn(20, "1.1.10.11; 1.1.10.31", 'netsh interface ip set address name="Ethernet" static 1.1.10.11 255.255.255.0 1.1.10.31')  
switchnetsh = Butn(42, "10.1.30.11", 'netsh interface ip set address name="Ethernet" static 10.1.30.11 255.255.255.0 10.1.30.254')  
dhcp = Butn(42, "DHCP", 'netsh interface ip set address name="Ethernet" source=dhcp')

masterp1 = Butn(20, "ping 10.10.10.1", "ping 10.10.10.1")
slavep1 = Butn(20, "ping 10.10.10.2", "ping 10.10.10.2")
masterp2 = Butn(20, "ping 1.1.10.1", "ping 1.1.10.1")
slavep2 = Butn(20, "ping 1.1.20.2", "ping 1.1.20.2")

# entry via Enter
def entr(self):
    exc = ent.get()
    os.system(exc)
    
ent = Entry(root, width=50, bd=3)
ent.bind("<Return>",entr)

# Class ButEnt
execut = ButEnt()

#Grid
lab = Label(root, text="devices:", font="Arial 10")
lab.grid(row=0, column=0, columnspan=2)
master.but.grid(row=1, column=0)
slave.but.grid(row=1, column=1)
master2.but.grid(row=2, column=0)
slave2.but.grid(row=2, column=1)
switch.but.grid(row=3, column=0, columnspan=2)
centos.but.grid(row=4, column=0, columnspan=2)

lab1 = Label(root, text="ipconfig:", font="Arial 10")
lab1.grid(row=5, column=0, columnspan=2)
ipconf.but.grid(row=6, column=0, columnspan=2)

lab1 = Label(root, text="PC configurations (IP;G):", font="Arial 10")
lab1.grid(row=7, column=0, columnspan=2)
MS.but.grid(row=8, column=0, columnspan=2)
NMS.but.grid(row=9, column=0)
NMSS.but.grid(row=9, column=1)
switchnetsh.but.grid(row=10, column=0, columnspan=2)
dhcp.but.grid(row=11, column=0, columnspan=2)

lab1 = Label(root, text="ping:", font="Arial 10")
lab1.grid(row=12, column=0, columnspan=2)
masterp1.but.grid(row=13, column=0)
slavep1.but.grid(row=13, column=1)
masterp2.but.grid(row=14, column=0)
slavep2.but.grid(row=14, column=1)

lab1 = Label(root, text="type your command here:", font="Arial 10")
lab1.grid(row=15, column=0, columnspan=2)
ent.grid(row=16, column=0, columnspan=2)
execut.but.grid(row=17, column=0, columnspan=2)

root.mainloop()