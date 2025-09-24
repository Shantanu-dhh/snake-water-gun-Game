import random
computer = random.choice((1,0,-1))
youstr = input("enter your choice :")
youdict = {"s":1, "w":0,"g":-1}
reversedict = {1 : "snake", 0 : "water", -1:"gun"}
you = youdict[youstr]

print(f"Your choice: {reversedict[you]}\nCompter's choice : {reversedict[computer]} ")
if(you==computer):
    print("It's a draw")

else:
     if((computer-you)==-2 or (computer-you)==1):
          print("You Loose!")
     else:
          print("You Win!")     
        
'''

    if(computer==1 and you==0 ) : (computer - you)=1
        print("You Loose!")   
    elif(computer==1 and you==-1) :(computer-you)=2
        print("You Win!")   
    elif(computer==0 and you==1 ) :(computer-you)=-1
        print("You Win!")   
    elif(computer==0 and you==-1 ) :(computer-you)= 1
        print("You Loose!")   
    elif(computer==-1 and you==0 ) :(computer - you)=-1
        print("You Win")   
    elif(computer == -1 and you ==1 ) : (computer-you)=-2
        print("You Loose!") 
    else:
        print("something went wrong") 

        Below logic is written based  on values of computer- you     

'''
   






  