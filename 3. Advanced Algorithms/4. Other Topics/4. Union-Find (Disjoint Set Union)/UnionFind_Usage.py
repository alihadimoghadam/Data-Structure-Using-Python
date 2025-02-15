from UnionFind_Algorithm import UnionFind

if __name__ == "__main__":
    # Initialize Union-Find for 10 elements
    uf = UnionFind(10)

    # Union operations
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(5, 6)

    # Check connectivity
    print("Example 1: Connectivity Tests")
    print(f"Are 1 and 3 connected? {uf.connected(1, 3)}")  # True
    print(f"Are 4 and 7 connected? {uf.connected(4, 7)}")  # True
    print(f"Are 1 and 4 connected? {uf.connected(1, 4)}")  # False

    # Additional Union
    uf.union(3, 4)
    print("\nExample 2: After Additional Union")
    print(f"Are 1 and 5 connected? {uf.connected(1, 5)}")  # True
