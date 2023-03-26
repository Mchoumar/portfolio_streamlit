import smtplib, ssl
from os import getenv

def send_email(msg):
    host = "smtp.gmail.com"
    port = 465

    username = "example@gmail.com"
    password = getenv("PASSWORD")

    receiver = "example@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)


if __name__ == "__main__":
    send_email("LOL, tst\nmahmoudchoumar@ieu.edu.pl")
    print("Sent")
