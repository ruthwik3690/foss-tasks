i=0
p=0
u=0
print("Enter the number of times you want to play the game.")
f=int(input())
while(i<f):
 print("Enter any one of three: rock or paper or scissors")
 import random
 a=input()
 b=['rock','paper','scissors']
 c=(random.choice(b))
 print(c)
 if(a==c):
   print("It's a tie!")
   i=i+1
 elif(a=="rock" and c=="scissors"):
   print("U win.!")
   u=u+1
   i=i+1
 elif(a=="paper" and c=="rock"):
   print("U win.!")
   u=u+1
   i=i+1
 elif(a=="scissors" and c=="paper"):
   print("U win.!")
   u=u+1
   i=i+1
 elif(not(a=="rock" or a=="paper" or a=="scissors")):
   print("Enter correctly..")
 else:
   print("Computer wins")
   p=p+1
   i=i+1
print("Your score is "+str(u))
print("Computer's score is " +str(p))
if(u>p):
  print("You win the game..!")
else:
  print("Computer wins the game..!")
