# https://leetcode.com/problems/valid-parentheses/


def check_brackets(stroka):
    acc = []

    for char in stroka:
        if char in ')]}' and len(acc) == 0:
            return False
        if char in '({[':
            acc.append(char)
        elif char in ')]}' and len(acc) > 0:
            if char == ')' and acc[-1] != '(':
                return False
            elif char == ']' and acc[-1] != '[':
                return False
            elif char == '}' and acc[-1] != '{':
                return False
            acc.pop()

    return False if acc else True


assert check_brackets(')(') == False
assert check_brackets('(()') == False
assert check_brackets('({)()})') == False
assert check_brackets('(3+[2*3)]') == False
assert check_brackets(']') == False
assert check_brackets('[]') == True
assert check_brackets('[([])]') == True
assert check_brackets('(5+5)/[4+4]*{2*2}') == True
