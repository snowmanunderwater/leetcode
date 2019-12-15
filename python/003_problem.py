# 3. Longest Substring Without Repeating Character
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s: str) -> int:
    stack = []
    current = []

    for index, character in enumerate(s):
        if character not in current:
            current.append(character)
        else:
            stack.append(current.copy())
            current = list(current[current.index(character)+1:])
            current.append(character)

    stack.append(current)

    if not stack:
        stack.append(s)

    return len(max(stack, key=lambda x: len(x)))


assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring(" ") == 1
assert lengthOfLongestSubstring("") == 0
assert lengthOfLongestSubstring("au") == 2
assert lengthOfLongestSubstring("dvdf") == 3
