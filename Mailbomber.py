#!/usr/bin/python3
#mass_mailer.py -> mass mailing script
import smtplib
import sys
def mass():
    smtpobj = smtplib.SMTP('smtp.gmail.com',587)
    #smtpobj is a SMTP object that represents a connection to an SMTP mail server and has methods for sending emails.
    my_email = input("What is  your gmail?:")
    my_passw = input("Enter the password:")
    recip_mail = input("What is the recipient gmail?:")
    message = input("Enter the message that you want to mail:\n")
    times = int(input("How many times do you want to mail?"))
    smtpobj.starttls() #This step enables encryption(TLS Encryption) for your connection.
    
    try:
        smtpobj.login(my_email,my_passw)
        #this will help user to loged in gmail account
    except smtplib.SMTPAuthenticationError:
        print("Change setting in your account to login in your account")
    
    for i in range(0,times):
        i=i+1
        smtpobj.sendmail(my_email,recip_mail,message)
        #sendmail() will help user to send mail to recipent user.
        print("mail sended",i,"times...")    
    print("Lets quit:\n",smtpobj.quit())
#it will close your connection
mass()
