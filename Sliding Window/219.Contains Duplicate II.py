from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # create an empty set to store the elements
        li = set()
        # loop through the array
        for i in range(len(nums)):
            # if the current element is already in the set, return True
            if nums[i] in li:
                return True
            # otherwise, add the current element to the set
            li.add(nums[i])
            # if the size of the set exceeds k, remove the oldest element
            if len(li) > k:
                li.remove(nums[i-k])
        # if no duplicate is found, return False
        return False



if __name__ == "__main__":
    res = Solution()
    inp = [0,1,2,3,2,5]
    k = 3

    print(res.containsNearbyDuplicate(inp, k))