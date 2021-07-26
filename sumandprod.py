import numpy 
n = int(input())
arr=numpy.array(list(map(int,input().split())))
for i in  range(n-1):
    a=list(map(int,input().split()))
    ar=numpy.array(a)
    arr=numpy.vstack((arr,ar))
# print(arr)
s=numpy.sum(arr,axis=0)
p=1
for i in s:
    p*=i
print(p)