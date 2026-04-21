import datetime
FILE_NAME = "./sample.txt"

text = ""
try:
    text = open(FILE_NAME, "r")
except:
    print("CANT FIND THE FILE")
print(text)