n = 5

# Parametarized
# Approach 1
def sumN1(n, sums):
    if n == 0:
        print(sums)
        return

    sumN1(n-1, sums + n)

sumN1(n, 0)

# Functional  

def sumN2(n):
    if n == 0: 
        return 0

    return n + sumN2(n-1)

print(sumN2(n))