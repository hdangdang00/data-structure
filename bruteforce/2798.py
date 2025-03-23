# 2798. 블랙잭 https://www.acmicpc.net/problem/2798
# 시간 복잡도: O(n^3), 공간 복잡도: O(n)

n, m =  map(int, input().split())
num_list = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total = num_list[i] + num_list[j] + num_list[k]
            if total <= m and total > result:
                result = total

print(result)