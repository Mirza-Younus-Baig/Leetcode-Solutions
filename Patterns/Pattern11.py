'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
'''

n = int(input("Enter the number of rows "))

val = 0
for i in range(1, n+1):
    val = val ^ i%2
    for j in range(i):
        print(val, end = " ")
        val = 1 ^ val
        
    print()