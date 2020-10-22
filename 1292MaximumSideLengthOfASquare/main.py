"""
Problem description:

https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

Example 1:

Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3

Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2



Constraints:

    1 <= m, n <= 300
    m == mat.length
    n == mat[i].length
    0 <= mat[i][j] <= 10000
    0 <= threshold <= 10^5

"""

# Submit na leetcode wysypywał się na TimeExceed, ale nie wiem jak to zoptymalizować

import numpy as np

class Solution:
    def maxSideLength(self, mat, threshold):

        ## First step: prepare input data
        # Convert nested lists to array matrix
        matrix = np.array(mat)
        # Rotate matrix to to be always horizontal (i.e. lower side length always be vertical
        if matrix.shape[0] > matrix.shape[1]:
            matrix = matrix.T
        height = min(matrix.shape)
        width = max(matrix.shape)

        for dim in range(height, 0, -1):
            for iter_width in range(0, width - dim + 1, 1 ):
                for iter_height in range(0, height - dim + 1, 1 ):
                    submatrix = matrix[iter_height : iter_height + dim, iter_width : iter_width + dim ]
                    sum_of_submatrix = submatrix.sum()
                    if sum_of_submatrix <= threshold:
                        return dim
        else:
            return 0


if __name__ == "__main__":

    object = Solution()

    mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
    threshold = 4
    assert object.maxSideLength(mat, threshold) == 2

    mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
    threshold = 1
    assert object.maxSideLength(mat, threshold) == 0

    mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
    threshold = 6
    assert object.maxSideLength(mat, threshold) == 3


    mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
    threshold = 40184
    assert object.maxSideLength(mat, threshold) == 2







