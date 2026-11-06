class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for n in nums.copy():
            if n == val:
                nums.remove(n)
            else:
                k +=1
                
        return k