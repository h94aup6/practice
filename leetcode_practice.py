class Solution:
    # # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    # def lengthOfLongestSubstring(self,s):
    #     s_length = len(s)
    #     s_start = 0
    #     answer = 0
    #     check = []
    #     for i in range(0,s_length):
    #         for j in range(s_start,s_length):
    #             if s[j] not in check:
    #                 check.append(s[j])
    #             elif s[j] in check:
    #                 if len(check) > answer:
    #                     answer = len(check)
    #                 elif len(check) <= answer:
    #                     pass
    #                 check = []
    #                 break
    #         s_start+=1
    #     if len(check) > answer:
    #         answer = len(check)
    #     return answer
    
########################################################################
    # # https://leetcode.com/problems/reverse-integer/
    # def reverse(self,x):
    #     # 解法1
    #     answer = int(str(x)[::-1].replace("-",""))

    #     # 解法2
    #     # x_list = [i for i in str(x)]
    #     # x_list.reverse()
    #     # answer = ""
    #     # for j in x_list:
    #     #     if j == "-":
    #     #         pass
    #     #     else:
    #     #         answer+=j
    #     # answer = int(answer)

    #     # 不變的return判斷
    #     if answer < -2**31 or answer > 2**31 -1:
    #         return 0
    #     elif x < 0:
    #         return -answer
    #     else:
    #         return answer

########################################################################
    # # https://leetcode.com/problems/two-sum/
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

########################################################################
    # # https://leetcode.com/problems/divide-two-integers/
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

########################################################################
    # # https://leetcode.com/problems/design-underground-system/
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
    
########################################################################
    # # https://leetcode.com/problems/longest-palindromic-substring/
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

########################################################################
    # # https://leetcode.com/problems/regular-expression-matching/
    # def isMatch(self,s,p):
    #     import re
    #     if p == ".*" \
    #         or p == f"{s[0]}*" \
    #             or p == f"{s[0]}.*" \
    #                 or s == p:
    #         return True
    #     if s in re.findall(p,s):
    #         return True
    #     else:
    #         return False

########################################################################
    # # https://leetcode.com/problems/add-two-numbers/description/
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    # def addTwoNumbers(self, l1:ListNode, l2:ListNode):
    #     l1_num = ""
    #     while True:
    #         try:
    #             l1_num += str(l1.val)
    #             l1 = l1.next
    #         except AttributeError:
    #             l1_num = l1_num[::-1]
    #             break

    #     l2_num = ""
    #     while True:
    #         try:
    #             l2_num += str(l2.val)
    #             l2 = l2.next
    #         except AttributeError:
    #             l2_num = l2_num[::-1]
    #             break
        
    #     l1_num = str(int(l1_num) + int(l2_num))
    #     for i in range(len(l1_num)):
    #         if i == 0:
    #             answer = Solution.ListNode(l1_num[i])
    #         else:
    #             answer = Solution.ListNode(l1_num[i],answer)
            
    #     return answer
        
########################################################################
    # # https://leetcode.com/problems/multiply-strings/description/
    # def multiply(self, num1:str, num2:str):
    #     a,b = 0,0
    #     for i in num1:
    #         check = 0
    #         while str(check) != i:
    #             check += 1
    #         if a == 0:
    #             a += check
    #         else:
    #             a = a*10 + check

    #     for j in num2:
    #         check = 0
    #         while str(check) != j:
    #             check += 1
    #         if b == 0:
    #             b += check
    #         else:
    #             b = b*10 + check
        
    #     return str(a*b)

########################################################################
    # # https://leetcode.com/problems/valid-sudoku/description/
    # def isValidSudoku(self, board:list):
    #     i = 0
    #     while i < 9:
    #         # 判斷九宮格
    #         if i == 2 or i == 5 or i == 8:
    #             k = 0
    #             while k < 9:
    #                 z = [board[z][zz] for z in range(i+1-3,i+1) for zz in range(k,k+3) if board[z][zz] != "."]
    #                 for zz in z:
    #                     if z.count(zz) > 1:
    #                         return False
    #                 k += 3

    #         for x in range(9):
    #             if board[i][x] == ".":
    #                 pass
    #             else:
    #                 # 判斷橫行
    #                 if board[i].count(board[i][x]) > 1:
    #                     return False

    #                 # 判斷直列
    #                 y = [board[j][x] for j in range(9)]
    #                 if y.count(board[i][x]) > 1:
    #                     return False
    #         i += 1
    #     return True
        
