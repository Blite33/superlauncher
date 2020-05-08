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
        if menu in("add profile", "addprofile", "ap", "add"):
            print("Add Profile selected.")
            time.sleep(0.5)
            profilenam = input("Profile Name?:")
            location = input("Location of starter file?:")
            filename = input("Filename?:")
            lnf = [location, filename]
            profilename = profilenam + ".sl"
            pickle.dump(lnf, open(profilename, "wb"))
        elif menu in("load profile", "loadprofile", "lp", "load"):
            print("Load Profile selected.")
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
        elif menu in("list", "list profile", "list profiles", "listprofile", "listprofiles"):
            dir_name = r'C:\Users\Public\Superlauncher'
            extension = ".sl"
            pathList = []
            pathList = findFilesInFolder(dir_name, pathList, extension, True)
            print(pathList)
        elif menu in("changelog", "cl"):
            print("Changelog:")
            print("Build 5 (v1.1.1): Added some extra cases.")
            print("Build 4 (v1.1): Added help")
            print("Build 3 (v1.0.2): Added some extra cases.")
            print("Build 2 (v1.0.1): Switched around some text.")
            print("Build 1 (v1.0): Added a list profile function.")
            time.sleep(3)
        elif menu in("exit", "stop", "escape"):
            menuloop = False
            print("Goodbye, thanks for using! -Blite33")
            time.sleep(2)
        elif menu in("help"):
            print("add profile, addprofile, ap, add")
            print("load profile, loadprofile, lp, load")
            print("list, list profile, list profiles, listprofile, listprofiles")
            print("changelog, cl")
            print("exit, stop, escape")
            print("help")
        else:
            print("Sorry, invalid input!")
            time.sleep(3)
else:
    print("Your SuperLauncher directory is missing! Run the installer first!")
    exit()
