number = abs(int(input()))

def dig(n):
    count = 0
    while abs(n) > 0:
        n = n//10
        count += 1
    return count

print(dig(number))