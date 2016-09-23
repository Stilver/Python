import os
import telnetlib
from ftp.func import f

os.chdir("C:/Users/Work/Desktop")

octt = True                     #responsible for exit
filename = f.get_file()         #gets file containing ip
address = f.read_file(filename) #reads file and takes ip


while octt:
    #cleaning window and imitating simple menu
    os.system("cls")
    print ("\nCurrent ftp-address is %s" % address)
    print ("\n------------------------------------------------")
    print ("#CHANGING:")
    print ("    1) to change address")
    print ("    2) to change the last octet\n")
    print ("#PING:")
    print ("    3) to ping current address")
    print ("    4) to ping MASTER")
    print ("    5) to ping SLAVE\n")
    print ("#FTP:")
    print ("    6) to enter ftp-server via local address\n")
    print ("#TELNET:")
    print ("    7) to connect to MASTER")
    print ("    71) to connect to MASTER 1.1.10.1")
    print ("    8) to connect to SLAVE")
    print ("    9) to connect to a current address\n")
    print ("#IP CONFIGURATION:")
    print ("    10) for ipconfig")
    print ("    11) for dhcp")
    print ("    12) for 10.10.10.3 with gateway 10.10.10.1")
    print ("    121) for 10.10.10.3 with gateway 10.10.10.31\n")
    print ("    122) for 1.1.10.254 with gateway 1.1.10.31")
    print ("    123) for 1.1.10.254 with gateway 1.1.10.1\n")
    print ("#EXTRA:")
    print ("    13) to ROCK!")
    print ("    14) to open sup_doc")
    print ("    15) to open q.txt") 
    print ("    Enter anythin else to input into cmd")
    print ("    'q' to quit\n")
    
    #user input and converting into number
    choise = input(" > ")
    rawchoise = choise
    choise = f.convert_number(choise)
    
    #decisions
    if choise == 1:
        print ("\nInput your address")
        tempaddr = input("> ")
        temp = tempaddr.split(".")
        
        if len(temp) != 4:
            inp = input ("bad input")
        else:
            address = tempaddr
            f.change_content(address)
        
    elif choise == 2:
        print ("\nInput your last octet")
        octet = input("> ")
        address = address.split(".")
        address = address[0]+"."+address[1]+"."+address[2]+"."+octet
        f.change_content(address)
        inp = input ("...")
        
    elif choise == 3 or rawchoise == "3 -t":
        f.ping(address, rawchoise)
            
    elif choise == 4 or rawchoise == "4 -t":
        pingip = "10.10.10.1"
        f.ping(pingip, rawchoise)
            
    elif choise == 5 or rawchoise == "5 -t":
        pingip = "10.10.10.2"
        f.ping(pingip, rawchoise)
    
    elif choise == 6:
        f.ftp(address)
                
    elif choise == 7:
        f.telnet("10.10.10.1")
        
    elif choise == 71:
        f.telnet("1.1.10.1")
            
    elif choise == 8:
        f.telnet("10.10.10.2")
            
    elif choise == 9:
        f.telnet(address)
        
    elif choise == 10:
        os.system("cls")
        os.system("ipconfig")
        inp = input ("...")
        
    elif choise == 11:
        os.system("cls")
        os.system('netsh interface ip set address name="Ethernet" source=dhcp')
        os.system("ipconfig")
        inp = input ("...")
        
    elif choise == 12:
        os.system("cls")
        os.system('netsh interface ip set address name="Ethernet" static 10.10.10.3 255.255.255.0 10.10.10.1')        
        os.system("ipconfig")
        inp = input ("...")
        
    elif choise == 121:
        os.system("cls")
        os.system('netsh interface ip set address name="Ethernet" static 10.10.10.3 255.255.255.0 10.10.10.31')        
        os.system("ipconfig")
        inp = input ("...")
        
    elif choise == 122:
        os.system("cls")
        os.system('netsh interface ip set address name="Ethernet" static 1.1.10.254 255.255.255.0 1.1.10.31')        
        os.system("ipconfig")
        inp = input ("...")
        
    elif choise == 123:
        os.system("cls")
        os.system('netsh interface ip set address name="Ethernet" static 1.1.10.254 255.255.255.0 1.1.10.1')        
        os.system("ipconfig")
        inp = input ("...")
        
    elif choise == 13:
        os.system('start "" "c:\Program Files (x86)\AIMP\AIMP.exe"')
    
    elif choise == 14:
        os.system('start sup_doc.docx')
        
    elif choise == 15:
        os.system('start q.txt')
        
    elif rawchoise == 'q' or rawchoise == 'Q':
        octt = False
    
    else:
        os.system('cls')
        try:
            os.system(rawchoise)
        except KeyboardInterrupt:
            octt = True
        inp = input("\b\b...")
