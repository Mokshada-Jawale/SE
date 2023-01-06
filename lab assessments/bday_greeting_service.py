import mysql.connector as mc
import datetime
import smtplib

def todays_birthdays():
    cursor.execute("SELECT * FROM BDAY")
    todays_birthdays = cursor.fetchall()
    for i in todays_birthdays:
        dob=i[-1]
        if dob.month==today.month and dob.day==today.day:
            continue
        else:
            todays_birthdays.remove(i)
    return todays_birthdays


def send_birthday_mail(birthdays):
    print(birthdays)
    for i in birthdays:
        name=i[0]
        eMail=i[1]
        print(name,eMail)
        server.sendmail(senderEmail, eMail, "Happy Birthday " + name)
    print("Birthday mails sent to ",len(birthdays),"users")

if __name__=="__main__":
    user="root"
    pwd="dbpass"
    db="SE"
    host="localhost"
    today=datetime.date.today()
    try:
        mycon=mc.connect(user=user,password=pwd,database=db,host=host)
        cursor=mycon.cursor()
    except:
        print("Error: Unable to connect to the database")
        exit()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # connecting to SMTP server at port 587
        server.ehlo()
        server.starttls()
        senderEmail = '<receiver email>'
        senderPass = '<sender password>'
        server.login(senderEmail, senderPass)
    except:
        print("Unable to connect to the SMTP server")
        exit()

    todays_birthdays = todays_birthdays()
    send_birthday_mail(todays_birthdays)
