class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        maxConsec = 0
        for n in nums:
            if n == 1:
                consec +=1 
                if consec > maxConsec:
                    maxConsec = consec
            else:
                consec = 0
        return maxConsec
        