rm info.txt
ifconfig wlp2s0 | grep inet | awk '$1 == "inet" { print $2 }' >> info.txt
ifconfig wlp2s0 | grep inet | awk '$1 == "inet" { print $4 }' >> info.txt
ip r | grep default | awk '$1 == "default" { print $3 }' >> info.txt
