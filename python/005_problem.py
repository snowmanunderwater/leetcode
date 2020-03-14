# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
"""Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""

# def longestPalindrome(s: str) -> str:
#     if not s:
#         return ""
#     if len(s) == 1:
#         return s
#     ans = []
#     for i, character in enumerate(s):
#         for sub in range(i+1, len(s)+1):
#             if s[i:sub] == s[i:sub][::-1]:
#                 ans.append(s[i:sub])
#     if not ans:
#     	return ""
#     return max(ans, key=lambda x: len(x))


def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        odd = palindromeAt(s, i, i)
        even = palindromeAt(s, i, i + 1)

        res = max(res, odd, even, key=len)
    return res


# starting at l,r expand outwards to find the biggest palindrome
def palindromeAt(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


assert longestPalindrome("babad") == "bab" or "aba"
assert longestPalindrome("cbbd") == "bb"
assert longestPalindrome("babab") == "babab"
assert longestPalindrome("") == ""
assert longestPalindrome("a") == "a"
assert longestPalindrome("ac") == "a"
assert longestPalindrome(
    "aksdrjhgsdrhugsjdhgkjsdflgsaaxxaajdhgsdhg") == "aaxxaa"
