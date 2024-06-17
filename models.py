import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
for i , j in enumerate(lst_in):
    if j == " ":
        lst_in.pop(i)
        lst_in.insert("-",i)
print(lst_in)