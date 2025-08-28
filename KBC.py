import time as t

questions=[['question-1. What is capital of India?','Gujarat','Maharastra','Delhi','Panjab','none',3],
          ['question-2. Who is the Prime Minister of  India?','Narendra modi','Rahul Gandi','Avarind kejrival','Mamta','none',1],
          ['question-3. Modi is which party Supported?','BJP','AAP','Congress','shivsena','none',1],
          ['question-4. What is capital of Gujarat?','Wankaner','surat','Delhi','Gandhinagar','none',4],
          ['question-5. Who is thalapathy Vijay?','actor','singer','polition','worker','none',1],
          ['question-6. when time is your state?','actor','singer','polition','worker','none',1],
          ['question-7. when time is Gujarat state?','actor','singer','polition','worker','none',1]
          ]
levels=[1000,2000,4000,10000,50000,100000,20000000]
lifeline=[' 1.Phone call',' 2.Audiounce Pall']
money=0
for i in range(0,len(questions)): 
    question=(questions[i])
    print(f"Quistion is {question[0]}for Rs.{levels[i]}")
    print(f"a.{question[1]} b.{question[2]}")
    print(f"c.{question[3]} b.{question[4]}")
    if lifeline:
        print("Choose a life line :")
        for i in range(0,len(lifeline)):
            print(f"{lifeline[i]}")
        choose=int(input("Enter a life line : "))
        if choose==1:
            phone_number=int(input("Enter a phone number : "))
            t.sleep(5)
            print("You dial number is correnty busy please try later ")
            lifeline.pop(choose-1)
        elif choose==2:
            print(f"{lifeline[i]} Answer is {question[-1]}")
            lifeline.pop(-1)
        else:
            print("No life Line use : ")
    else:
        print("You use all lifeline")
    reply=int(input("Enter your Answer{1-4}:"))
    if reply==question[-1]:
        print(f"Correct answer you have win by Rs {levels[i]}")
        if i==4:
            money=100000
    else:
        print("try Again")
        break
print(f"your collected money is {money}") 
