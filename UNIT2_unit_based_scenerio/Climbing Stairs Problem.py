def climb_stairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

# Execution
if __name__ == "__main__":
    stairs = int(input("Enter number of stairs: "))
    ways = climb_stairs(stairs)
    print(f"Distinct ways to climb {stairs} stairs: {ways}")
