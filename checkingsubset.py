n=int(input())
output=[]
for i in range(n):
    uselessno1 = int(input())
    a=set(map(int, input().split()))
    uselessno2 = int(input())
    b=set(map(int, input().split()))
    output.append(a.issubset(b))

for i in output:
    print(i)