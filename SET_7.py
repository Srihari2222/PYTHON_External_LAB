# Say you have the boring task of finding every phone number and email address
# in a long web page or document. Write a program to search for the phone
# numbers and email addresses from a given text file and store them in a
# separate text file.


import re

def Email(email):
    return re.match("\S+@\S+",email)

def phone(ph):
    return re.match("(\+91\-[98765]{1}[0-9]{9})",ph)
listEmail=[]
listPh=[]
with open("input.txt",'r') as fr,open("output.txt",'w') as fw:
    for line in fr:
        words=line.split()
        for word in words:
            if Email(word):listEmail.append(word)
            elif phone(word):listPh.append(word)
    fw.write("\n")
    fw.write("Mail IDs:\n")
    for i in listEmail:fw.write(i+"\n")
    fw.write("\n")
    fw.write("Phone Numbers:\n")
    for i in listPh:fw.write(i+"\n")
print(f"{len(listEmail)} emails collected!")
print(f"{len(listPh)} phone numbers collected!")

#
# sample input file:
#
# input.txt
#
# K. Sudheer Kumar    Asst. Professor     sudheerkumar19@gmail.com    +91-9948486011
# abcdef          Asst. Professor     dfkasdjfklsdj@gmail.com     +91-9324521664
# ijklmm          Asst. Professor     dfjisdioejrieroandcxsxz@gmail.com   +91-8946127845
#
# sample output file:
#
# output.txt
#
# Mail IDs:
# sudheerkumar19@gmail.com
# dfkasdjfklsdj@gmail.com
# dfjisdioejrieroandcxsxz@gmail.com
#
# Phone Numbers:
# +91-9948486011
# +91-9324521664
# +91-8946127845
#
#
# 3 emails collected!
# 3 phone numbers collected!