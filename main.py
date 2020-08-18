Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@cool-pants 
cool-pants
/
GitUpscale-MLH
Private
forked from HackclubVIT/GitUpscale-MLH
0
0
3
Code
Pull requests
Actions
Projects
Security
Insights
Settings
GitUpscale-MLH/main.py /
@cool-pants
cool-pants First Commit
Latest commit e0d8674 1 hour ago
 History
 1 contributor
43 lines (31 sloc)  632 Bytes
  
from os import system, name
from time import sleep


def clear():
    if name == "nt":
        _ = system("cls")


for i in range(4):
    print("Searching for Hackers.")
    sleep(0.5)
    clear()
    print("Searching for Hackers .")
    sleep(0.5)
    clear()
    print("Searching for Hackers  .")
    sleep(0.5)
    clear()

clear()

s = "Found all Hackers"
d = "Displaying"
dl = list(d)

# print(dl)

print(s)


clear()
print(dl)
with open("names.txt", "r", encoding="utf8") as file:
    txtname = file.read()

lstname = txtname.replace("\n", "$")
name = lstname.split("$")
name.pop()

for i in name:
    print(i)
    sleep(0.4)
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
