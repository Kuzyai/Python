from operator import mul, truediv, sub, add
import re
s = '((1+2*3- 5) * (4-(3 - 20 + 4) - 23 * (7 + 28)) + 102 *3)/ 5 '
print(eval(s))
result = list(filter(lambda x: x != '', re.split(
    r'(\d+|[()])', re.sub(r'\s', '', s))))


def parentheses(s):
    list_index_start = [i for i in range(len(s)) if s[i] == '(']
    my_list = []
    for i in list_index_start[::-1]:
        for j in range(i+1, len(s)):
            if s[j] == ')':
                return i+1, j


def calculation(s, i=0, j=len(result)):
    def replacement(f):
        nonlocal i, j
        n = str(f(float(s[i - 1]), float(s[i + 1])))
        del s[i - 1:i + 2]
        s.insert(i - 1, n)
        i -= 1
        j -= 2
    while '(' in s[i:j]:
        ret = parentheses(s)
        calculation(s, ret[0], ret[1])
        del s[ret[0] + 1]
        del s[ret[0] - 1]
    while j - i > 1:
        temp = i
        while i < j:
            if s[i] == '*':
                replacement(mul)
            elif s[i] == '/':
                replacement(truediv)
            i += 1
            if len(s) == 1:
                return s
        i = temp
        while i < j:
            if s[i] == '+':
                replacement(add)
            elif s[i] == '-':
                replacement(sub)
            i += 1
            if len(s) == 1:
                return s
    return s


print(*calculation(result))
