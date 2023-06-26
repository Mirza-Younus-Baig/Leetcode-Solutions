'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

n = int(input("Enter the value of n "))

for i in range(n):
    for j in range(1, n - i + 1):
        print(j, end = " ")
    print()