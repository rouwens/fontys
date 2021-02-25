import os
#import subprocess
import linecache

#ipv4 = os.system("ifconfig wlp2s0 | grep inet | awk '$1 == 'inet' { print $2 }'")
#ipv4 = subprocess.run(["ifconfig wlp2s0 | grep inet | awk '$1 == 'inet' { print $2 }'"])
#test = subprocess.run(["ifconfig wlp2s0 | grep inet | awk '$1 == "inet" { print $2 }'""])
os.system("bash import.bash")

ip = linecache.getline('info.txt', 1)
netmask = linecache.getline('info.txt', 2)
gateway = linecache.getline('info.txt', 3)

print ("IP address: ", ip)
print ("Netmask: ", netmask)
print ("Gatway: ", gateway)
