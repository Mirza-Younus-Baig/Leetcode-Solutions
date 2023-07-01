n = int(input("enter the input "))

# Parametarized way
def fact1(n, res):
    if n == 1:
        print(res)
        return 
    fact1(n-1, res * n)

fact1(n, 1)

# Functional Way

def fact2(n):
    if n == 1:
        return 1
    return n * fact2(n - 1)

print(fact2(n))