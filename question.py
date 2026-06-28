


#This is the start of my code with a function and welcomes the user
def main():
 print("hello wlecome to my qyiz")
#sets the score to 0
score = 0

#First question:
while True:
    print("Question 1:")
    print("(a: auckland")
    print("(b: wellitinton")
    print("c: queenstown")
    question = input("Question 1: whitch city is new zealnd capital city?").strip().lower()
    answer = ["b" , "wellington"]
 #if they get it right using Wellington
    if question in answer:
        print("Well done! It is Wellington. You got it right!")
        score = score + 1
        break
 # They get it wrong and have to try again
    else:
        print("pls try again")


# This is the second question of my code with a function 
while True:

    question = input("what ks captail city of new zealand?").strip()
    answer =["wellington" , "Wellington"]
 # if they get it right  using Wellington
    if question in answer:
         print("well done")
         score = score + 1
         break
  #They get it wrong and have to try again
    else:
        print ("pls try again ")

 # This is the third question of my code with a function     
while True:
 question2 = input("Which city has the largest population in New Zealand?").strip()
 # if they get it right using Auckland
 if question2 ==("Auckland"):
     print("nice")
     score = score + 1
     break
 # if they get it right  using auckland
 elif question2 ==("auckland"):
     print("nice")
     score = score + 1
     break
 #They get it wrong and have to try again
 else:
     print("pls try agine")
# This is the fourth question of my code with a function 
while True:
 question3 = input("Do you live in Auckland please answer yes or no!!!").strip() .lower()
 # if they get it right using yes
 if question3 == ("yes"):
   print("good job")
   score = score + 1
   break
 #They get it wrong and have to try again
 else:
   print("pls try agine")
# This is the fifte question of my code with a function 
while True:
 question4 = input("What is the largest city in New Zealand?").strip()
 # if they get it right using Auckland
 if question4 ==("Auckland"):
     print("nice")
     score = score + 1
     break
 # if they get it right using auckland
 elif question4 ==("auckland"):
     print("nice")
     score = score + 1
     break
 #They get it wrong and have to try again
 else:
     print("pls try agine")
# This is the sixth question of my code with a function 
while True:
 question5 = input("How many major islands are there in New Zealand?").strip() .lower()
 # if they get it right using two
 if question5 ==("two"):
     print("nice")
     score = score + 1
     break
 # if they get it right using 2
 elif question5 ==("2"):
     print("nice")
     score = score + 1
     break
 #They get it wrong and have to try again
 else:
     print("pls try agine")
     # This is the seventh question of my code with a function 
while True:
 question6 = input("What is the largest city in New Zealand?").strip()
 # if they get it right using Auckland
 if question6 ==("Auckland"):
     print("nice")
     score = score + 1
     break
 # if they get it right using auckland
 elif question6 ==("auckland"):
     print("nice")
     score = score + 1
     break
 #They get it wrong and have to try again
 else:
     print("pls try agine")
# This is the eighth question of my code with a function 
while True:
 question7 = input("What is 2 + 3?").strip() .upper()
 # if they get it right using 4
 if question7 ==("5"):
     print("nice")
     score = score + 1
     break
 # if they get it right using FIVE
 elif question7 ==("FIVE"):
    print("nice")
    score = score + 1
    break
 #They get it wrong and have to try again
 else:
     print("pls try agine")
# This is the ninth question of my code with a function 
while True:
 question8 = input("what is 1 + 1?").strip() .upper()
 # if they get it right using 2
 if question8 == input("2"):
     print("nice")
     score = score + 1
     break
 # if they get it right using TWO
 elif question7 ==("TWO"):
    print("nice")
    score = score + 1
    break
 #They get it wrong and have to try again
 else:
     print("pls try agine")
# This is the tenth question of my code with a function 
while True:
 question9 = input("what is 2 + 2?").strip() .upper()
 # if they get it right using 4 get 1 score
 if question9 == input("4"):
     print("nice")
     score = score + 1
     break
 # if they get it right using FOUR get 1 score
 elif question7 ==("FOUR"):
    print("nice")
    score = score + 1
    break
 #They get it wrong and have to try again
 else:
     print("pls try again")
     # This is the eleventh question of my code with a function 
while True:
 question10 = input("what is 2 + 1?").strip() .upper()
 # if they get it right using 3 get 1 score
 if question10 == input("3"):
     print("nice")
     score = score + 1
     break
 # if they get it right using THREE get 1 score
 elif question10 ==("THREE"):
    print("nice")
    score = score + 1
    break
 #They get it wrong and have to try again
 else:
     print("pls try again")

     print(score)

     print("good job thank you for u done the quzie this is u get score is: {score} / 11")

main()
