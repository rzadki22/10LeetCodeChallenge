"""
Problem description:
https://leetcode.com/problems/shifting-letters/

848. Shifting Letters
Medium

We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation:
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.

Note:

    1 <= S.length = shifts.length <= 20000
    0 <= shifts[i] <= 10 ^ 9
"""
# 46 / 46 test cases passed, but took too long.

class Solution(object):

    def __init__(self):
        self.ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        self.ALPHABET_PLACES = {val: index for index, val in enumerate(self.ALPHABET)}
        self.PLACES_ALPHABET = {index: val for index, val in enumerate(self.ALPHABET)}

    def prepare_shifts(self, shifts):
        cumul_shifts = []
        for index in range(0, len(shifts)):
            cumul_shifts.append(sum(shifts[index:]))
        return cumul_shifts

    def convert_string_to_list(self, S):
        list_of_places = []
        for letter in S:
            list_of_places.append(self.ALPHABET_PLACES[letter])
        return list_of_places

    def convert_list_to_string(self, list_of_places):
        list_of_signs = []
        for place in list_of_places:
            list_of_signs.append(self.PLACES_ALPHABET[place])
        decoded_string = "".join(list_of_signs)
        return decoded_string

    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """

        cumul_shifts = self.prepare_shifts(shifts)
        list_of_places = self.convert_string_to_list(S)
        list_of_places_shifted = [sum(x) % 26 for x in zip(list_of_places, cumul_shifts)]
        decoded_string = self.convert_list_to_string(list_of_places_shifted)

        return decoded_string


if __name__ == "__main__":
    obj = Solution()

    S = "abc"
    shifts = [3, 5, 9]
    assert obj.shiftingLetters(S, shifts) == "rpl"

    S = "z"
    shifts = [52]
    assert obj.shiftingLetters(S, shifts) == "z"







