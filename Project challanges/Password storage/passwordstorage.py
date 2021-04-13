import random
import time
import requests
import string
import mysql.connector as mysql
import re
import hashlib
import base64


# Ik gebruik functie in fuctie naar functie. Als tip heb ik moet ik return gaan gebruiken om terug te gaan.

# Moet nog in een config bestand komen 

db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "passwordmanager"
    )

#db = mysql.connect(
    #host = "192.168.178.200",
    #user = "daan",
    #passwd = "welkom01",
    #database = "passwordmanager"
    #)

cursor = db.cursor()

def start():

    def wachtwoorden(username):
        username = username

        print ()
        print ("Wachtwoorden beheer")
        print ()
        print ("1 - lijst zien")
        print ("2 - Wachtwoord zien")
        print ("3 - Toevoegen aan de lijst")
        print ("4 - Veranderen aan de lijst")
        print ("5 - Item verwijderen uit de lijst")
        print ("")
        print ("6 - Stoppen")
        keuze = input()

        if keuze == "1":
            print()
            show = """SELECT * FROM `%s`;"""
            cursor.execute(show, (username,))

            sql = cursor.fetchall()
            print ("ID      Gebruikersnaam      Wachtwoord (gecrypt)     Omschrijving")  
            for row in sql:
                print(row, '\n')
            input("Druk op enter om verder te gaan...")

        elif keuze =="2":
            print ()
            print ("Vul hierin het ID waarvan je het wachtwoord wilt zien.")
            id = input() 

            # Ophalen van het wachtwoord uit de database
            getpwd = """SELECT password FROM `%s` WHERE `ID` = %s"""
            cursor.execute(getpwd, (username, id,))
            fetch = cursor.fetchall()
            clean = str(fetch)
            pwd = clean[3:-4]

            # Het decoderen van het opgehaalde wachtwoord
            b64_str = pwd
            b64_str = b64_str.encode('ascii')
            b64_bytes = base64.b64decode(b64_str)
            decode_str = b64_bytes.decode('ascii')
            
            print ()
            print ("Het wachtwoord bij ID " + id + " is " + decode_str)
            time.sleep(2)
            wachtwoorden(username)

        
        elif keuze == "3":
            print ()
            print ("Vul hier de titel in van het item.")
            titel = input ()
            print ()
            print ("Wat is de gebruikersnaam?")
            gebruikersnaam = input()
            print ()
            print ("Vul het wachtwoord in")
            pwd1 = input()
            print ()
            print ("Vul het wachtwoord nog een keer in ter controle")
            pwd2 = input()

            if pwd1 == pwd2:
                print ()
            
            else:
                print ("Wachtwoorden kloppen niet. Probeer het opnieuw....")
                time.sleep(2)
                wachtwoorden(username)
        
            print ("Vul hier een omschrijving in van het item.")
            omschrijving = input ()

            str_pwd = pwd1
            str_to_bytes = str_pwd.encode("ascii")
            bytes_to_base64= base64.b64encode(str_to_bytes)
            base64_output = bytes_to_base64.decode('ascii')

            cursor.execute("INSERT INTO `%s` VALUES (NULL, %s, %s, %s, %s)", (username, titel, gebruikersnaam, base64_output, omschrijving))
            db.commit()

            print ("De gegevens zijn omgeslagen")
            time.sleep(2)    

        elif keuze == ("4"):
            print ()
            print ("Wat is het ID van het item dat je wilt aanpassen?")
            id = input()
            print ()
            print ("Wat wil je aanpassen? (naam/gebruikersnaam/wachtwoord/omschrijving)")
            keuze = input()

            if keuze == "naam":
                print ()
                print ("Wat word de nieuwe naam van het item?")
                name = input()
                cursor.execute("UPDATE `%s` SET `name` = %s WHERE `%s`.`ID` = %s;", (username, name, username, id))
                db.commit()
                print()
                print ("Naam is aangepast")
                time.sleep(2)
                wachtwoorden(username)

            if keuze == "gebruikersnaam":
                print ()
                print ("Wat word de nieuwe gebruikersnaam?")
                gebruikersnaam = input()
                cursor.execute("UPDATE `%s` SET `username` = %s WHERE `%s`.`ID` = %s;", (username, gebruikersnaam, username, id))
                db.commit()
                print ()
                print ("Gebruikernaam is aangepast")
                time.sleep(2) 

            
            elif keuze == "wachtwoord":
                print ()
                print ("Vul hier het nieuwe wachtwoord in")
                pwd1 = input()
                print ()
                print ("Vul hier nog een keer het wachtwoord ter controle")
                pwd2 = input()
                
                if pwd1 == pwd2:
                    print ()
                    str_pwd = pwd1
                    str_to_bytes = str_pwd.encode("ascii")
                    bytes_to_base64= base64.b64encode(str_to_bytes)
                    base64_output = bytes_to_base64.decode('ascii')

                    cursor.execute("UPDATE `%s` SET `password` = %s WHERE `%s`.`ID` = %s;", (username, base64_output, username, id))
                    db.commit()
                    print ()
                    print ("Het wachtwoord is bijgewerkt")
                    time.sleep(2)

                        
                else:
                    print ()
                    print ("Wachtwoorden komen niet overeen")
                    time.sleep(2)
                
                wachtwoorden(username)
            
            elif keuze == "omschrijving":
                print ()
                print ("Wat word de nieuwe omschrijving?")
                omschrijving = input()
                cursor.execute("UPDATE `%s` SET `sum` = %s WHERE `%s`.`ID` = %s;", (username, omschrijving, username, id))
                db.commit()
                print ()
                print ("Omschrijving is aangepast")
                time.sleep(2) 
            
            else:
                print ("Input niet herkend. Probeer het opnieuw...")
                time.sleep(2)
            
            wachtwoorden(username)
        
        elif keuze == ("5"):
            print ()
            print ("Vul het ID in van het item dat je wilt verwijderen.")
            id = input()
            print ()
            print ("Weet je het zeker? (y/n)")
            bevestiging = input()
            if bevestiging == "y":
                cursor.execute("DELETE FROM `%s` WHERE ID = %s ;", (username, id))
                db.commit()
                print ("Item is verwijderd...")
                time.sleep(2)
                wachtwoorden(username)
            
            else:
                print ("De wijzegingen zijn niet aangebracht. De input klopt niet. Probeer het opnieuw....")
                time.sleep(2)
                wachtwoorden(username)
        
        elif keuze == ("6"):
            exit()
        
        else:
            print ("Keuze niet herkend...")
            time.sleep(2)
            wachtwoorden(username)



   # Dit is de functie dat gaat over alle instellingen van de gebruiker.
    def instellingen(username):
        username = username

        print()
        print ("Instellingen")
        print ("")
        print ("1 - Database droppen")
        print ("2 - Account verwijderen")
        print ("")
        print ("3 - Terug")
        print ("")
        keuze = input()

        if keuze == "1":
            print ("Weet je het zeker? Er is geen mogelijkheid om je gegevens later te herstellen. (y/n)")
            delvraag1 = input()
        
            if delvraag1 == "y":
                print ()
                print ("Type VERWIJDER in om de database definitief te verwijderen")
                delvraag2 = input()

                if delvraag2 == "VERWIJDER":
                    
                    state = """SELECT `added_table` FROM `accounts` WHERE `username` = %s"""
                    cursor.execute(state, (username,))
                    sql = cursor.fetchall()
                    sqlstring = str(sql)
                    state = re.sub(r'[^\w\s]', '', sqlstring)

                    if state == "1":
                    
                        dropdatabase = "DROP TABLE `passwordmanager`.`%s`;"
                        cursor.execute(dropdatabase, (username,))
                        
                        onetonullsql = """UPDATE `accounts` SET `added_table` = '0' WHERE `accounts`.`username` = %s;"""
                        cursor.execute(onetonullsql, (username,))

                        print ()
                        print ("Database is verwijderd")
                        time.sleep(2)
                        funcgebruiker(username, db, cursor)
                
                    
                    else:
                        print ("Database bestaat niet. Dus valt er niks te verwijderen ;)")
                        time.sleep(2)
                        funcgebruiker(username,db,cursor)
                  
                else:
                    print ("Input verkeerd. De database is niet verwijderd")
                    time.sleep(2)
                    instellingen(username)
                           

        elif keuze == "2":
            print ("Weet je het zeker? Er is geen mogelijkheid om je gegevens later te herstellen. (y/n)")
            delvraag1 = input()
        
            if delvraag1 == "y":
                print ()
                print ("Type VERWIJDER in om je account definitief te verwijderen")
                delvraag2 = input()

                if delvraag2 == "VERWIJDER":
                    print()
                    fetchid = """SELECT ID FROM `accounts` WHERE `username` = %s"""
                    cursor.execute(fetchid, (username,))
                    sql = cursor.fetchall()
                    sqlstring = str(sql)
                    id = re.sub(r'[^\w\s]', '', sqlstring)

                    
                    dropdatabase = "DROP TABLE `passwordmanager`.`%s`;"
                    cursor.execute(dropdatabase, (username,))
                    dropaccount = """DELETE FROM `accounts` WHERE `accounts`.`username` = %s;"""
                    cursor.execute(dropaccount, (username,))                    
                    print ("Gebruiker is verwijderd.")
                    time.sleep (2)
                    start ()

        elif keuze == "3":
            funcgebruiker(username, db, cursor)
        
        else:
            print ("Keuze niet herkend. Probeer het opnieuw...")
            time.sleep(2)
            instellingen(username)

    def funcgebruiker (username, db, cursor):
        username = username
        db = db
        cursor = cursor

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
            wachtwoorden(username)
        
        elif keuze == "2":
            instellingen(username)
        
        elif keuze == "3":
            exit()
        
        elif keuze == "init":
            cursor.execute("CREATE TABLE `passwordmanager`.`%s` ( `ID` INT(255) NOT NULL , `name` TEXT NOT NULL , `username` TEXT NOT NULL , `password` TEXT NOT NULL ) ENGINE = InnoDB", (username,))
            db.commit()
            cursor.execute("UPDATE `accounts` SET `added_table` = '0' WHERE `accounts`.`username` = %s;", (username,))
            db.commit()
            #switch = """UPDATE `accounts` SET `added_table` = '0' WHERE `accounts`.`username` = %s;"""
            #cursor.execute(switch, (username,))
            #createtable = """CREATE TABLE `passwordmanager`.`%s` ( `ID` INT(255) NOT NULL , `name` TEXT NOT NULL , `username` TEXT NOT NULL , `password` TEXT NOT NULL ) ENGINE = InnoDB;"""
            #cursor.execute(createtable, (username,))
            print ()
            print ("Database aangemaakt")
            time.sleep(2)
            funcgebruiker (username, db, cursor)


    # Dit is het login scherm
    def inloggen(db, cursor):
        db = db
        cursor = cursor
 
        cursor = db.cursor()
        
        print ()
        print ("Geef je gebruikersnaam op")
        username = input()

        # Checkt of gebruikersnaam bestaat in de database

        gebruikerSQL = """SELECT * FROM `accounts` WHERE `username` = %s"""
        cursor.execute(gebruikerSQL, (username,))
        gebruiker = cursor.fetchall()

        if gebruiker == []:
            print ("Gebruiker niet gevonden")
            time.sleep(2)
            start()


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

        # Hier word gekeken van de net gemaakte hash overedenkomt met de hash in de database
        if pwd2check == hpwd:
            print ("De login gegevens zijn juist")
                    
        
        else:
            print ("De login gegevens zijn niet juist. Probeer het opnieuw...")
            time.sleep(2)
            inloggen(db, cursor)
        
        funcgebruiker (username, db, cursor,)



    def accountmaken(db, cursor):
        db = db
        cursor = cursor
        
        cursor = db.cursor()

        print ("Wat is de gebruikersnaam?")
        username = input()
        print ()
        gebruikerSQL = """SELECT * FROM `accounts` WHERE `username` = %s"""
        cursor.execute(gebruikerSQL, (username,))
        gebruiker = cursor.fetchall()

        if gebruiker != []:
            print ("Gebruikersnaam bestaat al. Probeer het openieuw...")
            time.sleep(2)
            accountmaken(db, cursor)
        
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
            accountmaken(db, cursor)

        password_checker(pwd = password)

        print ("Vul hier een hint in van het wachtwoord")
        hint = input()
        print ()
        
        if hint == password:
            print("Hint mag het wachtwoord niet bevatten")
            print("Probeer het opnieuw....")
            time.sleep (2)
            accountmaken(db, cursor)

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
            accountmaken(db, cursor)

        # Hier word een salt gegenereerd en gelijk daarna gehasht met het wachtwoord.
        tekens = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        salt = ''.join((random.choice(tekens) for i in range(10)))
        spwd = password + salt
        strspwd = str(spwd).encode()
        hpwd = hashlib.sha256(strspwd).hexdigest()

        addedtable = str(0)

        cursor.execute("INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, %s)", (username, hpwd, salt, hint, addedtable))
        db.commit()
        start()
    
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
                accountmaken(db, cursor)

            elif letter_test == False:
                print ("Het wachtwoord bevat geen hoofdletter en/of kleine letter.")
                print ("Probeer het opnieuw...")
                print()
                time.sleep (2)
                accountmaken(db, cursor)

            elif lengte_test < 10:
                print ("Het wachtwoord voldoet niet aan de minimale lengte.")
                print ("Probeer het opnieuw...")
                time.sleep (2)
                accountmaken(db, cursor)

            elif cijfer_test == False:
                print("Het wachtwoord heeft geen cijfer(s).")
                print("Probeer het opnieuw...")
                print()
                time.sleep (2)
                accountmaken(db, cursor)

            elif any(str in leestekentest for str in pwd):
                print("Het wachtwoord voldoet aan alle eisen.")
                print ()

            else: 
                print ("Het wachtwoord heeft geen leestekens.")
                print ("Probeer het opnieuw...")
                print ()
                time.sleep (2)
                accountmaken(db, cursor)

          

    print ("Password storage")
    print ()
    print ("1 - Inloggen")
    print ("2 - account maken")
    print ()
    print ("3  - stoppen")
    print ()
    keuze = input()

    if keuze == "1":
        inloggen(db, cursor)

    elif keuze == "2":
        accountmaken(db, cursor)

    elif keuze == "3":
        exit()


start()