from operator import mul, truediv, sub, add
import re
s = '((1+2*3- 5) * (4-(3 - 20 + 4) - 23 * (7 + 28)) + 102 *3)/ 5 '
print(eval(s))
result = list(filter(lambda x: x != '', re.split(
    r'(\d+|[()])', re.sub(r'\s', '', s))))


def parentheses(s):
    my_list = []
    # temp1, temp2 = 0, 0
    count = 0
    for i in list_index_start:
        for j in range(i+1, len(s)):
            if s[j] == '(':
                count += 1
            elif s[j] == ')' and count:
                count -= 1
                continue
            if s[j] == ')' and not count:
                return i, j
    # for i in list_index_start[::-1]:
    #     for j in range(i+1, len(s)):
    #         if j >= temp1 and j <= temp2:
    #             continue
    #         if s[j] == ')':
    #             my_list.append((i+1, j))
    #             temp1 = i
    #             if j < temp2:
    #                 pass
    #             else:
    #                 temp2 = j
    #             break
    # print(my_list)


# print(parentheses(result))


def calculation(s, i=0, j=len(s)):
    def replacement(f):
        nonlocal i, j
        n = str(f(float(s[i - 1]), float(s[i + 1])))
        del s[i - 1:i + 2]
        s.insert(i - 1, n)
        i -= 1
        j -= 2
    # global ret
    # if len(s) == 1:
    #     return s
    if '(' not in s:
        while j - i > 1:
            temp = i
            j = len(s)
            while i < j:
                if s[i] == '*':
                    replacement(mul)
                elif s[i] == '/':
                    replacement(truediv)
                i += 1
            i = temp
            while i < j:
                if s[i] == '+':
                    replacement(add)
                elif s[i] == '-':
                    replacement(sub)
                i += 1
            return s
    if '(' in s:
        global test
        ret = parentheses(s)
        if ret[1] < test:
            test = ret[1]
            del s[ret[1]]
            del s[ret[0]]
            return s[:ret[0]] + calculation(s[ret[0]:ret[1]-1]) + s[ret[1]-1:]
        calculation(s[ret[0]:ret[1]-1])
        # l = ret.pop()
        # i = l[0]
        # j = ret[-1][1]
        # ret.pop()

        # del s[ret[0] + 1]
        # del s[ret[0] - 1]


test = len(result)
list_index_start = [i for i in range(len(result)) if s[i] == '(']
# print(len(result))
print(*calculation(result))
""" def calculation_expression(s, i=0, j=len(result)):
    index_list = parentheses(s)
    countdown = len(index_list) // 2
    if len(s) > 1 and countdown:
        while countdown:
            s = calculation(
                s, index_list[countdown - 1], index_list[countdown])
            index_list = parentheses(s)
            countdown = len(index_list) // 2
            del s[index_list[countdown]]
            del s[index_list[countdown - 1]]
            index_list = parentheses(s)
            countdown = len(index_list) // 2
    if len(s) > 1 and not countdown:
        s = calculation(s, i, j=len(s))
        return ''.join(s) """


# s = calculation_expression(result)
# print(s)
