def fibonacci(n):
    # 创建一个数组用于存储计算过的结果
    dp = [0] * (n+1)

    # 初始条件
    dp[0] = 0
    dp[1] = 1

    # 动态规划计算
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    # 返回结果
    return dp[n]

# 测试
n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
