"""
 * Name: Akash Sarangi
 * Reg No: 2341019337
 * PS LINK: https://cses.fi/problemset/task/1069/
"""
n=input().strip()
char=n[0]
count=1
mcount=1
for i in range(1, len(n)):
    if n[i]==char:
        count += 1
    else:
        mcount= max(mcount,count)
        char=n[i]
        count=1
mcount= max(mcount,count)
print(mcount)