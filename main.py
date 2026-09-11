"""
a = int(input())
if a < 3:
    print('a < 3')
elif a >= 3 and a % 2 == 0:
    print('a >= 3 and even')
else:
    print('no')

a = ''
if a:
    print('True')
else:
    print('False')
a = [[i for i in range(5)] for j in range(5)]
print(a)
x = 5
print(f"x = {x}")
y = 7.0
print(f"x = {x}, y = {y}")
pi = 3.14159265
print(f"{pi:.2f}")
"""
s = input()
l = len(s)
pali = True
mirror = True
mirror_still = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
mirror_world = [['E', '3'], ['J', 'L'], ['S', '2'], ['Z', '5']]

for i in range(l//2):
    if s[i] != s[-i-1]:
        pali = False
    if s[i] in mirror_still:
        if s[i] != s[-i-1]:
            mirror = False
    elif s[i] in [mirror_world[j][0] for j in range(3)]:
        for j in range(3):
            if s[i] == mirror_world[j][0] and s[-i-1] == mirror_world[j][1]:
                break
            else:
                mirror = False
    elif s[i] in [mirror_world[j][1] for j in range(3)]:
        for j in range(3):
            if s[i] == mirror_world[j][1] and s[-i-1] == mirror_world[j][0]:
                break
            else:
                mirror = False
    else:
        mirror = False
if s[l//2] not in mirror_still:
    mirror = False
if pali == False and mirror == False:
    print(f'{s} is not a palindrome')
elif pali == True and mirror == False:
    print(f'{s} is a regular palindrome')
elif pali == False and mirror == True:
    print(f'{s} is a mirrored string')
else:
    print(f'{s} is a mirrored palindrome')


