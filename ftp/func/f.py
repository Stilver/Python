import os
import sys
import telnetlib
import time
import getpass

#converts string into integer
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

#connects to a ftp using local ip and login.txt file
def ftpconnection(ftp):
    try:
        print ("\nTryin to connect to ftp-server...\n")
        os.system(ftp)
    except KeyboardInterrupt:
        print ("\b\bno can do")
        octt = True
    inp = input("\b\b...")

#ECHO-request
def ping(address, tcheck):
    os.system("cls")
    ping = "ping " + address
    des = tcheck.split()
    try:
        if des[1]:
            try:
                ping = ping + " " + des[1]
                os.system(ping)
            except KeyboardInterrupt:
                octt = True
    except IndexError:
        try:
            os.system(ping)        
        except KeyboardInterrupt:
            octt = True
    inp = input("\b\b...")

#remote control via telnet    
def telnet(address):
    os.system("cls")
    telnet = "telnet " + address
    os.system(telnet)
    print ("\b\b")

# Creates command for ftp connection and also copying sup_doc.docx file
# to put it into ftp-server
def ftp(address):
    os.system("cls")
    inp = input ("\nWould you like to put your sup_doc.docx? [y\\n]\n\n> ")
    
    if inp == 'y':
        ftp = "ftp -s:login.txt -i " + address
        os.system('copy sup_doc.docx "ftp/sup_doc.docx"')
        os.chdir("ftp")
        print ("\nBefore putting in ftp:\n------------------------------------------------")
        os.system("dir /b")
        ftpconnection(ftp)
        print ("\nAfter putting in ftp:\n------------------------------------------------")
        os.system("del sup_doc.docx")
        os.system("dir /b")
        os.chdir("..")
        
    else:
        os.chdir("ftp")
        ftp = "ftp -s:loginnoput.txt -i " + address
        ftpconnection(ftp)
        os.chdir("..")

#gets file containing local ip
def get_file():
    return 'ftp/ip.txt'

#reads file containing local ip
def read_file(filename):
    file = open(filename)
    address = file.read()
    file.close()
    return address

#changes local ip
def change_content(address):
    filename = get_file()
    file = open(filename, 'w')
    file.write(address)
    file.close()