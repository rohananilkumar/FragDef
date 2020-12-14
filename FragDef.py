import os

def mysort(l):
    rlist=[]
    files={}
    for i in l:
        files[int(i.split()[-1])]=i
    for i in sorted(files):
        rlist.append(files[i])
    return rlist
   

def frag(path,number):
    try:
        with open(path,"rb") as file_:
            data=file_.read()
            file_.seek(0)
            folderpath=path.replace(path.split("\\")[-1],"")
            vol=int(len(data)/number)  
            filename=path.split('\\')[-1]
            if f"Fragmented Data {filename.replace('.','_')}" not in os.listdir(folderpath):
                os.makedirs(folderpath+"\\"+f"Fragmented Data {filename.replace('.','_')}")
            del data
            for i in range(number):
                with open(folderpath+"\\"+f"Fragmented Data {filename.replace('.','_')}"+"\\"+filename+"vol "+str(i),"wb") as newfile:
                    newfile.write(file_.read(vol))
            return folderpath+"\\"+f"Fragmented Data {filename.replace('.','_')}"
    except:
        raise FileNotFoundError("The requested file could not be found")

def defrag(path):
    try:
        files=os.listdir(path)
        files=[x for x in files if "vol " in x]

        files=mysort(files)

        if "Defragmented File" not in os.listdir(path):
            os.makedirs(path+"\\"+"Defragmented File")
        open(path+"\\Defragmented File\\"+files[0].replace("vol 0",""),"w+").close()
        with open(path+"\\Defragmented File\\"+files[0].replace("vol 0",""), "ab") as file:
            for i in files:
                print(f"Stitching file : {i}")
                with open(path+"\\"+i,"rb") as rfile:
                    file.write(rfile.read())
        return path+"\\"+"Defragmented File"
    except:
        raise FileNotFoundError("The requested file could not be found")

def main():
    choice = input("F\\G\nDon't worry I wont delete or overwrite your existing file\nFragment or Defragment?(f\d) : ")
    if choice=="f":
        path=input("File path : ")
        number=int(input("number of fragments : "))
        print(f"The fragmented files have been saved in {frag(path,number)}")
        print("Please do not edit or rename the files... Doing so might corrupt the orginal file\n")
    elif choice=="d":
        path=input("Folder containing the fragmented files : ")
        print(f"The defragmented file has been stored in {defrag(path)}\n")
    else:
        print("Invalid input")
    main()
main()         