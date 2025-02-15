from KosarajuSCC_Algorithm import KosarajuSCC

if __name__ == "__main__":
    # Example 1: Graph with SCCs
    graph1 = KosarajuSCC(5)
    graph1.add_edge(1, 0)
    graph1.add_edge(0, 2)
    graph1.add_edge(2, 1)
    graph1.add_edge(0, 3)
    graph1.add_edge(3, 4)

    print("Example 1: SCCs in Graph")
    print(f"Strongly Connected Components: {graph1.find_sccs()}")

    # Example 2: Another Graph with SCCs
    graph2 = KosarajuSCC(7)
    graph2.add_edge(0, 1)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 0)
    graph2.add_edge(1, 3)
    graph2.add_edge(3, 4)
    graph2.add_edge(4, 5)
    graph2.add_edge(5, 3)
    graph2.add_edge(5, 6)

    print("\nExample 2: Another SCC Detection")
    print(f"Strongly Connected Components: {graph2.find_sccs()}")
