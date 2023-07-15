# arr = list(map(int, input().split()))

arr = [4,7,6,3,98,43,22,5,1]

firstLargest, secondLargest = float('-inf'), float('-inf')

firstSmallest, secondSmallest = float('inf'), float('inf')


for i in range(len(arr)):
    # Smallest Elements
    if arr[i] < firstSmallest:
        firstSmallest, secondSmallest = arr[i], firstSmallest
    elif arr[i] < secondSmallest:
        secondSmallest = arr[i] 

    # Largest Elements
    if arr[i] > firstLargest:
        firstLargest, secondLargest = arr[i], firstLargest
    elif arr[i] > secondLargest:
        secondLargest = arr[i]

print("First Largest: {}\nSecond Largest: {}".format(firstLargest, secondLargest))
print("First Smallest: {}\nSecond Smallest: {}".format(firstSmallest, secondSmallest))