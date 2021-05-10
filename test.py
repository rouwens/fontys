import random
import time
import requests
import string
import mysql.connector as mysql
import re
import hashlib
import base64

db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "passwordmanager"
    )
cursor = db.cursor()

id = "8"
fetchid = """SELECT ID FROM `wachtwoorden` WHERE `userid` = %s"""
cursor.execute(fetchid, (id,))
sql = cursor.fetchall()
sqlstring = str(sql)
id = re.sub(r'[^\w\s]', '', sqlstring)

print (sqlstring)