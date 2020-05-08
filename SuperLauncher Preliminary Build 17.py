import time
import pickle
import os
from os import path
test = os.path.exists(r'C:\Users\Public\SuperLauncher')
if(test == True):
    print("Verified Filesystem!")
    os.chdir(r'C:\Users\Public\SuperLauncher')
    menuloop = True
    while(menuloop == True):
        menu = input("Menu:")
        if(menu == "add profile"):
            print("Add Profile selected")
            time.sleep(0.5)
            profilenam = input("Profile Name?:")
            location = input("Location?:")
            filename = input("File?:")
            lnf = [location, filename]
            profilename = profilenam + ".sl"
            pickle.dump(lnf, open(profilename, "wb"))
        elif(menu == "load profile"):
            print("Load Profile selected")
            time.sleep(0.5)
            profilenam = input("Profile Name?:")
            profilename = profilenam + ".sl"
            test2 = path.exists(profilename)
            if(test2 == True):
                load = pickle.load(open(profilename, "rb"))
                location = load[0]
                filename = load[1]
                print(load)
                load2 = location + filename
                cd = "cd\ "
                os.system(cd)
                os.system("start " + load2)
            else:
                print("Whoops! This file doesn't exist, or you spelt it wrong.")
        elif(menu == "changelog"):
            print("Changelog:")
            print("PB17: Fixed an exiting bug existing since PB05. Serious bruh.")
            print("PB16: Fixing a bug in the way it launches files. (line 33)")
            print("PB15: Added starting of files. Most likely the end of Preliminary Builds. (line 33)")
            print("PB14: Loading now no longer has an error. (line 26)")
            print("PB13: Loading profiles now works correctly. (line 24)")
            print("PB12: Fixed filename not being saved")
            print("PB11: removed unnessesary text")
            print("PB10: Fixed wrong dir bug. (line 18)")
            print("PB09: Added .sl filetype. (line 17)")
            print("PB08: Added Verification code. (line 4)")
            print("PB07: Added code to save file (line 14)")
            print("PB06: Added OS import (line 3), changed timing, and variables (line 10)")
            print("PB05: Added axit to menuloop (Line 19)")
            print("PB04: Added menuloop")
            print("PB03: Changed text.")
            print("PB02: Added Pickle import, Added changelog.")
            time.sleep(3)
        elif(menu == "exit"):
            menuloop = False
            print("Goodbye!")
            time.sleep(2)
        else:
            print("Sorry, Invalid!")
            time.sleep(3)
else:
    print("Your SuperLauncher directory is missing! Run the installer first!")
    exit()
