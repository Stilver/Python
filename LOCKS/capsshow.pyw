#! "C:\Program Files\Python35\python.exe"

import win32api #contains winAPI functions
import win32gui #contains winGUI functions
import win32con #contains Windows' constants
import winerror #contains Windows' error handlers
import sys, os
import time
from threading import *

time.sleep(15)

class MainWindow:
    def __init__(self):
        self.CLstate = win32api.GetAsyncKeyState(win32con.VK_CAPITAL)
        self.path = r'd:\Coding\Python\Programs\LOCKS\Caps'
        
        msg_TaskbarRestart = win32gui.RegisterWindowMessage("Taskbar"); # registers a new unique window

        message_map = {                                         # dict containing functions, that will
                msg_TaskbarRestart: self.OnRestart,             # be used in this tray program every function recieves 
                win32con.WM_DESTROY: self.OnDestroy,            # self, hwnd, msg, wparam, lparam on call.
                win32con.WM_USER+20 : self.OnTaskbarNotify,     # for use by private window classes
        }

        # Register the Window class.
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32api.GetModuleHandle(None)       # returns a 'None' handle to the instance 
                                                                      # that contains the window procedure for the class.
        wc.lpszClassName = "TaskbarScreenBrghtnss"                  # specifies the window class name (!)
        wc.lpfnWndProc = message_map                                # (!) connects functions to window

        try:                                                  # registering a class window and check 
            classAtom = win32gui.RegisterClass(wc)            # if it is already exists
        except win32gui.error as err_info:
            if err_info.winerror != winerror.ERROR_CLASS_ALREADY_EXISTS:
                raise

        # Create the Window
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU       # configuration window's style

        # creates window and returns handle (probably)
        self.hwnd = win32gui.CreateWindow(classAtom, "Brghtns", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
                
        # updates current Windows GUI, giving handle of a new GUI-element
        win32gui.UpdateWindow(self.hwnd)
        
        # Hides a console window
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_HIDE)

        # calls function that deply an icon on the tray       
        self._DoCreateIcons()
        
    def _DoCreateIcons(self):
        hinst = win32api.GetModuleHandle(None)           
        iconPathName = os.path.join(self.path, 'CapsOFF.ico') # set path to a tray icon        
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            
        #checks if a choosen path contains an icon
        try:
            hicon = win32gui.LoadImage(hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        
        # sets some flags
        flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP
        
        # creates tuple, consisting of 
        # 1) our program's window's handler
        # 2) zero (?)
        # 3) our flags
        # 4) WM_USER constant + 20
        # 5) handle of loaded icon
        # 6) Name of tray icon when mouse pointing on it
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "Kick Ass Prog")
        
        try:
            # implements our settings and sets (win32gui.NIM_ADD)
            # our window (nid)in tray
            win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
        except win32gui.error:
            # This is common when windows is starting, and this code is hit
            # before the taskbar has been created.
            print("Failed to add the taskbar icon - is explorer running?")
            # but keep running anyway - when explorer starts, we get the
            # TaskbarCreated message.
        
        Thread(target = self.show_Caps_state).start()
        
    def show_Caps_state(self):
        while self.CLstate == win32api.GetKeyState(win32con.VK_CAPITAL):
            time.sleep(1)           
        else:
            if self.CLstate == -1:
                return  
            if win32api.GetKeyState(win32con.VK_CAPITAL) == 1:
                iconPathName = os.path.join(self.path, 'CapsON.ico')
                self.CLstate = 1
            else:
                iconPathName = os.path.join(self.path, 'CapsOFF.ico')
                self.CLstate = 0
                
            hinst = win32api.GetModuleHandle(None)
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            hicon = win32gui.LoadImage(hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
            flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP
            nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon)        
            win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, nid)
            
        self.show_Caps_state()
            
        
    # function, needed for viewing our icon on a sudden restart of the Windows' GUI
    # (I guess)
    def OnRestart(self, hwnd, msg, wparam, lparam):
        self._DoCreateIcons()        
    
    # function, implementing some setting on destroying our icon
    def OnDestroy(self, hwnd, msg, wparam, lparam):       
        nid = (self.hwnd, 0) #tuple of our window's handle and zero(?)        
        # implements our settings and deletes (win32gui.NIM_DELETE)
        # our window (nid)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)        
        win32gui.PostQuitMessage(0) # Terminate the app.
        self.CLstate = -1
    
    def OnTaskbarNotify(self, hwnd, msg, wparam, lparam):
        if lparam == win32con.WM_LBUTTONDBLCLK:
            print("Goodbye")
            win32gui.DestroyWindow(self.hwnd)
        return 1

def main():
    w = MainWindow()        #class, creating window
    win32gui.PumpMessages() #runs the program until a WM_QUIT message is recieved
    
if __name__=='__main__':
    main()
    
# a useful link:
# See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winui/menus_0hdi.asp