class Solution(object):
    def stringAnagram(n):
        """
        :type n: List[str]
        :rtype: List[str]
        """

        anagrams = {}
        for word in n:
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in anagrams.keys():
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)

        sorted_words = []
        for anagram_list in anagrams:
            for word in sorted(anagrams[anagram_list]):
                sorted_words.append(word)

        return sorted_words
