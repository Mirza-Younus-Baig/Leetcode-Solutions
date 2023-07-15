arr = [4,7,6,3,98,43,22,5,1]

# arr = [1,2,3,4,5,6,7,8,9]

for i in range(1, len(arr) - 1):
    if arr[i-1] > arr[i]:
        print("Not in Ascending Order")
        break
else:
    print("Ascending Order")