########################################################################
    # # https://leetcode.com/problems/max-points-on-a-line/
    # def maxPoints(self, points:list):
    #     if len(points) == 1:
    #         return 1
    #     elif len(points) == 2:
    #         return 2
        
    #     from fractions import Fraction
    #     i = 0
    #     formula_dict = {}
    #     while i < len(points):
    #         j = i + 1
    #         while j < len(points):
    #             if points[i][0] == points[j][0]:
    #                 answer_formula = f"x = {points[i][0]}"
    #             elif points[i][1] == points[j][1]:
    #                 answer_formula = f"y = {points[i][1]}"
    #             else:
    #                 a = Fraction((points[i][1] - points[j][1]),(points[i][0] - points[j][0]))
    #                 b = points[i][1] - (points[i][0] * a)
    #                 answer_formula = f"y = {a}x + {b}"
                
    #             if answer_formula not in formula_dict:
    #                 formula_dict.update({answer_formula:1})
    #             else:
    #                 formula_dict[answer_formula] += 1
    #             j += 1
    #         i += 1

    #     answer = 1
    #     z = max(formula_dict.values())
    #     while z != 0:
    #         z = z - answer
    #         answer += 1
    #     return answer

########################################################################
    # # https://leetcode.com/problems/find-the-highest-altitude/description/
    # def largestAltitude(self, gain:list):
    #     check = answer = 0
    #     for i in gain:
    #         check += i
    #         if check > answer:
    #             answer = check
    #     return answer

########################################################################
    # # https://leetcode.com/problems/basic-calculator/description/
    # def cal(self,cal_s):
    #     if "+" not in cal_s and "-" not in cal_s:
    #         return int(cal_s)
    #     if cal_s[0] == "-" and "+" not in cal_s[1:] and "-" not in cal_s[1:]:
    #         return int(cal_s)

    #     x = y = answer = 0
    #     while y < len(cal_s):
    #         if (cal_s[y] in "+-" and y != 0) or y == len(cal_s) - 1:
    #             if y == len(cal_s) - 1:
    #                 answer += int(cal_s[x:])
    #             else:
    #                 answer += int(cal_s[x:y])
    #                 x = y
    #         y += 1
    #     return answer
    
    # def calculate(self, s:str):
    #     s = s.replace(" ","")
    #     b = s.find(")")
    #     while b != -1:
    #         a = b
    #         while s[a] != "(":
    #             a -= 1
    #         s = s.replace(s[a:b+1],str(self.cal(s[a+1:b])))
    #         if "+-" in s:
    #             s = s.replace("+-","-")
    #         elif "--" in s:
    #             s = s.replace("--","+")
    #         b = s.find(")")
    #     return self.cal(s)

########################################################################
    # # https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     if len(word1) == 1:
    #         return word1 + word2

    #     x = 1
    #     for i in range(len(word2)):
    #         if x > len(word1):
    #             return word1 + word2[i:]
    #         else:
    #             word1 = word1[:x] + word2[i] + word1[x:]
    #         x += 2
    #     return word1            

########################################################################
    # # https://leetcode.com/problems/k-radius-subarray-averages/description/
    # # 方法一
    # def getAverages(self, nums:list, k:int):
    #     if k == 0:
    #         return nums
    #     elif k >= len(nums) / 2:
    #         return [-1] * len(nums)

    #     answer = []
    #     for i in range(k,len(nums) - k):
    #         if i == k:
    #             a = sum(nums[i-k:i+k+1])
    #         else:
    #             a = a - nums[i-k-1] + nums[i+k]
    #         answer.append(int(a / (k*2 + 1)))
    #     return [-1] * k + answer + [-1] * k

    # # 方法二
    # def getAverages(self, nums:list, k:int):
    #     if k == 0:
    #         return nums
    #     elif k >= len(nums) / 2:
    #         return [-1] * len(nums)

    #     answer = []
    #     i = 0
    #     while i + (k*2 + 1) <= len(nums):
    #         if i == 0:
    #             a = sum(nums[0:(k*2 + 1)])
    #         else:
    #             a = a - nums[i-1] + nums[i+(k * 2)]
    #         answer.append(int(a / (k*2 + 1)))
    #         i += 1
    #     return [-1] * k + answer + [-1] * k

########################################################################
    # # https://leetcode.com/problems/counting-bits/?envType=daily-question&envId=2023-09-01
    # def countBits(self, n:int) -> list[int]:
    #     answer = []
    #     for i in range(n+1):
    #         answer.append(bin(i).count("1"))
    #     return answer

########################################################################
    # # https://leetcode.com/problems/maximum-number-of-balls-in-a-box/submissions/1038438839/
    # def countBalls(self, lowLimit:int, highLimit:int) -> int:
    #     answer = {}
    #     for i in range(lowLimit, highLimit + 1):
    #         a = 0
    #         while i != 0:
    #             a += i % 10
    #             i = i // 10
    #         if a not in answer:
    #             answer[a] = 1
    #         else:
    #             answer[a] += 1
    #     return max(answer.values())
    
########################################################################
    def next_q(self):
        pass

