"""
 * Name: Akash Sarangi
 * Reg No: 2341019337
 * PS LINK: https://cses.fi/problemset/task/1755/
"""
s = input()
single = []
pairs = []
for char in s:
    if char in single:
        single.remove(char)
        pairs.append(char)
    else:
        single.append(char)
r = ''.join(pairs) + ''.join(single) + ''.join(pairs)[::-1]
if r == r[::-1]:
    print(r)
else:
    print("NO SOLUTION")