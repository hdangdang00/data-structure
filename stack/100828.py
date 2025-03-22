# 10828. 스택 https://www.acmicpc.net/problem/10828
# 시간 복잡도: O(n), 공간 복잡도: O(n)

n = int(input())
stack = list()
result = list()

for _ in range(n):
    parts = input().split()
    if parts[0] == "push":
        num = parts[1]
        stack.append(num)
    elif parts[0] == "pop":
        result.append(-1 if not stack else stack.pop())
    elif parts[0] == "size":
        result.append(len(stack))
    elif parts[0] == "empty":
        result.append(1 if not stack else 0)
    elif parts[0] == "top":
        result.append(-1 if not stack else stack[-1])

for output in result:
    print(output)