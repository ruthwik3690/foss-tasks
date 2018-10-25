from PIL import Image
print("WELCOME TO SHOPKART")
Amount=0
print("How many categories of items do u want?\n1)Mobile Phones\n2)Computer Accessories\n3)Watches\n4)Headphones")
f=int(input())
for e in range(0,f):
 print("Select a category\n1)Mobile Phones\n2)Computer Accessories\n3)Watches\n4)Headphones")
 c=int(input())
 if(c==1):
  print("The available items are \nITEM NAME         PRICE\n1)Asus Zenfone    11000\n2)Note 5 Pro      16000\n3)Realme          10000\n4)Nokia 5.1 Plus  14000\n5)Vivo V9         18000")
  a=['11000','16000','10000','14000','18000']
  print("Enter the no. of items u want..")
  b=int(input())
  for i in range(0,b):
    print("Enter the item number")
    z=int(input())
    if(z==1):
     Amount=Amount+int(a[0])
    elif(z==2):
      Amount=Amount+int(a[1])
    elif(z==3):
      Amount=Amount+int(a[2])
    elif(z==4):
      Amount=Amount+int(a[3])
    else:
      Amount=Amount+int(a[4])
 elif(c==2):
   print("The available items are\nITEM NAME    PRICE\n1)Mouse       500\n2)Keyboard    750\n3)Speakers    1200\n4)Headphones  700")
   x=['500','750','1200','700']
   print("Enter the no. of items u want..")
   b=int(input())
   for i in range(0,b):
    print("Enter the item number")
    p=int(input())
    if(p==1):
      Amount=Amount+int(x[0])
    elif(p==2):
       Amount=Amount+int(x[1])
    elif(p==3):
       Amount=Amount+int(x[2])
    else:
       Amount=Amount+int(x[3])
  
 elif(c==3):
   print("The available items are\nITEM NAME     PRICE\n1)Fastrack     4000\n2)Rolex       120000\n3)Timex        6400\n4)Sonata       2500\n5)Titan        3600")
   k=['4000','120000','6400','2500','3600']
   print("Enter the no. of items u want..")
   b=int(input())
   for i in range(0,b):
    print("Enter the item number")
    i=int(input())
    if(i==1):
      Amount=Amount+int(k[0])
    elif(i==2):
     Amount=Amount+int(k[1])
    elif(i==3):
      Amount=Amount+int(k[2])
    elif(i==4):
      Amount=Amount+int(k[3])
    else:
      Amount=Amount+int(k[4])
 elif(c==4):
  print("The available items are\nITEM NAME      PRICE\n1)Sony          900\n2)Skullcandy    800\n3)JBL           1500\n4)Mi            600")
  g=['900','800','1500','600']
  print("Enter the no. of items u want..")
  b=int(input())
  for i in range(0,b):
    print("Enter the item number")
    z=int(input())
    if(z==1):
     Amount=Amount+int(g[0])
    elif(z==2):
      Amount=Amount+int(g[1])
    elif(z==3):
      Amount=Amount+int(g[2])
    else:
      Amount=Amount+int(g[3])
print("Proceeding to checkout..")
print("The amount payable is "+ str(Amount))
print("Do u have coupons?")
r=input()
if(r=="yes"):
 print("Congratulations!You got a discount of 4%")
 Amount=Amount-Amount*0.04
 print("Final amount is "+str(Amount))
else:
  print("Final amount is "+str(Amount))
print("Proceeding to payment..")
print("Select a payment option")
print("1)Credit Card\n2)Debit Card\n3)Net Banking\n4)Cash-on-Delivery")
q=int(input())
print("Enter the captcha code displayed for security reasons..")
print("Prove that you are not a robot.")
img=Image.open("1.jpg")
img.show()
img.close()
y=input()
if(y=="qGphJD"):
    print("Success.You r not a robot.")
    print("Proceeding to payment")
    if(q==1):
        print("Enter ur credit card no.")
        e=int(input())
        print("Completing the payment..")
        print("Success.Your transaction has been completed")
    elif(q==2):
        print("Enter ur debit card no.")
        e=int(input())
        print("Completing the payment..")
        print("Success.Your transaction has been completed")
    elif(q==3):
        print("Enter ur account no.")
        e=int(input())
        print("Completing the payment..")
        print("Success.Your transaction has been completed")
    elif(q==4):
        print("Money will be taken when delivered.")
        print("Success.Your transaction has been completed")
else:
    print("The captcha u entered is not correct.")
    print("Try another one..")
    img=Image.open("images.png")
    img=img.show()
    r=input()
    if(r=="m9gtl0"):
        print("Sucess.You r not a robot.")
        print("Proceeding to payment")
        if(q==1):
          print("Enter ur credit card no.")
          e=int(input())
          print("Completing the payment..")
          print("Success.Your transaction has been completed")
        elif(q==2):
          print("Enter ur debit card no.")
          e=int(input())
          print("Completing the payment..")
          print("Success.Your transaction has been completed")
        elif(q==3):
          print("Enter ur account no.")
          e=int(input())
          print("Completing the payment..")
          print("Success.Your transaction has been completed")
        elif(q==4):
          print("Money will be taken when delivered.")
          print("Success.Your transaction has been completed")
    else:
        print("The captcha you entered is not correct.")
        print("Cannot proceed to payment")
        print("Your transaction is cancelled")
        print("Completing the payment..")

