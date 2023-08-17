class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        for letter in t:
            if letter not in s or s.count(letter)<t.count(letter):
                return letter

