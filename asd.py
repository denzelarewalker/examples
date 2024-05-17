import os
 
if os.path.isfile("myfile.txt"):
    print("Файл существует")
else:
    print("Файл не существует")
