"""
 * Name: Akash Sarangi
 * Reg No: 2341019337
 * PS LINK: https://cses.fi/problemset/task/1623/
"""
n = int(input())
w= list(map(int, input().split()))
def min_difference(index, a, b):
    if index >= len(w):
        return abs(a - b)
    return min(min_difference(index + 1, a + w[index], b), min_difference(index + 1, a, b + w[index]))
print(min_difference(0, 0, 0))