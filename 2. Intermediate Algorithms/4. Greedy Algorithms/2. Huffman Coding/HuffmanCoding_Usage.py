from HuffmanCoding_Algorithm import huffman_encoding

if __name__ == "__main__":
    # Example 1: Encoding a simple string
    text1 = "hello huffman"
    encoded1, codes1 = huffman_encoding(text1)
    print("Example 1: Huffman Encoding")
    print(f"Original Text: {text1}")
    print(f"Encoded Text: {encoded1}")
    print(f"Huffman Codes: {codes1}")

    # Example 2: Encoding a different string
    text2 = "data compression"
    encoded2, codes2 = huffman_encoding(text2)
    print("\nExample 2: Huffman Encoding for another string")
    print(f"Original Text: {text2}")
    print(f"Encoded Text: {encoded2}")
    print(f"Huffman Codes: {codes2}")

    # Example 3: Encoding a string with repeated characters
    text3 = "aaaaaaabbbbcc"
    encoded3, codes3 = huffman_encoding(text3)
    print("\nExample 3: Encoding with highly repeated characters")
    print(f"Original Text: {text3}")
    print(f"Encoded Text: {encoded3}")
    print(f"Huffman Codes: {codes3}")
