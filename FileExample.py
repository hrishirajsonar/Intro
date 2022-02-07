import os

try:
    file = open("C:\\Users\hrish\Desktop\\intents.json","r")
    try:
        for i in range(4):
            print(file.readline())

        for lines in file.readlines():
            print(lines)
    except:
        print("Error while reading from the file")
except:
    print("Error while opening the file")
else:
    print("This will be executed if  no error is raised ")
finally:
    #file.close()
    print('This will be executed no matter what')

try:
    import os
    os.remove("C:\\Users\hrish\Desktop\\runs.txt") #no recycle bin
    os.rmdir("myFolder") #removes directory
except:
    print("Error importing os")
else:
    print("Executed if no error")
finally:
    print("This is also printed anyway")