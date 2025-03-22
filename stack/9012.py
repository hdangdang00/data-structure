# 9012. 괄호 https://www.acmicpc.net/problem/9012
# 시간 복잡도: O(n * m), 공간 복잡도: O(n * m)

n = int(input())
s_list = list()

for _ in range(n):
    s_list.append(input())

for s in s_list:
    stack = list()
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                stack.append(ch)
                break
    print("YES" if not stack else "NO")