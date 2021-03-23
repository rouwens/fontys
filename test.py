from cryptography.fernet import Fernet 
import mysql.connector as mysql

#print ("Type hier je geheim bericht")
#secret = input()

#key = Fernet.generate_key()
#encryption_type = Fernet(key)
#encrypted_message = encryption_type.encrypt(b"Hello World")

#decryption_message = encryption_type.decrypt(encrypted_message)
#print (key)
#print (encrypted_message)
#print ()
#print (decryption_message)

username = input()

db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "passwordmanager"
    )
cursor = db.cursor()

tableSQL = """SELECT * FROM `'everstegen'`"""
cursor.execute(tableSQL)
table = cursor.fetchall()
for record in table:
    tableout = record

#tablestring = str(tableout)
#tabletofilter = tablestring.text
#tablefilter = tablestring.find(username)

print (table)
#if tablefilter == username:
 #   print("Gebruikerstabel bestaat al")

#else:
#    print ("Table aangemaakt")                  