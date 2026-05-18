import os

File_name = "demo.txt"

found = False


def createFile():
    if not os.path.exists(File_name) :
      with open(File_name,"w") as file:
          file.write("STUDENT MANGEMENT \n")
    else :
       print("file all read existes")

def addStudent():
   with open(File_name,"a") as file:
     name = input('Enter student name :').lower()
     file.write(name + "\n")

def viewStudent():
   with open(File_name,"r") as file:
      content = file.read()
      print(content)  

def readLineByLine():
   with open(File_name,"r") as file:
      one_line = file.readline()
      print(one_line)

def readAllLines():
   with open(File_name,"r") as file:
      all_line = file.readlines()
      print(all_line)  



def searchStudent():
    found = False
    search = input('search a student name :').lower()
    with open(File_name,"r") as file:
       for data in file :
          if search.lower() in data.lower() :
             found = True
             print(f'student Fount {data}') 
    if not found :
     print(f'name not Fount')  

def cursor_demo():

    with open(File_name, "r") as file:

        print("\nCursor position:", file.tell())

        data = file.read(10)

        print("Read data:",data)

        print("Cursor after reading:", file.tell())

        file.seek(0)

        print("Cursor after seek:", file.tell())      
          

while True :

 options = ["create file","Add student","view student","read line one by one","read all lines","search student","cursor","exit"]

 for index,op in  enumerate(options,start=1) :
   print(f"{index}) {op.title()}")
           
 check = int(input("choose the operation in File :"))

 if check == 1 :
   createFile()
 elif check == 2 :
   addStudent()
 elif check == 3 :
   viewStudent()
 elif check == 4 :
   readLineByLine()
 elif check == 5 :
   readAllLines()
 elif check == 6 :
     searchStudent()
 elif check == 7 : 
     cursor_demo()
 elif check == 8 :    
     print('program end')
     break
 else : 
    print('invalid choice')     

      

      

         
       
