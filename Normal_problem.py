n=int(input())
for i in range(n):
    s=input()
    s=list(s)
    for i in range(len(s)):
        if s[i] == 'q':
            s[i]='p'
        elif s[i] == 'p':
            s[i]='q'
    s.reverse()
    print("".join(s))
