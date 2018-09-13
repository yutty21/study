#!/usr/bin/python3
import re

line = "Cats are12222 smarter than dogs"

matchObj = re.match(r'(.*) are(.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(1))
else:
    print("No match!!")