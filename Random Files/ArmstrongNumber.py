n = int(input())
temp = n
res = 0
while n > 0:
    res += (n%10) ** 3
    n //=10

print(True if res == temp else False)


