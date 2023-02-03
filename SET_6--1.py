# Write a program to print each line of a file in reverse order. Also compute
# the number of characters, words and lines in a file.
with open("bin.txt", 'r') as f:
    F_lst = f.readlines()
f.close()
print("Reverse order:")
for i in reversed(F_lst):
    print(i.rstrip())
print(f"Number of lines: {len(F_lst)}")
c = 0
k = 0
for line in F_lst:
    line = line.strip('\n')
    words = line.split()
    c += len(words)
    k += len(line)
print("Number of words:", c)
print("Number of characters:", k + 1)

#
# Input file (ngit.txt):
#
# Neil Gogte Institute of Technology (NGIT).
# NGIT was established in year 2017.
# NGIT is one of the premier engineering colleges in the state of Telangana.
#
# output:
#
# Reverse order:
# NGIT is one of the premier engineering colleges in the state of Telangana.
# NGIT was established in year 2017.
# Neil Gogte Institute of Technology (NGIT).
# Number of lines: 3
# Number of words: 25
# Number of characters: 151