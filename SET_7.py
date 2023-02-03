# Say you have the boring task of finding every phone number and email address
# in a long web page or document. Write a program to search for the phone
# numbers and email addresses from a given text file and store them in a
# separate text file.


import re

with open("input.txt", 'r') as f, open("output.txt", 'r+') as fp:
    mlst = []
    plst = []
    for line in f:
        mtemp = re.findall('\S+@\S+', line)
        ptemp = re.findall('(\+91\-[98765]{1}[0-9]{9})', line)
        mlst.extend(mtemp)
        plst.extend(ptemp)
print("Mail IDs:")
for i in mlst:
    print(i)
print("\nPhone Numbers:")
for i in plst:
    print(i)
print("\n")
print(f"{len(mlst)} emails collected!")
print(f"{len(plst)} phone numbers collected")

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