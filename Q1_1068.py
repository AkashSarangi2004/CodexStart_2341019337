"""
 * Name: Akash Sarangi
 * Reg No: 2341019337
 * PS LINK: https://cses.fi/problemset/task/1068/
"""

n=int(input())
print(n, end=" ")
while n!=1:
    if n%2==0:
        n=n//2
        
    else:
        n=(n*3)+1
    
    print(n, end=" ")    

