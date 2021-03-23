import smtplib
import configparser
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipar

# Importeren va config bestand
config = configparser.ConfigParser()
config.read('config.ini')

# Mail server instellingen
smtp_server = 'mail.daanesmee.nl'
smtp_port = 587
smtp_username = 'spam@daanesmee.nl'
smtp_password = 'Spammer123.'

# Bericht informatie
subject = config['mail']['subject']

# Bericht in HTML
f = open('spam.html', 'r')
html = f.read()
htmlstage = MIMEText(html, "html")
message = str(htmlstage)

receivers_mail = ['slachtoffer1@daanesmee.nl', 'daan@daanesmee.nl']
to = ", ".join(receivers_mail)
#to = ['slachtoffer1@daanesmee.nl', 'daan@daanesmee.nl']
#to = ", ".join(recipients)

smtp_subject = 'Subject:' + subject + '\n'
smpt_sender = smtp_username
smtp_sender_pwd = smtp_password
smtpserver = smtplib.SMTP(smtp_server,smtp_port)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(smpt_sender, smtp_sender_pwd)
header = 'To:' + to + '\n' + 'From: ' + smpt_sender + '\n' + smtp_subject
msg = header + message
smtpserver.sendmail(smpt_sender, to, msg)
smtpserver.close()