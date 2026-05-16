# quize application 

question = [
    {
    "question" : "What is the capital of Japan?",
    "option":["Beijing","Seoul","Tokyo","Bangkok"],
    "ans":"Tokyo"
   },
   {
    "question" : "Which planet is known as the Red Planet?",
    "option":["Venus","Mars","Jupiter","Saturn"],
    "ans":"Mars"
  }
]

i = 0
print("Choose correct options below the question,plz select option number",end = " ")

while(i < len(question)):
    print(question[i]["question"])
    for j in range(len(question[i]["option"])):
          print(f'{j + 1}) {question[i]["option"][j]}')
    ans = int(input("type the correct option number :"))
    if question[i]["ans"] == question[i]["option"][ans-1] :
            print(f' ==> {question[i]["option"][ans-1]} is correct')
    else :
          print(f' ==>  {question[i]["option"][ans-1]} answer is wrong , {question[i]['ans']} is correct')
                  
    i += 1          

# print(f"{i+1}) {question[i]["question"]["option"]}")