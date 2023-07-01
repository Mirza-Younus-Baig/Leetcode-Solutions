# name = input("Enter the name ")
# n = int(input("Enter the value of n "))

def printName(name, n):
    if n == 0:
        return
    print(n, name)
    printName(name, n-1)

def print1toN(n):
    if n == 0:
        
        return
    print1toN(n-1)
    print(n)

def printNto1(n):
    if n == 0:
        
        return
    print(n)
    print1toN(n-1)
    

# print names n times
# printName(name, n)

# print from 1 to 10
# print1toN(10)

# print from 10 to 1
# printNto1(10)