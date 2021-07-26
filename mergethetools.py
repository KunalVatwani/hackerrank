def merge_the_tools(s, n):
    # your code goes here
    length = len(s)//n
    for i in range(0,len(s),n):
        l=[]
        for j in range(i,n+i):
            if s[j] not in l:
                l.append(s[j])
        ss = ''.join(l)
        print(ss)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)