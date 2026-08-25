def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def generate_fibonacci_sequence_memo(n):
    memo = {}
    return [fib_memo(i, memo) for i in range(n)]

# Execution
if __name__ == "__main__":
    n = int(input("Enter N: "))
    sequence = generate_fibonacci_sequence_memo(n)
    print(f"Fibonacci Sequence (first {n} numbers): {sequence}")
