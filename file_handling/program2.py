# write a program to input muiltiple line in file 


with open("newfile.txt",'a') as file :
  while True :
      name = input('Enter something :').lower()

      if name.lower() == "stop" :
         break
  
      file.write(name + "\n")  
print('program is stop')  
    
