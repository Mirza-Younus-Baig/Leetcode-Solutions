arr = [5,1,3,7,8,2,9]

# selection sort
# Basic idea: Find the minimum element in the unsorted portion of the array 
# and swap it with the first unsorted element. 
# Repeat until the array is fully sorted.


# for i in range(len(arr) - 1):
#     minInd = i
#     for j in range(i, len(arr)):
#         if arr[j] < arr[minInd]:
#             minInd = j
#     # print(minInd)
#     arr[i], arr[minInd] = arr[minInd], arr[i]

# print(f"Selection Sort: {arr}")

# Bubble Sort
# Basic idea: Iterate through the array repeatedly, 
# comparing adjacent pairs of elements 
# and swapping them if they are in the wrong order. 
# Repeat until the array is fully sorted.


# for i in range(len(arr)):
#     for j in range(len(arr) - i - 1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(f"Bubble Sort: {arr}")

# Insertion Sort
# Basic idea: Build up a sorted subarray from left to right 
# by inserting each new element into its correct position in the subarray. 
# Repeat until the array is fully sorted.

# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and key < arr[j]:
#         arr[j + 1] = arr[j]
#         j -= 1
#     arr[j + 1] = key

# print(f"Insertion Sort: {arr}")

# Merge Sort

low, high = 0, len(arr) - 1
for i in range(len(arr)):
    while low < high:
        mid = (high - low)//2 + low
        

