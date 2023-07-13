# arr = list(map(int, input().split()))

arr = [12, 13, 5, 7, 9, 1]

for i in range(len(arr)):
    j = i

    while j > 0 and arr[j - 1] > arr[j]:
        arr[j], arr[j-1] = arr[j - 1], arr[j]
        j -= 1
    
    print("Step {}: {}".format(i, arr))

print("Sorted Array: {}".format(arr))

