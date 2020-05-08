import time
import pickle
import os
from os import path
test = os.path.exists(r'C:\Users\Public\SuperLauncher')
if(test == True):
    print("Verified Filesystem!")
    def findFilesInFolder(path, pathList, extension, subFolders = True):
        try:
            for entry in os.scandir(path):
                if entry.is_file() and entry.path.endswith(extension):
                    pathList.append(entry.path)
                elif entry.is_dir() and subFolders:
                    pathList = findFilesInFolder(entry.path, pathList, extension, subFolders)
        except OSError:
            print('Cannot access ' + path +'. Probably a permissions error')
        return pathList
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
        elif(menu == "list"):
            dir_name = r'C:\Users\Public\Superlauncher'
            extension = ".sl"
            pathList = []
            pathList = findFilesInFolder(dir_name, pathList, extension, True)
            print(pathList)
        elif(menu == "changelog"):
            print("Changelog:")
            print("Build 1: Added a list profile function.")
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
