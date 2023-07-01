n = int(input())

i = 1
while i * i <= n:
    if n % i == 0:
        print(i, end = " ")
        if n//i != i:
            print(n//i, end = " ")
    i += 1
print()