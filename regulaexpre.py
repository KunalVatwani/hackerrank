import re
n = int(input())
output=[]
for i in range(n):

    p = input()
    try:
        re.compile(p)
        output.append(True)
    except re.error:
        output.append(False)
for i in output:
    print(i)