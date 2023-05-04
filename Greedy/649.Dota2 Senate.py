

# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         if len(senate) < 2:
#             return "Radiant" if senate == "R" else "Dire"
#         senate = list(senate)
#         senate1 = senate[:]
#         for ind in range(len(senate)-1):
#             if senate[ind] == "R" and "D" in senate1:
#                 senate1.remove("D")
#             elif senate[ind] == "D" and "R" in senate1:
#                 senate1.remove("R")
#         # print(senate)
#         if senate1.count("R") == 0:
#             return "Dire"
#         else:
#             return "Radiant"
        

# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         senate = list(senate)
#         ind = 0
#         while True:
            
#             if senate.count("R") == 0 or senate.count("D") == 0:
#                 return "Radiant" if senate.count("D") == 0 else "Dire" 
#             if senate[ind] == "R" and senate.count("D") != 0:
#                 senate[senate.index("D")] = 0
#             elif senate[ind] == "D"  and senate.count("R") != 0:
#                 senate[senate.index("R")] = 0
#             print(senate)
#             ind = (ind + 1) % len(senate)
        
# Inspired by solutions
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        r_arr = [i for i in range(len(senate)) if senate[i]=='R']
        d_arr = [j for j in range(len(senate)) if senate[j]=='D']
        
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d:
                r_arr.append(n + r)
            else:
                d_arr.append(n + d)
                
        return 'Radiant' if r_arr else 'Dire'
    

res = Solution()

t = 5
inp = "DDRRRDR"

print(res.predictPartyVictory(inp))