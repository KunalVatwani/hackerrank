import collections
n = int(input())
deq = collections.deque()
for i in range(n):
    ls = input().split()
    if (ls[0]=='append'):
        deq.append(int(ls[1]))
    elif (ls[0]=='appendleft'):
        deq.appendleft(int(ls[1]))
    elif (ls[0]=='pop'):
        deq.pop()
    elif (ls[0]=='popleft'):
        deq.popleft()
for i in range(len(deq)-1):
    print(deq[i], end=' ')
print(deq[len(deq)-1])
