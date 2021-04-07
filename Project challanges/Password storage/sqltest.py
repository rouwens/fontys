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
username = "drouwens"
inhoud = "drouwens@gmail.com"
id = "2"
switch = """UPDATE %s SET username = %s WHERE %s.ID = %s;"""
cursor.execute(switch, (username, inhoud, username, id,))


