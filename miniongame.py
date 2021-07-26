# key = input()
# key = key.lower()
def minion(key):
    Stuart = 0
    Kevin = 0
    
    for i in range(len(key)):
        # for j in range(i,len(key)+1):
        #     sub=key[i:j]
        #     if (sub!=''):
        sub=key[i]
        increment = len(key)-i
        # print(sub, increment)
        if(sub=='A' or sub=='E' or sub=='I' or sub=='O' or sub=='U'):
                Kevin+=increment
            
        else:  
                Stuart+=increment

    # print('Stuart {}'.format(Stuart))
    # print('Kevin{}'.format(Kevin))
    if (Stuart>Kevin):
        print('Stuart {}'.format(Stuart))
    elif (Stuart<Kevin):
        print('Kevin {}'.format(Kevin))
    elif (Stuart==Kevin):
        print('Draw')

if __name__=="__main__":
    key = input()
    minion(key)