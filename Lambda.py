# Mapping
print("Map")
def addition(a, b):
    return a + b

addition1 = lambda a, b: a+b
print(addition(1,2))
print(addition1(1,4))

oldList = list(range(10))
newList = list(map(lambda x: x * 2, oldList))

print(oldList)
print(newList)

# Filtering
print("Filtering")

ifEven = lambda x: x % 2 == 0
print(list(filter(ifEven, oldList)))

# Sorting
print("Sorting")
a = [(1,6), (2,2), (3,5), (7,8)]

print(sorted(a))
print(sorted(a, key = lambda x: x[1]))

# Reduce
from functools import reduce
print("Reduce")
print(reduce(lambda x,y: x+y, oldList))