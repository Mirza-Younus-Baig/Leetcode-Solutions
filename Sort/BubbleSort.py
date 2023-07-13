# arr = list(map(int, input().split()))

arr = [12, 13, 5, 7, 9, 1]
# arr = [1,2,3,4,5,6]

didSwap = 0

for i in range(len(arr) - 1):

    for j in range(len(arr) - i - 1):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            didSwap = 1

    if didSwap == 0:
        break

    print("Step ", i, " : ", arr)   
    
print("Sorted array:",arr)

print("Time Complexity: O(n2)")