"""
Problem description:

https://leetcode.com/problems/camelcase-matching/

A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.



Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation:
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation:
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation:
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".



Note:

    1 <= queries.length <= 100
    1 <= queries[i].length <= 100
    1 <= pattern.length <= 100
    All strings consists only of lower and upper case English letters.


"""
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        subpatterns = self.prepare_pattern(pattern)
        subqueries = self.prepare_queries(queries)

        results = []

        for subquery in subqueries:
            if len(subquery) != len(subpatterns):
                results.append(False)
                continue

            index = 0
            stop_index = len(subquery)
            result = True
            while index < stop_index and result:
                word = subquery[index]
                for letter in subpatterns[index]:
                    ind = word.find(letter)
                    if ind == -1:
                        result = False
                        break
                    word = word[ind + 1:]
                index += 1
            results.append(result)
        return results


    def prepare_pattern(self, pattern):
        patter_string = "".join(["_ " +letter if letter.isupper() else letter for letter in pattern ])
        list_of_subpatterns = patter_string.split("_")[1:]
        return list_of_subpatterns

    def prepare_queries(self, queries):
        list_of_subqueries = []
        for query in queries:
            list_of_subqueries.append(self.prepare_pattern(query))
        return list_of_subqueries





if __name__ == "__main__":

    object = Solution()

    queries = ["FooBar" ,"FooBarTest" ,"FootBall" ,"FrameBuffer" ,"ForceFeedBack"]
    pattern = "FB"
    assert object.camelMatch(queries, pattern) == [True ,False ,True ,True ,False]

    queries = ["FooBar" ,"FooBarTest" ,"FootBall" ,"FrameBuffer" ,"ForceFeedBack"]
    pattern = "FoBa"
    assert object.camelMatch(queries, pattern) == [True ,False ,True ,False ,False]

    queries = ["FooBar" ,"FooBarTest" ,"FootBall" ,"FrameBuffer" ,"ForceFeedBack"]
    pattern = "FoBaT"
    assert object.camelMatch(queries, pattern) == [False ,True ,False ,False ,False]

    queries = ["CompetitiveProgramming" ,"CounterPick" ,"ControlPanel"]
    pattern = "CooP"
    assert object.camelMatch(queries, pattern) == [False ,False ,True]
