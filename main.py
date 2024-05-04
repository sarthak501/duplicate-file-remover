import os
def compare(a,b):
    try:
     with open(a,"rb") as file1, open(b,"rb") as file2:
      if file1.read()==file2.read():
        return True
      else:
        return False
    except :
     return False
def main(c):
 t_files=[]
 files=os.listdir(c)
 size=0 
 for i in range(len(files)):
   for j in range(i+1,len(files)):
    path1=os.path.join(c,files[i])
    path2=os.path.join(c,files[j])
    if compare(path1,path2) and (path1 not in t_files and path2 not in t_files):
     print(f"{files[i]} and {files[j]} are same")
     t_files.append(path2)
     size+=os.path.getsize(path2)
 size=size/1024
 print(f" you can free {size} Kb memory")
 choice=input("press yes or no: ")
 if choice.lower()=="yes":
  for i in t_files:
   os.remove(i)
 # print(t_files) 

path=input("enter the path: ")
main(path)

