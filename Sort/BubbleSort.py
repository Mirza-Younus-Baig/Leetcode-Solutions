# arr = list(map(int, input().split()))

arr = [12, 13, 5, 7, 9, 1]

for i in range(len(arr) - 1):

    for j in range(len(arr) - i - 1):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Step ", i, " : ", arr)   
print("Sorted array:",arr)

print("Time Complexity: O(n2)")