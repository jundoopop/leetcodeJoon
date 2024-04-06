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

        result = [0, 0]
        while result[0] == 0 or result[1] == 0:
            # Iterate a number range to find the solution
            for testcase in range(1, len(nums) + 1):
                # Find the omitted number
                if testcase not in nums_dict:
                    result[1] = testcase
                # Find the repeated number
                if nums_dict.get(testcase) == 2:
                    result[0] = testcase

        # Return the list of repeated and omitted number
        return result

