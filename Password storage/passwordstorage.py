import random
import time
import requests
import string
import mysql.connector as mysql
import re
import hashlib

def start():

    def funcgebruiker (username):
        username = username
        db = mysql.connect(
            host = "rouwens.ddns.net",
            user = "fontys",
            passwd = "E6g2sAnv4FHBB4HB",
            database = "passwordmanager"
            )
        cursor = db.cursor()

        tableSQL = """SELECT added_table FROM `accounts` WHERE `username` = %s"""
        cursor.execute(tableSQL, (username,))
        tableFETCH = cursor.fetchall()
        strtableFETCH = str(tableFETCH)
        added_table = re.sub(r'[^\w\s]', '', strtableFETCH)
        
        print()
        print ("Ingelogd als gebruiker " + username)
        print ("")
        print ("1 - Naar wachtwoorden gaan")
        print ("2 - Instellingen")
        print ("")
        print ("3 - stoppen")
        print ("")
        
        if added_table == "0":
            print ("Database bestaat nog niet type init om het aan te maken")
        
        keuze = input()
        if keuze == "1":
            print ("Keuze 1")
        
        elif keuze == "2":
            print ("Keuze 2")
        
        elif keuze == "3":
            exit()
        
        elif keuze == "init":
            switch = """UPDATE `accounts` SET `added_table` = '1' WHERE `accounts`.`username` = %s;"""
            cursor.execute(switch, (username,))
            createtable = """CREATE TABLE `passwordmanager`.`%s` ( `ID` INT(255) NOT NULL , `name` TEXT NOT NULL , `username` TEXT NOT NULL , `password` TEXT NOT NULL ) ENGINE = InnoDB;"""
            cursor.execute(createtable, (username,))
            print ()
            print ("Database aangemaakt")
            funcgebruiker (username)

        

    

    # Dit is het login scherm
    def inloggen():
        db = mysql.connect(
            host = "rouwens.ddns.net",
            user = "fontys",
            passwd = "E6g2sAnv4FHBB4HB",
            database = "passwordmanager"
            )
        cursor = db.cursor()
        
        print ()
        print ("Geef je gebruikersnaam op")
        username = input()

        # Checkt of gebruikersnaam bestaat in de database

        gebruikerSQL = """SELECT * FROM `accounts` WHERE `username` = %s"""
        cursor.execute(gebruikerSQL, (username,))
        gebruiker = cursor.fetchall()
        for record in gebruiker:
            gebruikerstring = record

        if gebruikerstring == []:
            print ("Gebruiker niet gevonden")
            time.sleep(2)
            start()
        
        #else:
            #tableSQL = """SHOW TABLES"""
            #cursor.execute(tableSQL)
            #table = cursor.fetchall()
            #for record in table:
                #tableout = record
            
            #tablestring = str(table)
            #print (table)
            #sqlusername = "'" + username + "'"
            #tablefilter = tablestring.find(sqlusername)

            #if tablefilter == username:
                #print("Gebruikerstabel bestaat al")
            
            #else:
                #print ("Table aangemaakt")
                #CREATE TABLE `passwordmanager`.`test` ( `ID` INT(255) NOT NULL , `name` TEXT NOT NULL , `username` TEXT NOT NULL , `password` TEXT NOT NULL ) ENGINE = InnoDB;
                #createtable = """CREATE TABLE `passwordmanager`.`%s` ( `ID` INT(255) NOT NULL , `name` TEXT NOT NULL , `username` TEXT NOT NULL , `password` TEXT NOT NULL ) ENGINE = InnoDB;"""
                #usernameclean = re.sub(r'[^\w\s]', '', username)
                #cursor.execute(createtable, (usernameclean,))

        # Haalt het gehashte wachtwoord uit de database en haalt alle interpuncties die er aan zitten weg. Zo is het een schone string.
        pwdSQL = """SELECT PASSWORD FROM `accounts` WHERE `username` = %s"""
        cursor.execute(pwdSQL, (username,))
        pwdFETCH = cursor.fetchall()
        strpwdFETCH = str(pwdFETCH)
        pwd2check = re.sub(r'[^\w\s]', '', strpwdFETCH) 

        # Haalt de salt uit de database en haalt alle interpuncties die er aan zitten weg. Zo is het een schone string

        saltSQL = """SELECT SALT FROM `accounts` WHERE `username` = %s"""
        cursor.execute(saltSQL, (username,))
        saltFETCH = cursor.fetchall()
        strsaltFETCH = str(saltFETCH)

        salt = re.sub(r'[^\w\s]', '', strsaltFETCH)

        print ()
        print ("Vul nu het wachtwoord in")
        print ()
        pwd = input()

        # Hier word het ingevulde wachtwoord opgezet naar een gehashte waarde
        pwdsalt = pwd + salt
        strspwd = str(pwdsalt).encode()
        hpwd = hashlib.sha256(strspwd).hexdigest()

        # Hier word gekeken van de net gemaakte hash overeenkomt met de hash in de database
        if pwd2check == hpwd:
            print ("De login gegevens zijn juist")
            
            #tableSQL = """SELECT added_table FROM `accounts` WHERE `username` = %s"""
            #cursor.execute(tableSQL, (username,))
            #tableFETCH = cursor.fetchall()
            #strtableFETCH = str(tableFETCH)
            #added_table = re.sub(r'[^\w\s]', '', strtableFETCH)
            #usernamesqlsyntax = "'" + username + "'"

            #if added_table == "0":
                #print ("Table bestaat niet")
                #createtable = """CREATE TABLE `passwordmanager`.`%s` ( `ID` INT(255) NOT NULL , `name` TEXT NOT NULL , `username` TEXT NOT NULL , `password` TEXT NOT NULL ) ENGINE = InnoDB;"""
                #switch = """UPDATE `accounts` SET `added_table` = '1' WHERE `accounts`.`username` = %s;"""
                #cursor.execute(createtable, (username,))
                #cursor.execute(switch, (username,))

            #else:
                #print ("Table bestaat")
            
        
        else:
            print ("De login gegevens zijn niet juist. Probeer het opnieuw...")
            time.sleep(2)
            inloggen()
        
        funcgebruiker (username)



    def accountmaken():
        db = mysql.connect(
            host = "rouwens.ddns.net",
            user = "fontys",
            passwd = "E6g2sAnv4FHBB4HB",
            database = "passwordmanager"
                )
        
        cursor = db.cursor()

        print ("Wat is de gebruikersnaam?")
        username = input()
        print ()
        print ("Wat is het wachtwoord dat je wilt gebruiken")
        password = input()
        print()
        print ("Vul het wachtwoord opnieuw in ter controle")
        password_check = input()
        

        if password == password_check:
            print ()
        
        else:
            print ("Wachtwoorden komen niet overeen. Probeer het opnieuw...")
            print ()
            time.sleep (2)
            accountmaken()

        password_checker(pwd = password)

        print ("Vul hier een hint in van het wachtwoord")
        hint = input()
        print ()
        
        if hint == password:
            print("Hint mag het wachtwoord niet bevatten")
            print("Probeer het opnieuw....")
            time.sleep (2)
            accountmaken()

        print("Samenvatting van de gegevens")
        print ()
        print ("Gebruikersnaam: ", username)
        print ("Wachtwoord:     ", password)
        print ("Hint:           ", hint)
        print ("")
        print ("Kloppen deze gegevens? (j/n")
        confirm = input()
        print ()

        if confirm == "j":
            print ("Gegevens opgeslagen. Je kan nu daarmee inloggen.")
            print ()
        
        elif confirm == "n":
            print ("Gegevens weggegooit")
            print ()
            start() 
        
        else:
            print ("invoer onjuist begin opnieuw...")
            time.sleep (2)
            accountmaken()

        # Hier word een salt gegenereerd en gelijk daarna gehasht met het wachtwoord.
        tekens = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        salt = ''.join((random.choice(tekens) for i in range(10)))
        spwd = password + salt
        strspwd = str(spwd).encode()
        hpwd = hashlib.sha256(strspwd).hexdigest()


        cursor.execute("INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s)", (username, hpwd, salt, hint))
        db.commit()
        start()

        #print ("Wachtwoord:         ",password)
        #print ("Salt:               ",salt)
        #print ("Slatt + wachtwoord: ", spwd)
        #print ("Hash:               ", hpwd)
    
    def password_checker(pwd):
            pwd = pwd
            
            pwd_lijst = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/worst-passwords-2017-top100-slashdata.txt') 
            x = pwd_lijst.text
            find = x.find(pwd)

            cijfer_list = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            cijfer_list_string = str(cijfer_list)

            letter_test = not pwd.islower() and not pwd.isupper()
            lengte_test = len(pwd)
            cijfer_test = any(ele in pwd for ele in cijfer_list_string)
            leestekentest = set(string.punctuation)

            
            if find > -1:
                print("Het wachtwoord is gevonden in de lijst met onveilige wachtwoorden.")
                print ("Probeer het opnieuw...")
                print()
                time.sleep (2)
                accountmaken()

            elif letter_test == False:
                print ("Het wachtwoord bevat geen hoofdletter en/of kleine letter.")
                print ("Probeer het opnieuw...")
                print()
                time.sleep (2)
                accountmaken()

            elif lengte_test < 10:
                print ("Het wachtwoord voldoet niet aan de minimale lengte.")
                print ("Probeer het opnieuw...")
                time.sleep (2)
                accountmaken()

            elif cijfer_test == False:
                print("Het wachtwoord heeft geen cijfer(s).")
                print("Probeer het opnieuw...")
                print()
                time.sleep (2)
                accountmaken()

            elif any(str in leestekentest for str in pwd):
                print("Het wachtwoord voldoet aan alle eisen.")
                print ()

            else: 
                print ("Het wachtwoord heeft geen leestekens.")
                print ("Probeer het opnieuw...")
                print ()
                time.sleep (2)
                accountmaken()

          

    print ("Password storage")
    print ()
    print ("1 - Inloggen")
    print ("2 - account maken")
    print ()
    print ("3  - stoppen")
    print ()
    keuze = input()

    if keuze == "1":
        inloggen()

    elif keuze == "2":
        accountmaken()

    elif keuze == "3":
        exit()


start()