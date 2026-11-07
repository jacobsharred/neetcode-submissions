class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            latest = []

            for j in range(i + 1, len(arr)):
                latest.append(arr[j])

            if latest:
                greatest = max(latest)
            else:
                greatest = -1

            arr[i] = greatest

        return arr