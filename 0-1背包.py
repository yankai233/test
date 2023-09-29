# M, n = 6, 3
# p = [0, 5, 4, 3]
# w = [0, 3, 3, 2]
p, w = [], []
# 用户输入
M, n = (int(i) for i in input().split())
i = n
while i > 0:
    s = input().split()
    if len(s) == 0:
        continue
    p.append(int(s[0]))
    w.append(int(s[1]))
    i -= 1
# dp[i][j]:物品为1~i,容量为j的背包能装的最大物品数
dp = [[0] * (M + 1) for i in range(n + 1)]
X = [0] * n
for i in range(1, n + 1):   # 遍历物品
    for j in range(1, M + 1):   # 遍历背包
        if j - w[i - 1] < 0:    # 装不下
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + p[i - 1])

# 解向量
j = M
for i in range(n, 0, -1):
    if dp[i][j] != dp[i - 1][j]:
        X[i - 1] = 1
        j = j - w[i - 1]
    else:
        X[i - 1] = 0
print(dp[-1][-1])
for i in range(len(X)):
    print(X[i], end=' ')
