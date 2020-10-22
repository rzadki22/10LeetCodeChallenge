"""
Problem description:

https://leetcode.com/problems/sequential-digits/

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]



Constraints:

    10 <= low <= high <= 10^9



"""


class Solution:
    def sequentialDigits(self, low, high):
        full_seq = self.generator()
        seq = list(filter(lambda x: low <= x <= high, full_seq))
        return seq

    def generator(self):
        range_10 = [10**x for x in [1,2,3,4,5,6,7,8,9]]
        seq_nums = []
        for i_ten_power in range(len(range_10) - 1):
            first = [str(digit + 1) for digit in range(len(str(range_10[i_ten_power])))]
            first = int("".join(first))
            add = "1" * len(str(range_10[i_ten_power]))
            add = int("".join(add))
            num = first
            seq_nums.append(num)
            while num < range_10[i_ten_power + 1]  and str(num)[-1] != "9" :
                num += add
                seq_nums.append(num)
        return seq_nums




if __name__ == "__main__":

    object = Solution()
    low = 100
    high = 300
    object.sequentialDigits(low, high)

    low = 100
    high = 300
    assert object.sequentialDigits(low, high) == [123,234]

    low = 1000
    high = 13000
    assert object.sequentialDigits(low, high) == [1234,2345,3456,4567,5678,6789,12345]



