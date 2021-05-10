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

item = "9"

getuserid = """SELECT userid FROM `wachtwoorden` WHERE `ID` = %s"""
cursor.execute(getuserid, (item, ))
fetch = cursor.fetchall()
clean = str(fetch)
id = re.sub(r'[^\w\s]', '', clean)
print (id)