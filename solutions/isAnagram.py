"""Solution for problem https://leetcode.com/problems/valid-anagram/
The main idea is to count letters in each string and compare results.
"""
from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter, t_counter = Counter(s), Counter(t)
        for ch, count in s_counter.iteritems():
            if s_counter[ch] != t_counter[ch]:
                return False

        return len(s) == len(t)


if __name__ == '__main__':
    import checker
    cases = (
        {'args': ("anagram", "nagaram"), 'result': True},
        {'args': ("rat", "car"), 'result': False},
    )
    checker.check(Solution().isAnagram, cases)
