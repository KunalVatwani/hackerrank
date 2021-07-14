l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input())

if (n==1):
    print(l[0])
else :
    for i in range(1,n+1):
        s=''
        for j in range(i):
            v = n-j-1
            if(v>0):
                s+=l[v]
                s+='-'
            if (v==0):
                s1 = s + 'a-'
            else:
                s1=s
           
            rev = s1[::-1]
            rev1 = rev[3:]
            s1+=rev1
        print(s1.center(4*n-3,'-'))


    for i in range(n-1,0,-1):
        s=''
        for j in range(i):
            v = n-j-1
            if(v>0):
                s+=l[v]
                s+='-'
            if (v==0):
                s1 = s + 'a-'
            else:
                s1=s
           
            rev = s1[::-1]
            rev1 = rev[3:]
            s1+=rev1
        print(s1.center(4*n-3,'-'))