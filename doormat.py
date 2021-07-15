s='.|.'
n = int(input('Enter the number of lines you want'))
for i in range(1,(n+1)//2):
    line = (2*i-1)*s
    print(line.center(3*n,'-'))
print("WELCOME".center(3*n,'-'))
for i in range((n-1)//2,0,-1):
    line = (2*i-1)*s
    print(line.center(3*n,'-'))