# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import itertools


def letterCombinations(digits):
    if digits == "":
        return []

    alphabet = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    args = map(alphabet.get, digits)

    return list(map(''.join, itertools.product(*args)))


assert letterCombinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
