def fib_tabulation(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp

# Execution
if __name__ == "__main__":
    n = int(input("Enter N: "))
    sequence = fib_tabulation(n)
    print(f"Fibonacci Sequence (first {n} numbers): {sequence}")
