n = int(input())
a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')
if a<=n<=z or A<=n<=Z:
    print('Буква', chr(n))
    print(a)
else:
    print('Символ', chr(n))