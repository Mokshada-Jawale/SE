#Sending and generating OTP as a program without Functional decomposition

import random   #Random library to generate OTP
import smtplib  #to send e-mail

#Generate random 4-5 digit otp
otp = str(random.randint(1000,99999))

sender_email = '<sender email>'
sender_pass = '<sender password>'
receiver_email = '<receiver email>'

#sending the otp to receivers email
#connect to the server
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()

#start the server
server.starttls()

#login
server.login(sender_email,sender_pass)

#send the email
msg = '[OTP]\n OTP for email verification is: '+otp
server.sendmail(sender_email, receiver_email, msg)

#close the server
server.close()

print('OTP has sent to your email address')
