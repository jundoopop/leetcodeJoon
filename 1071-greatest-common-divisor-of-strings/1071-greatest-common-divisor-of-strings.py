import math


class Solution:
    # Get maximum multiple
    #
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        max_common_divisor = math.gcd(len(str1), len(str2))
        # Initialize a list to store common divisors
        list_common_divisors = [
            number_to_test  # If the number is a common divisor,
            for number_to_test in range(
                1, max_common_divisor + 1
            )  # Count from 1 to the maximum common divisor
            if max_common_divisor % number_to_test
            == 0  # If the number is a common divisor
        ]

        # Check if the common divisor is a common multiple of str1 and str2
        for element in list_common_divisors[
            ::-1
        ]:  # Start from the largest common divisor
            if (
                str1[:element] * (len(str1) // element) == str1
                and str1[:element] * (len(str2) // element) == str2
            ):  # If the common divisor is a common multiple of str1 and str2
                return str1[:element]

        return (
            ""  # if there is no common multiple of str1 and str2, return empty string
        )
