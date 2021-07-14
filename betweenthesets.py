# a = [3,4]
# b = [24,48]
# lo = max(a)
# hi = min(b)
# #print(lo,hi)
# c=0
# for i in range(lo,hi+1):
#     for j in a:
#         if(i%j!=0):
#             break
#     else :
#         for k in b:
#             if(k%i!=0):
#                 break
#         else :
#             print(i)
#             c+=1

# print(c)
s='abcdefgh'
r = s[::-1]
r = r[1:len(r)]
print(r)