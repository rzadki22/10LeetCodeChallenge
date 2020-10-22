"""
Problem description:
https://leetcode.com/problems/h-index/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.


"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse=True)

        for index in range(1, len(citations) + 1):
            bigger_than_index = list(map(lambda x: x >= index, citations[:index]))
            lower_than_index = list(map(lambda x: x <= index, citations[index:]))
            if (all(bigger_than_index) and all(lower_than_index)):
                return index
        else:
            return 0


if __name__ == "__main__":
    obj = Solution()

    citations = [3, 0, 6, 1, 5]
    assert obj.hIndex(citations) == 3

    citations = [3, 3, 3, 3, 3]
    assert obj.hIndex(citations) == 3

    citations = [0, 0]
    assert obj.hIndex(citations) == 0

    citations = []
    assert obj.hIndex(citations) == 0




