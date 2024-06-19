class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)  # k is for the return
        for i in range(len(nums)):
            if nums[i] == val:  # If the element is same as val
                k -= 1  # Remaining length would be decreased

        start_point = 0
        for i in range(k):  # Iterate for the number of valid elements
            # Start from the former's last index
            for j in range(start_point, len(nums)):
                start_point += 1
                # Swap with the current first `val` and nums[j]
                if nums[j] != val:  # Judge whether it should be removed
                    nums[i] = nums[j]
                    break

        return k
