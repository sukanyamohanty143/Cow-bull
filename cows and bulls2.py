import random
name = input("Enter the name")
print("WELCOME",name,"TO COW BULL GAME")
print("If your guess is equal to the secreaat number and position then it will print(Bull)")
print("If your gues is wrong then it will priont, (COW)")
def cow_bull():
    move=[1,2,3,4,5,6,7,8,9]
    sec=random.sample(move,5)
    print(sec)
    cow=[]
    bull=[]
    i=1
    print("You have 7 Chances to play")
    while i<=7:
        if sec==bull:
            print("Congrats 🥳 You are the Winner!")
            break
        user=int(input("Enter Your no from 0 to 9:"))
        position=int(input("Enter the position:"))
        if user not in sec:
            print("guessed number is not exist in the list")
        else:
            if user in sec and sec.index(user)==position:
                bull.insert(position,user)
                print("Bull",bull)
            
            elif sec.index(user)!=position:
                cow.insert(position,user)
                print("Cow",cow)
                
        i+=1 
cow_bull()
user2=input("Do you want to play again(y/n):")
if user2=="y":
    cow_bull()
else:
    print("Thanks for playing the Game 😌")