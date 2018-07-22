# MIME --> Multipurpsoe Internet Mail Extension
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# create an object of MIMEMultipart

message = MIMEMultipart()

message["Subject"] = "MYNTRA SHOPPING"
##message["Cc"] = "abc@gmail.com"
##message["Bcc"] = "pqr@gmail.com"
message["From"] = "MYNTRA HOLI SALE"

# sender and receive
sender = "uttam.saxena5@gmail.com"
receiver = "meetuttamsaxena@gmail.com"
'''
Reading a column from CSv file (written in list comprehension)
'''
##receiver = [i[0] for i in list(csv.reader(open("file.csv")))]

# username and password
username = sender
password = open("pwd.txt").read()

# writing mail body
body = """
<h1> FLAT 50% OFF </h1>
<h2> EXTRA 10% OFF ON AXIS BANK CREDIT CARD </h2>
<p> Buy 1 get 10 free </p>
<p> Free Shipping on purchase of 20000 </p>
<h1> Only 2 days left , Hurry !!!! </h1>
"""
txt = MIMEText(body,"html")   # plain for normal text
message.attach(txt)


# attach an image
i = open("image.jpg","rb")
img = MIMEImage(i.read())
message.attach(img)


# old program
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(username,password)
server.sendmail(sender,receiver,message.as_string())

print("Mail Sent")










































