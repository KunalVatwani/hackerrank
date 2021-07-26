t = int(input())
for i in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
# ls=[1,2,3]
    base = 2**31
    for i in range(len(ls)):
        if (ls[0]>=ls[len(ls)-1] and ls[0]<=base):
            base = ls.pop(0)
        elif (ls[len(ls)-1]>=ls[0] and ls[len(ls)-1]<=base):
            base = ls.pop(len(ls)-1)
        else:
            print("No")
            break
    else:
        print("Yes")