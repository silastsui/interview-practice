class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}
        for letter in s:
            if letter not in letters.keys():
                letters[letter] = 1
            else:
                letters[letter] += 1
        for letter in t:
            if letter not in letters.keys():
                return False
            else:
                letters[letter] -= 1
        for keys in letters:
            if letters[keys] != 0:
                return False
        return True
