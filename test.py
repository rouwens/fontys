import pyad
x = pyad.set_defaults(ldap_server="192.168.195.123", username="cn=Administrator,cn=Users,dc=rouwens,dc=com", password="W3lk0m!")
print (x)