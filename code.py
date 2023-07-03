import time
import os
a = open("app.bat","w")
a.write("reg query HKEY_CURRENT_USER\SOFTWARE\>>software_list.txt")
a.close()
#time.sleep(10) #Within these 10 seconds please double-click manually on the batch file that is created
os.system("app.bat")
try:
    for f in  open('software_list.txt'):
         a = f.replace("\\" ," ")
         b = a.split()
         c = len(b)
         for i in range(c):
              d = b[i + (c - 1)]
              with open("only_software_name.txt", "a") as f:
                   print(d,file=f) #Here file=f is used so that the input can be written in the created file. 
              break
except(FileNotFoundError):
     print("Please press the batch file manually within 10 second")
