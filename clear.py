import os
#when you run the cls() function the python console will clear
def cls():
    #if you run os.system(cls) on windows the screen will clear
    #and if you run os.system(clear) on linux and mac it will clear
    #so the code checks what os you are using and enters clear or cls accordingly
    os.system('cls' if os.name=='nt' else 'clear')


print("stuff so much random stuff")
print("more stuff to remove!")
input("just press enter to clear")
cls()
input("how cool!")

#NOTE DOES NOT WORK WITH PYCHARM CONSOLE
#I don't know why but if you run it with terminal it will work.