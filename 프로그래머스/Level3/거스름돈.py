def solution(n, money):
    money.sort()
    dp = [0] * 100001
    dp[0] = 1

    for i in money:
        for j in range(1, n + 1):
            if j >= i:
                dp[j] += dp[j - i]

    return dp[n] % 1000000007