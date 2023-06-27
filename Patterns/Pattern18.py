'''
E 
D E 
C D E 
B C D E 
A B C D E
'''

n = int(input("Enter the number of rows "))


for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ord('A') + n - i + j - 1), end = " " )
    print()