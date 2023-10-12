"""
 * Name: Akash Sarangi
 * Reg No: 2341019337
 * PS LINK: https://cses.fi/problemset/task/1622/
"""
str = input()
letters = list(str)
words = set()
def alphy(word, letters):
    if len(letters) == 1:
        words.add(word + letters[0])
    else:
        for i in range(len(letters)):
            alphy(word + letters[i], letters[0:i] + letters[i+1:])
alphy("", letters)
print(len(words))
print("\n".join(sorted(words)))