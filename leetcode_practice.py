class Solution:
#     def lengthOfLongestSubstring(self,s):
#         s_length = len(s)
#         s_start = 0
#         answer = 0
#         check = []
#         for i in range(0,s_length):
#             for j in range(s_start,s_length):
#                 if s[j] not in check:
#                     check.append(s[j])
#                 elif s[j] in check:
#                     if len(check) > answer:
#                         answer = len(check)
#                     elif len(check) <= answer:
#                         pass
#                     check = []
#                     break
#             s_start+=1
#         if len(check) > answer:
#             answer = len(check)
#         return answer
    
# ########################################################################
#     def reverse(self,x):
#         # 解法1
#         answer = int(str(x)[::-1].replace("-",""))

#         # 解法2
#         # x_list = [i for i in str(x)]
#         # x_list.reverse()
#         # answer = ""
#         # for j in x_list:
#         #     if j == "-":
#         #         pass
#         #     else:
#         #         answer+=j
#         # answer = int(answer)

#         # 不變的return判斷
#         if answer < -2**31 or answer > 2**31 -1:
#             return 0
#         elif x < 0:
#             return -answer
#         else:
#             return answer

# ########################################################################
    # def twoSum(self ,nums:list ,target:int):
    #     for a in nums:
    #         b = target - a
    #         a_index = nums.index(a)
    #         a_count = nums.count(a)
    #         if a == b:
    #             if a_count > 1:
    #                 nums.remove(a)
    #                 return [a_index,nums.index(b)+1]
    #         else:
    #             if b in nums:
    #                 return [a_index,nums.index(b)]

# ########################################################################
    # def divide(self ,dividend:int ,divisor:int):
    #     import math
    #     answer = dividend / divisor
    #     if answer > 2**31 - 1:
    #         return 2**31 - 1
    #     elif answer < 0:
    #         if answer < -2**31:
    #             return -2**31
    #         return math.ceil(answer)
    #     return math.floor(answer)

# ########################################################################
    # def __init__(self):
    #     global np
    #     import numpy as np
    #     self.in_dict = {}
    #     self.average_time = {}

    # def checkIn(self ,id ,stationName ,t):
    #     if id not in self.in_dict :
    #         self.in_dict.update({id:[stationName,t]})

    # def checkOut(self ,id ,stationName ,t ):
    #     if id in self.in_dict:
    #         in_station = self.in_dict[id][0]
    #         in_time = self.in_dict[id][1]
    #         in_out_station = in_station + "_" + stationName
    #         travel_time = t - in_time
    #         if travel_time > 0:
    #             if in_out_station not in self.average_time:
    #                 self.average_time.update({in_out_station:[travel_time]})
    #             else:
    #                 self.average_time[in_out_station].append(travel_time)
    #             del self.in_dict[id]

    # def getAverageTime(self ,startStation ,endStation ):
    #     in_out_station = startStation + "_" + endStation
    #     if in_out_station in self.average_time:
    #         return np.mean(self.average_time[in_out_station])
    
# ########################################################################
    # def longestPalindrome(self ,s):
    #     s_start = 1
    #     s_end = len(s)
    #     while True:
    #         s_slice = s_end
    #         for i in range(0,s_start):
    #             a = s[i:s_slice]
    #             if a == a[::-1]:
    #                 return a
    #             s_slice+=1
    #         s_start+=1
    #         s_end-=1

# ########################################################################
    def next_question(self):
        pass
