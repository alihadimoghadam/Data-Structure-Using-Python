from EdmondsKarp_Algorithm import EdmondsKarp

if __name__ == "__main__":
    # Example 1: Simple Flow Network
    ek1 = EdmondsKarp(6)
    ek1.add_edge(0, 1, 16)
    ek1.add_edge(0, 2, 13)
    ek1.add_edge(1, 2, 10)
    ek1.add_edge(1, 3, 12)
    ek1.add_edge(2, 1, 4)
    ek1.add_edge(2, 4, 14)
    ek1.add_edge(3, 2, 9)
    ek1.add_edge(3, 5, 20)
    ek1.add_edge(4, 3, 7)
    ek1.add_edge(4, 5, 4)

    print("Example 1: Maximum Flow in Graph")
    print(f"Max Flow: {ek1.max_flow(0, 5)}")  # Expected Output: 23

    # Example 2: Another Flow Network
    ek2 = EdmondsKarp(4)
    ek2.add_edge(0, 1, 10)
    ek2.add_edge(0, 2, 5)
    ek2.add_edge(1, 2, 15)
    ek2.add_edge(1, 3, 10)
    ek2.add_edge(2, 3, 10)

    print("\nExample 2: Another Maximum Flow Calculation")
    print(f"Max Flow: {ek2.max_flow(0, 3)}")  # Expected Output: 15
