import os 

oldPhrase = input("What is the phrase that you would like replaced?: ")
newPhrase = input("What would you like '" + oldPhrase + "' replaced with?: ")

print("-------")
root = input("What is the root folder directory?: ")

for path, subdirs, files in os.walk(root):
    for name in files + subdirs:
        if oldPhrase in name:
            oldPath = os.path.join(path, name)
            newPath = os.path.join(path, name.replace(oldPhrase, newPhrase))
            print("Old:", oldPath)
            print("New:", newPath)
            print("")

confirm = input("Would you like to continue? This cannot be undone (Y/N): ").lower()
if (confirm == "y"):
    print("Renaming")
    for path, subdirs, files in os.walk(root, topdown = False):
        for name in files + subdirs:
            if oldPhrase in name:
                oldPath = os.path.join(path, name)
                newPath = os.path.join(path, name.replace(oldPhrase, newPhrase))
                os.rename(oldPath, newPath)
    print("Rename Complete")
else:
    print("Exiting Program")