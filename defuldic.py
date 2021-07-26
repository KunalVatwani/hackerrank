import collections
ls = list(map(int, input().split()))
l=[]
l1=[]
for i in range(ls[0]):
    l.append(input())
for i in range(ls[1]):
    l1.append(input())

d=collections.defaultdict(lambda:-1)
# l=['a','b','c','a','d','a']
for i in range(len(l)):
    if l[i] in d:
        d[l[i]]+=' {}'.format(i+1)
    else:
        d[l[i]]=str(i+1)

for i in l1:
    print(d[i])