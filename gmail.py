import smtplib   #import the SIMPLE MAIL TRANSFER PROTOCOL(SMTP)-smtplib module
import getpass   #import this for hiding the password you type
from email.mime.text import MIMEText    #import the classes
from email.mime.multipart import MIMEMultipart

fromadress=input("Enter email of sender: ")       #sender's email
password=getpass.getpass("Enter password of receiver: ")           #sender's password,getpass is used to hide the password from the terminal

mailto=input("Enter the email address you want to send to:")
subject=input("Enter the subject:")
body=input("Enter the body:")
				
msg=MIMEMultipart()
msg['From']=fromadress   #storing all values in variable
msg['To']=mailto
msg['subject']=subject
msg.attach(MIMEText(body,'plain'))  #attaching the body of email to other parts(MIMEText)	

server=smtplib.SMTP('smtp.gmail.com',587)  #creates SMTP session, 587 is port number for gmail
server.starttls()    #enabling the TLS mode: which sends the email securely(encyption)
server.login(fromadress,password)       #authentication(login)
server.sendmail(fromadress,mailto,msg.as_string())    #sending the mail
print("\nThe email was sent successfully!!")
server.quit #ending session

