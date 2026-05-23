import re

#regex = "a*"
#regex = "(ab)*"
regex = '(a|b)c'
Text_words = ["", "ac", "bc", "c", "abc","a","b"]

for s in Text_words:
    if re.fullmatch(regex, s):
        print(f'"{s}" is Accepted')
    else:
        print(f'"{s}" is Rejected')
