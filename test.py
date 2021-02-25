import os

print ("Type s of l")
var = input()
cmd = "ls -{0}".format(var)
test = os.system(cmd)
print
