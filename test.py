from ldap3 import Server, Connection, ALL
server =Server('192.168.195.144', get_info=ALL)
conn = Connection(server, 'cn=admin,dc=rouwens,dc=com', 'welkom01', auto_bind=True)
conn.add('cn=Lieke Rouwens,ou=gebruikers,dc=rouwens,dc=com', 'inetOrgPerson', {'givenName': 'Lieke', 'sn': 'Rouwens', 'uid': 'lrouwens'})
