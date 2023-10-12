"""
 * Name: Akash Sarangi
 * Reg No: 2341019337
 * PS LINK: https://cses.fi/problemset/task/1618/
"""
n = int(input())
c = 0
i = 5
while(n/i>=1):
    c+=int(n/i)
    i*=5
print(c)