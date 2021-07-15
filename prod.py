import itertools
input1 = input()
input2 = input()
lis1 = input1.split()
lis2 = input2.split()
o=itertools.product(lis1,lis2)

out = list(o)

for i in range(len(out)-1):
    print(out[i],end=' ')
print(out[len(out)-1])
