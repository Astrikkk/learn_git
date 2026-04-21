import datetime

FILE_NAME = "./sample.txt"

try:
    with open(FILE_NAME, "r") as file:
        text = file.read() 
except FileNotFoundError:
    print("CAN'T FIND THE FILE")
    text = "FILE NOT FOUND"  

log = f"output: {text}"

with open("log.txt", "a") as f:
    f.write(f"{datetime.datetime.now()} {log}\n")