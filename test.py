import subprocess

text = input()
ping = subprocess.check_output (['echo', text])
print (ping)
