print("welcome to this maze")
score = 0
start =input("Do want to play a game ?  ")
if start.lower() == "yes":
    print("lets start the game")
else:
    print("sorry youu are a chicken")
    quit()
ans1=input("What is necessory to live ")
if ans1.lower() == "oxygen":
    print("correct")
    score += 1
else:
    print("incorrect")  

ans1=input("What is necessory to walk ")
if ans1.lower() == "legs":
    print("correct")
    score += 1
else:
    print("incorrect")  

ans1=input("What is necessory to talk ")
if ans1.lower() == "speak":
    print("correct")
    score += 1
else:
    print("incorrect")  

ans1=input("What is necessory to see ")
if ans1.lower() == "eyes":
    print("correct")
    score += 1
else:
    print("incorrect")  

ans1=input("What is necessory to die o")
if ans1.lower() == "life":
    print("correct")
    score += 1
else:
    print("incorrect")  

print("your score is "+ str(score) +" out of 5")
print("your persentage is "+str((score/5)*100) +" %")