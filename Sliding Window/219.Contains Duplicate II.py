from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        # Create an empty set to store the elements
        # An alternative approach is to use dictionary to store the {val: ind} pair
        li = set()
        
        # Iterate until the length of the array
        for i in range(len(nums)):
            
            # If the current element is already in the set, return True
            if nums[i] in li:
                return True

            # Add the current element to the set
            li.add(nums[i])

            # Remove the left element if the size of set > k
            if len(li) > k:
                li.remove(nums[i-k])

        # Return False if there are no duplicates
        return False



if __name__ == "__main__":
    res = Solution()
    inp = [0,1,2,3,2,5]
    k = 3

    print(res.containsNearbyDuplicate(inp, k))