from CoinChange_Algorithm import coin_change_memo, coin_change_tab

if __name__ == "__main__":
    # Example 1: Standard case
    coins1 = [1, 2, 5]
    amount1 = 11
    print("Example 1: Coin Change using Memoization")
    print(f"Minimum coins needed: {coin_change_memo(coins1, amount1)}")

    print("\nExample 1: Coin Change using Tabulation")
    print(f"Minimum coins needed: {coin_change_tab(coins1, amount1)}")

    # Example 2: Exact match with one coin
    coins2 = [2, 3, 7]
    amount2 = 7
    print("\nExample 2: Exact Coin Match")
    print(f"Minimum coins needed: {coin_change_tab(coins2, amount2)}")

    # Example 3: Impossible case
    coins3 = [2, 4]
    amount3 = 3
    print("\nExample 3: No Possible Combination")
    print(f"Minimum coins needed: {coin_change_tab(coins3, amount3)}")
