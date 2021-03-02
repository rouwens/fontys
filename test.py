import string 
pwd="hello."
leestekentest = set(string.punctuation)
if any(str in leestekentest for str in pwd):
    print ("invalid")
else:
    print("valid")