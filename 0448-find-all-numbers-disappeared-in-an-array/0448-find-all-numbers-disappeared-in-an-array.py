class Solution:
    def findDisappearedNumbers(self, nums):

        # The variable going to used for iteration
        length_of_nums = len(nums)

        # Array for the result
        result = []

        # Number counting board
        count_numbers = [0 for i in range(length_of_nums)]

        # Count the numbers
        for element in nums:
            count_numbers[element - 1] += 1

        for i in range(length_of_nums):
            result.append(i + 1) if count_numbers[i] == 0 else None

        return result
