class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        keyboard = [list("qwertyuiop"), list("asdfghjkl"), list("zxcvbnm")]
        good_words = []
        for word in words:
            for keyboard_row in keyboard:
                if set(list(word.lower())).issubset(keyboard_row):
                    good_words.append(word)

        return good_words
