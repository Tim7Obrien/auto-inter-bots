import win32gui
 
HLD = win32gui. FindWindow (None, u "'League of Legends (TM) Client") # Returns the handle of the window titled Adobe Acrobat
print(HLD)
