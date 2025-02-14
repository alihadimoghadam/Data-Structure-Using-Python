from Fibonacci_Algorithm import fibonacci_memo, fibonacci_tab

if __name__ == "__main__":
    # Example 1: Compute Fibonacci using Memoization
    n1 = 10
    print("Example 1: Fibonacci using Memoization (Top-Down)")
    print(f"Fibonacci({n1}) = {fibonacci_memo(n1)}")

    # Example 2: Compute Fibonacci using Tabulation
    n2 = 10
    print("\nExample 2: Fibonacci using Tabulation (Bottom-Up)")
    print(f"Fibonacci({n2}) = {fibonacci_tab(n2)}")

    # Example 3: Compute large Fibonacci numbers efficiently
    n3 = 50
    print("\nExample 3: Large Fibonacci Computation")
    print(f"Fibonacci({n3}) using Memoization = {fibonacci_memo(n3)}")
    print(f"Fibonacci({n3}) using Tabulation = {fibonacci_tab(n3)}")
