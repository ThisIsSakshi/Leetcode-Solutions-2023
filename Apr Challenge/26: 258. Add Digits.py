# problem:
# https://leetcode.com/problems/add-digits/

# solution:
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))==1:
            num=sum(map(int,str(num)))