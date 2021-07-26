a=set(map(int, input().split()))
n=int(input())
output=[]
for i in range(n):
    b=set(map(int, input().split()))
    output.append(b)
c=0
for i in output:
    if (a.issuperset(i) and a!=i):
        c+=1

if (c==len(output)):
    print(True)
else:
    print(False)