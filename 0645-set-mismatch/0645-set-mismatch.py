class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # Declare a dictionary to find the repeated and omitted cases
        nums_dict = {}

        # Count the elements in `nums` and record the cases into `nums_dict`
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        repeated = None
        omitted = None
        # Iterate a number range to find the solution
        for testcase in range(1, len(nums) + 1):
            # Find the omitted number
            if testcase not in nums_dict:
                omitted = testcase
            # Find the repeated number
            if nums_dict.get(testcase, 0) == 2:
                repeated = testcase

        # Return the list of repeated and omitted number
        return [repeated, omitted]

