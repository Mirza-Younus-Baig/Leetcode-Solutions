'''
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 
'''

n = int(input("Enter the number of rows "))


for i in range(1, n+1):
    # numbers
    for j in range(1, i + 1):
        print(j, end = " ")

    # space
    for j in range(i, 2*n - i):
        print(" ", end = " ")

    # numbers
    for j in range(2 * n - i, 2*n):
        print(2 * n - j, end = " ")
    
    print()