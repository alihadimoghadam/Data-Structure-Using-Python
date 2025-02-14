import heapq

class HuffmanNode:
    """
    Node class for the Huffman Tree.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    """
    Build a Huffman Tree using a Min-Heap (Priority Queue).

    Characteristics:
    - Time Complexity: O(n log n) (due to heap operations).
    - Space Complexity: O(n) (tree storage).

    Args:
    freq_dict (dict): A dictionary containing character frequencies.

    Returns:
    HuffmanNode: The root node of the Huffman Tree.
    """
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(node, prefix="", huffman_codes=None):
    """
    Generate Huffman Codes by traversing the Huffman Tree.

    Args:
    node (HuffmanNode): The root of the Huffman Tree.
    prefix (str): Current prefix of the Huffman code.
    huffman_codes (dict): Dictionary to store Huffman codes.

    Returns:
    dict: A dictionary of character-to-code mappings.
    """
    if huffman_codes is None:
        huffman_codes = {}

    if node is not None:
        if node.char is not None:
            huffman_codes[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", huffman_codes)
        generate_huffman_codes(node.right, prefix + "1", huffman_codes)

    return huffman_codes


def huffman_encoding(text):
    """
    Perform Huffman Encoding on the given text.

    Args:
    text (str): The input text to encode.

    Returns:
    tuple: (Encoded text, Huffman codes)
    """
    if not text:
        return "", {}

    # Step 1: Build frequency dictionary
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # Step 2: Build Huffman Tree
    huffman_tree_root = build_huffman_tree(freq_dict)

    # Step 3: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(huffman_tree_root)

    # Step 4: Encode text
    encoded_text = "".join(huffman_codes[char] for char in text)

    return encoded_text, huffman_codes
