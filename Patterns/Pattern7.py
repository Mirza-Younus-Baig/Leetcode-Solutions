'''
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
'''

n = int(input("Enter the number of rows "))

for i in range(n):
    for j in range(2*n - 1):
        if j < n - i - 1 or j >= n + i:
            print(" ", end = " ")
        else:
            print("*", end = " ")
    print()