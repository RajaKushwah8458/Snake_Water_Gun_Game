import random

computer = random.choice([1,-1,0])
youstr  = input("Enter your choice:")
youdist  = {'s':1,'w':-1,'g':0}
revercedist = {1:'Snake',-1:'Water',0:'Gun'}
you = youdist[youstr]
print(f"Your Choice {revercedist[you]} \n Computer Chioce {revercedist[computer]}")

if(you==computer):
    print("Game Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Lose") 
    elif(computer==1 and you==-1):
        print("You lose")    
    elif(computer==1 and you==0):
        print("You Win") 
    elif(computer==0 and you==-1):
        print("You Win")              
    elif(computer==0 and you==1):
        print("YOu lose")
    else:
        print("Something was wrong!!!!!")        


