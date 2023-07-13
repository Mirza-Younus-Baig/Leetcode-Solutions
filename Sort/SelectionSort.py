# arr = list(map(int, input().split()))
arr = [12, 13, 5, 7, 9, 1]

for i in range(len(arr) - 1):
    minInd = i
    for j in range(i , len(arr)):
        if arr[j] < arr[minInd]:
            minInd = j
    arr[i], arr[minInd] = arr[minInd], arr[i]

print(arr)

print("Space Complexity: O(n2)")