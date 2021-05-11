import os

dir = os.popen("dir").readlines()
print("Current Directory: ", dir)
print("---Khiem's Shell---")
path =input("Enter your home directory: ")
os.chdir(path)
cmd = ""
command = " "
while (command != "exit"):
    command = input(">> ")
    cmdr = os.popen(command)
    line = " "
    while line:
        line = cmdr.read()
        print(line)
    cmdr.close()
print("---Shell Closed---")


