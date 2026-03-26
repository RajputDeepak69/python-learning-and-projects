# there is always a module for frequently done tasks ...
import os as o


folders = input( "provide list of folder names:").split()

#now using loop to automate repeatative listing hehehehehe ...
for folder in folders:
    # okh, let's play with exception handelling too 
    try:
         files = o.listdir(folder)
    except FileNotFoundError:
        print("bhai is name ka koi folder nhi hai", folder)
        continue
    print("These are files and folders inside:", folder)

    for file in files:
        print(file)


