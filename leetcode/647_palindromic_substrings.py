class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # naive O(n^3) solution
        count = 0

        for i in range(len(s)+1):
            for j in range(i):
                if s[i:j] == s[i:j][::-1]:
                    count += 1

        return count

    def countSubstrings2(self, s):
        # center expansion O(n^2) solution
        n = len(s)
        count = 0
        for center in range(2*n - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count

    def countSubstrings3(self, s):
        # manacher's algorithm, O(n) solution
        def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in xrange(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S))
