
from typing import List

# Using Array Hashing
def arrayHashing(n: List[int]) -> List[int]:
    arr = [0 for _ in range(len(n))]
    for i in n:
        arr[i] += 1
    
    return arr


# Using Dictionary Hashing
def dictionaryHashing(n: List[int]) -> dict:
    dicH = dict()
    for i in n:
        dicH[i] = dicH.get(i, 0) + 1
    
    return dicH


# Using hash()
def hashh(n: List[int]) -> dict:
    dictt = dict()
    for i in n:
        dictt[hash(i)] = dictt.get(hash(i), 0) + 1
    for ind, val in dictt.items():
        print(ind, val)
    return dictt



if __name__ == "__main__":
    # Read input
    # n = list(map(int, input("Enter the elements").split()))
    # query = list(map(int, input("Enter the query elements").split()))
    n = [1, 4, 3, 2, 4, 6, 4, 8, 6, 4, 3, 3, 2, 3, 4, 5, 6]
    query = [2, 3, 4]

    arr = arrayHashing(n)
    dicH = dictionaryHashing(n)
    dictt = hashh(n)

    for i in query:
        print("Array Hashing: ", i, arr[i])
        print("Dictionary Hashing: ", i, dicH[i])
        print("Hashing Function: ", i, dictt[i])
