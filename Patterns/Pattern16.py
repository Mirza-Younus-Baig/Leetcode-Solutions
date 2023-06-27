'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''

n = int(input("Enter the number of rows "))

for i in range(n):
    for j in range(i+1):
        print(chr(ord('A') + i), end = " ")
    print()