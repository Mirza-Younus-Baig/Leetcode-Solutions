# class FrequencyTracker:
    
#     def __init__(self):
#         self.arr = {}
        
#     def add(self, number: int) -> None:
#         if number in self.arr:
#             self.arr[number] += 1
#         else:
#             self.arr[number] = 1

#     def deleteOne(self, number: int) -> None:
#         if number in self.arr:
#             self.arr[number] -= 1
            
#             if self.arr[number] == 0:
#                 del self.arr[number]
        


#     def hasFrequency(self, frequency: int) -> bool:
#         if frequency in self.arr.values():
#             return True
#         return False

class FrequencyTracker:
    def __init__(self):
        self.values = {}
        self.frequencies = {}

    def add(self, number):
        if number not in self.values:
            self.values[number] = 0
        self.values[number] += 1
        frequency = self.values[number]
        if frequency not in self.frequencies:
            self.frequencies[frequency] = set()
        self.frequencies[frequency].add(number)
        print(frequency)
        if frequency > 1:
            self.frequencies[frequency - 1].remove(number)
            if len(self.frequencies[frequency-1]) == 0:
                del self.frequencies[frequency-1]


    def deleteOne(self, number):
        if number in self.values:
            frequency = self.values[number]
            self.frequencies[frequency].remove(number)
            if len(self.frequencies[frequency]) == 0:
                del self.frequencies[frequency]
            self.values[number] -= 1
            if self.values[number] == 0:
                del self.values[number]
            else:
                frequency = self.values[number]
                if frequency not in self.frequencies:
                    self.frequencies[frequency] = set()
                self.frequencies[frequency].add(number)

    def hasFrequency(self, frequency):
        return frequency in self.frequencies



obj = FrequencyTracker()
obj.add(5)
obj.add(5)
print(obj.hasFrequency(1))
print(obj.hasFrequency(2))
