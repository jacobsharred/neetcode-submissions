class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        consecHighest = 0
        for n in nums:
            if n == 1:
                consec += 1;
                if consec > consecHighest:
                    consecHighest = consec
            elif n != 1:
                consec = 0
        return consecHighest
