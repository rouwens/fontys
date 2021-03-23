import smtplib

to = 'daan@daanesmee.nl'
gmail_user = 'daan@daanesmee.nl'
gmail_pwd = 'Daan0409.'
smtpserver = smtplib.SMTP('mail.daanesmee.nl',587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print (header)
msg = header + '\n this is test msg from mkyong.com \n\n'
smtpserver.sendmail(gmail_user, to, msg)
#print 'done!'
smtpserver.close()