import datetime
FILE_NAME = "./sample.txt"

text = ""
try:
    text = open(FILE_NAME, "r")
except:
    print("CANT FIND THE FILE")
print(text)

log = f"output: {text}"

with open("log.txt", "a") as f:
    f.write(f"{datetime.datetime.now()} {log}")