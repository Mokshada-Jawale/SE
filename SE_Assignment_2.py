# Sending and generating OTP assignment with Functional decomposition after code review
import random  # Random library to generate OTP
import re      #regular expression library to check if email is in valid format
import smtplib # to send e-mail

def is_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #setting email template: *@*.*
    if re.fullmatch(regex,email): #checking if the entered email matches the template
        return True
    else:
        return False
# function to return a OTP of length n
def generate_otp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(0,9))
    return otp

# function to send the otp
def send_otp(otp):
    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    # Start the server
    server.starttls()
    # Login
    sender_email = '<sender email>'
    sender_pass = '<sender password>'
    server.login(sender_email, sender_pass)
    receiver_email = '<receiver email>'
    # Send the email
    # msg = "OTP for email verification is: " + otp
    if is_email(receiver_email):
        server.sendmail(sender_email, receiver_email, "Subject:OTP\nYour OTP for email verification is "+otp)
    else:
        print('Invalid email ID! Please try again later')
    # close the server
    server.close()
    print("OTP sent to your email address")

# function to verify otp
def verify_otp(otp,OTP):
    if OTP==otp:
        print("Email ID successfully verified...")
    else:
        print("Invalid OTP")

otp = generate_otp()
send_otp(otp)

# Enter the OTP they received for verification
OTP = input('Enter the OTP you received: ')
verify_otp(otp, OTP)










