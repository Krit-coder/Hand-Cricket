import random
import os
tr=0
tr1=0
def batting(w1,b1):
    r = 0
    i=1
    while(i<=b1 and w1>0):
        h = int(input("Enter your Hand number: "))
        if(h>6 or h<0):
            print("Wrong Number\n You are OUT")
            exit()
        ran2 = random.randint(0,6)
        print(ran2 ,"\t", h)
        if(h==ran2):
            w1-=w1
            if(w1>0):
                print("Current Score = ",r)
                print("Remaining Wickets = ",w1)
        elif(h==0):
            h=ran2
            r+=h
            if(r>tr1 and tr1!=0):
                break
        else:
            r+=h
            if(r>tr1 and tr1!=0):
                break
        i+=1

    return r

def bowling(w2,b2):
    r1 = 0
    j=1
    while(j<=b2 and w2>0):
        h1 = int(input("Enter your Hand number: "))
        if(h1>6 or h1<0):
            print("Wrong Number\n You are OUT")
            exit()
        ran3 = random.randint(0,6)
        print(ran3 ,"\t", h1)
        if(h1==ran3):
            w2-=1
            if(w2>0):
                print("Current Score = ",r1)
                print("Remaining Wickets = ",w2)
        elif(ran3==0):
            ran3=h1
            r1+=ran3
            if(r1>tr and tr!=0):
                break
        else:
            r1+=ran3
            if(r1>tr and tr!=0):
                break
        j+=1

    return r1

flag = True
while(flag):
    print("\t\t****HAND CRICKECT****")
    print("=======================")
    print("| WELCOME TO THE GAME |")
    print("=======================")
    print("")
    name = input("Enter Your Name: ")

    for c in range(3):
        print("====================================")

    print("Hello ",name,",")
    print(".")
    print("WELCOME TO THE CRICKET-MANIA")
    print(".")

    print("\t\t^^INSTRUCTIONS^^")

    print("1.While playing you have to choose any number between 0 to 6(hand number)\n")
    print("2.If hand number matches between you and the computer then one who is batting lose 1 wicket\n")
    print("3.If you enter a number more than 6 or less than 0 then you are OUT\n")
    print("4.If batsman enter 0 then he gets the runs which the bolwer has enterd\n")
    print("5.Batsman hand no. is shown on right side and that of bowler on left side\n")

    for c in range(3):
        print("====================================")

    print("\tGAME STARTS")

    for c in range(3):
        print("====================================")

    over = int(input("Enter number of overs: "))
    b = over*6
    w = int(input("\nEnter number of wickets: "))

    for c in range(3):
        print("====================================")
    
    print("\tTOSS")

    for c in range(3):
        print("====================================")
    
    s = input("Heads or Tails: ")
    s1=""
    ran = random.randint(0,1)

    if(ran == 0):
        s1 = "Heads"
    else:
        s1 = "Tails"
    
    if((s.lower())==(s1.lower())):
        print("You won the toss")
        s2 = input("Batting or Bowling: ")
        if((s2.lower()=="batting")):
            tr = batting(w,b)
            print("You Scored ",tr," runs")
            print("Computer needs ",(tr+1)," runs to win")
            tr1 = bowling(w,b)
            print("Computer Scored ",tr1," runs")

            for c in range(3):
                print("#############################")

            if(tr1<tr):
                print("Congratulations "+name+"!! You Have Defeated The Almighty, Computer!!")
                print("You won by ", (tr-tr1)," runs")
            if(tr1>tr):
                print("Sorry "+name+", But The Computer Has Defeated You..!")
                print("You lose by ",(tr1-tr)," runs")
            if(tr1==tr):
                print("It's a Tie..! :( ")
            
            for c in range(3):
                print("#############################")

        if((s2.lower()=="bowling")):
            tr1 = bowling(w,b)
            print("Computer Scored ",tr1," runs")
            print("You need ",(tr1+1)," runs to win")
            tr = batting(w,b)
            print("You Scored ",tr," runs")

            for c in range(3):
                print("#############################")

            if(tr<tr1):
                print("Sorry "+name+", But The Computer Has Defeated You..!")
                print("You lose by ",(tr1-tr)," runs")
            if(tr>tr1):
                print("Congratulations "+name+"!! You Have Defeated The Almighty, Computer!!")
                print("You won by ",(tr-tr1)," runs")
            if(tr==tr1):
                print("It's a Tie..! :( ")

            for c in range(3):
                print("#############################")

    else:
        print("You lost the toss")
        ran4 = random.randint(0,1)
        s2 = ""
        if(ran4 == 0):
            s2 = "batting"
        else:
            s2 = "bowling"

        if(s2 == "batting"):
            print("Computer will bat")
            tr1 = bowling(w,b)
            print("Computer Scored ",tr1," runs")
            print("You need ",(tr1+1)," runs to win")
            tr = batting(w,b)
            print("You Scored ",tr," runs")

            for c in range(3):
                print("#############################")

            if(tr<tr1):
                print("Sorry "+name+", But The Computer Has Defeated You..!")
                print("You lose by ",(tr1-tr)," runs")
            if(tr>tr1):
                print("Congratulations "+name+"!! You Have Defeated The Almighty, Computer!!")
                print("You won by ",(tr-tr1)," runs")
            if(tr==tr1):
                print("It's a Tie..! :( ")

            for c in range(3):
                print("#############################")

        if(s2 == "bowling"):
            print("Computer will bowl")
            tr = batting(w,b)
            print("You Scored ",tr," runs")
            print("Computer needs ",(tr+1)," runs to win")
            tr1 = bowling(w,b)
            print("Computer Scored ",tr1," runs")

            for c in range(3):
                print("#############################")

            if(tr1<tr):
                print("Congratulations "+name+"!! You Have Defeated The Almighty, Computer!!")
                print("You won by ",(tr-tr1)," runs")
            if(tr1>tr):
                print("Sorry "+name+", But The Computer Has Defeated You..!")
                print("You lose by ",(tr1-tr)," runs")
            if(tr1==tr):
                print("It's a Tie..! :( ")
            
            for c in range(3):
                print("#############################")

    
    print("")
    print("Enter 1 to Play again")
    print("")
    print("Enter 0 to quit")
    choice  = int(input("====> "))
    print("")

    if(choice==1):
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Good Bye!")
        flag = False




            


            
    




    

