#The EnDa Image Resizer's source code

#Import needed modules
from Tools.SaveFile import *
from Tools.Essentials import *

#Create needed values
value = random.randint(1,4)
path = pathlib.Path(__file__).parent.resolve()

#Create a start-up
clearConsole()
space()
os.system("title EnDa Image Resizer - EnDaTeam")
banner(value)
print(Fore.YELLOW + "[*]" + Fore.CYAN + " Welcome to EnDa Image Resizer!")
if os.path.isdir('Images') != 1:
    space()
    error("The folder 'Images' does not exist! Creating a new one...")
    os.makedirs("Images")
    space()
    print(Fore.LIGHTYELLOW_EX + "[TIP] >> " + "The folder is empty, we are leaving the program!")
    print(Fore.LIGHTYELLOW_EX + "[TIP] >> " + "Please put some images to modify them in the folder!" + Fore.WHITE)
    space()
    time.sleep(5)
    exit()
path2 = os.path.join(path, "Images")
directory = os.listdir(path2)
if len(directory) == 0:
    space()
    error("The folder 'Images' is empty!")
    space()
    print(Fore.LIGHTYELLOW_EX + "[TIP] >> " + "The folder is empty, we are leaving the program!")
    print(Fore.LIGHTYELLOW_EX + "[TIP] >> " + "Please put some images to modify them in the folder!" + Fore.WHITE)
    space()
    time.sleep(5)
    exit()
else:
    fileSelecting = 1
    while fileSelecting:
        space()
        print(Fore.WHITE + f"There are {Fore.RED}{len(directory)}{Fore.WHITE} files in folder!")
        print(Fore.LIGHTYELLOW_EX + "[TIP] >> Is there are less selected that means that that them can't be used to resize!")
        count = 0
        space()
        fileNames = []
        for i in directory:
            if i.split(".")[-1] in ("png","jpg","jpeg","gif"):
                count = count + 1
                print(Fore.CYAN + f"File{count} is : " + str(i))
                fileNames.append(i)
        space()
        print(Fore.WHITE + "[*] The files are ok?")
        filereverify = input("Yes or No ? : ")
        if str(filereverify).lower() in ("y","yes","yeah"):
            space()
            print(Fore.GREEN + "[*] Great! Now the next step..." + Fore.WHITE)
            fileSelecting = 0
        else:
            space()
            print(Fore.RED + "[*] We are sorry about it, re-verifying...")
            continue
space()
optionsChoice = 1
imageResizing = 1
while imageResizing:
    while optionsChoice:
        print(Fore.CYAN + "[*] Please select an option from the list!")
        space()
        options()
        space()
        option = input(Fore.WHITE + "Option : ")
        try:
            int(option)
        except:
            space()
            error("The inputed option is not avaible!")
            space()
            continue
        if int(option) not in (1,2,3,9,0):
            pass 
        else:
            optionsChoice = 0
    space()
    print(Fore.LIGHTYELLOW_EX + "[TIP] >> Please use the OPTIONS.txt file to guide you.")
    if os.path.isfile('Options.txt') != 1:
        createfileandsave()
    if int(option) == 1:
        temp = 1
        while temp:
            space()
            print(Fore.LIGHTYELLOW_EX + "[*] Please input the size to resize the images!!")
            space()
            width = input(Fore.WHITE + "Width > ")
            try:
                int(width)
            except:
                space()
                error("The inputed width is not avaible! Must be an integer.")
            else:
                temp = 0
        temp1 = 1
        while temp1:
            space()
            print(Fore.LIGHTYELLOW_EX + "[*] Great, now input the height!")
            space()
            height = input(Fore.WHITE + "Height > ")
            space()
            try:
                int(height)
            except:
                error("The inputed height is not avaible! Must be an integer.")
            else:
                temp1 = 0
        sizeImage = (int(width),int(height))
        for i in fileNames:
            try:
                image = Image.open(r"Images\\" + i)
                new_image = image.resize(sizeImage)
                string1 = i.split(".")
                string2 = string1[:-1]
                for i in string2:
                    string3 = i
                string = str(string3) + str(width) + "x" + str(height) + ".png"
                new_image.save(r"Images\\" + str(string),"PNG")
                print(Fore.GREEN + f"[SUCCESS] >> {i} was succesfully resized and saved as {string}!")
            except:
                error(f"Something went wrong about {i}!")
        space()
    elif int(option) == 2:
        temp = 1
        while temp:
            print(Fore.LIGHTYELLOW_EX + "[TIP] >> This is a BETA version! Can be errors about it!")
            space()
            print(Fore.LIGHTYELLOW_EX + "[*] Please input the size to resize the images!!")
            space()
            width = input(Fore.WHITE + "Width > ")
            try:
                int(width)
            except:
                space()
                error("The inputed width is not avaible! Must be an integer.")
            else:
                temp = 0
        temp1 = 1
        while temp1:
            space()
            print(Fore.LIGHTYELLOW_EX + "[*] Great, now input the height!")
            space()
            height = input(Fore.WHITE + "Height > ")
            space()
            try:
                int(height)
            except:
                error("The inputed height is not avaible! Must be an integer.")
            else:
                temp1 = 0
        sizeImage = (int(width),int(height))
        for i in fileNames:
            try:
                image = Image.open(r"Images\\" + i)
                image.thumbnail(sizeImage)
                string1 = i.split(".")
                string2 = string1[:-1]
                for i in string2:
                    string3 = i
                string = str(string3) + str(width) + "x" + str(height) + ".png"
                saveLocation = r"Images/" + str(string)
                image.save(str(saveLocation),"PNG")
                print(Fore.GREEN + f"[SUCCESS] >> {i} was succesfully resized and saved as {string}!")
            except:
                error(f"Something went wrong about {i}!")
        space()
    elif int(option) == 3:
        space()
        print(Fore.LIGHTYELLOW_EX + "[*] Great, here are the informations for every image!")
        space()
        for i in fileNames:
            Img = Image.open("Images/" + i)
            print(Fore.WHITE + "Image Filename  >> ",Fore.CYAN ,Img.filename)
            print(Fore.WHITE + "Image Format  >> ",Fore.MAGENTA,Img.format)
            print(Fore.WHITE + "Image Mode  >> ",Fore.BLUE,Img.mode)
            print(Fore.WHITE + "Image Width  >> ",Fore.GREEN,Img.width)
            print(Fore.WHITE + "Image Height  >> ",Fore.GREEN,Img.height)
            print(Fore.WHITE + "Image Final Size  >> ",Fore.LIGHTRED_EX,Img.size,Fore.WHITE)
            space()
    elif int(option) == 0 or int(option) == 9:
        print(Fore.BLUE + "[*] Roger, thank you for using EnDa Image Resizer!")
        time.sleep(3)
        exit()
    print(Fore.RED + "[*] Do you want to do another operation?")
    continues = input(Fore.WHITE + "(Y)es or (N)o > ")
    space()
    if str(continues).lower() not in ("yes","y","yeah","yy"):
        print(Fore.BLUE + "[*] Thank you for using EnDa Image Resizer!" + Fore.WHITE)
        time.sleep(3)
        exit()
    else:
        optionsChoice = 1
        continue
