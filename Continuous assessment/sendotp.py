#Implement a program in Python to generate One Time Password and send it to the registered email ID.

import random  #Random library to generate OTP
import re      #regular expression library to check if email is in valid format
import smtplib #to send e-mail

def is_email(email):
    regex = r'\b[A-Za-z0-9._%+]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #setting email template: *@*.*
    if re.fullmatch(regex,email): #checking if the entered email matches the template
        return True
    else:
        return False

#function to return a OTP of length n
def generate_otp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(0,9))
    return(otp)


#Function to verify if entered OTP is correct
def verify_otp(otp,OTP):
    if OTP==otp:
        return True
    else:
        return False

if __name__=='__main__':
    # try block to check if connection can be established with the smtp server
    try:
        server=smtplib.SMTP('smtp.gmail.com',587) #connecting to SMTP server at port 587
        server.ehlo()
        server.starttls() #transfered layer security
        senderEmail='<sender email>'
        senderPass='<sender password>'
        server.login(senderEmail,senderPass)
    except:
        print("Unable to connect to the SMTP server")
        exit()
    otp=generate_otp()
    for i in range(3): # Stop the program if user enters a invalid email several times
        eMail=input("Enter receiver's email id: ")
        if is_email(eMail):
            break
        else:
            print("Invalid email id!!!")
    else:
        print("You've entered an invalid email too many times!!! \n Try again later...")
        exit()
    server.sendmail(senderEmail,eMail,"Subject:OTP\nYour OTP for is "+otp) #Sending the email
    print("An OTP has been sent to {}".format(eMail))
    print("Verify your email id: ")
    OTP=input("Enter the OTP: ")
    verify_otp(otp,OTP)
    server.close()