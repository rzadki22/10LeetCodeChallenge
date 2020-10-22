"""
Problem description:

https://leetcode.com/problems/partition-labels/

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so
that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like >> "ababcbacadefegde", "hijhklij" << is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.

Ma nastapic rozdzielenie stringa na mozliwie duzo podstringow w ktorych beda rozne litery.

"""

class Solution:
    def partitionLabels(self, S):
        # First step: make list of individual characters
        characters = set(S)
        # Second step: make dict of indices (like coordinates in one dimensional space) where characters occurs
        coors_basket = {}
        for character in characters:
            index_list = [i for i, x in enumerate(S) if x == character]
            coors_basket[character] = index_list
        # Third step: fullfill the ranges between boudnary indices
        for char in characters:
            coors_basket[char] = list(range(min(coors_basket[char]), max(coors_basket[char]) + 1))
        # Fourth step: find common elements in lists by finding intersection between character spaces and partitions
        # and iteratively wide partitions and then again check intersections with other char-ranges etc.
        number = self.segragate_partitions(coors_basket)
        return number

    def segragate_partitions(self, basket):
        popped = list(basket.keys())
        partitions = {}
        i = 1
        while popped != []:
            partitions[i] = basket[popped[0]]
            popped.remove(popped[0])
            while True:
                to_rmv = []
                for key in popped:
                    if self.intersection(partitions[i], basket[key]):
                        partitions[i].extend(basket[key])
                        to_rmv.append(key)
                for rmv in to_rmv:
                     popped.remove(rmv)
                if not to_rmv:
                    break
            i += 1

        # Fifth step: preparing demanded ouput:
        partitions = [list(set(val)) for key, val in partitions.items()]
        partitions.sort(key=lambda x: x[0])
        number = [len(x) for x in partitions]
        return number

    def intersection(self, list_1, list_2):
        list_3 = [value for value in list_1 if value in list_2]
        if list_3:
            return True
        else:
            return False


if __name__ == "__main__":
    #S = "ababcbacadefegdehijhklij"
    S = "babacdeeed"
    # S = "caedbdedda"
    object = Solution()
    result = object.partitionLabels(S)
    print(result)


