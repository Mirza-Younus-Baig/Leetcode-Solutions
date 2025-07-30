class Solution:

    def mergeSort(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)

    def merge(self,arr, low, mid, high):
        res = []
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        while i <= mid:
            res.append(arr[i])
            i += 1
        while j <= high:
            res.append(arr[j])
            j += 1
        
        for i in range(low, high + 1):
            arr[i] = res[i - low]
    

if __name__ == "__main__":
    obj = Solution()
    arr = [12, 13, 5, 7, 9, 1]
    print("Before sorting: ", arr)
    obj.mergeSort(arr, 0, len(arr) - 1)
    print("After sorting: ", arr)

