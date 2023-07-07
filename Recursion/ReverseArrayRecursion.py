arr = [x for x in range(10)]

print("Before reversal ", arr)
def rev(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]

    rev(arr, l + 1, r - 1)

rev(arr, 0, len(arr) - 1)
print("After reversal ", arr)