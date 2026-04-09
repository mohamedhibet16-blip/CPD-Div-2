n=int(input())
s=input()
alphabet="abcdefghijklmnopqrstuvwxyz"
s=s.lower()
no=0
yes=0
for i in alphabet:
    if i not in s:
        no+=1
    else:
        yes+=1
if no > 0:
    print("NO")
else:
     print("YES")
