'''
        A       
      A B A     
    A B C B A   
  A B C D C B A 
A B C D E D C B A 
'''

n = int(input("Enter the number of rows "))

for i in range(1, n+1): 
    ch = "A"
    # spaces
    for j in range(n - i):
        print(" ", end = " ")
    
    # alphabets
    for j in range(n-i+1, n+i):
        print(ch, end = " ")
        if j < n:
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)

    
    # spaces
    for j in range(n+i, 2*n-1):
        print(" ", end = " ")

    print()