class TrieNode:
    """
    A node in the Trie structure.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Implementation of Trie (Prefix Tree) for efficient word storage and retrieval.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.

        Args:
        word (str): The word to insert.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Search for a word in the Trie.

        Args:
        word (str): The word to search.

        Returns:
        bool: True if the word is present, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if any word in the Trie starts with the given prefix.

        Args:
        prefix (str): The prefix to check.

        Returns:
        bool: True if any word starts with the prefix, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        """
        Delete a word from the Trie.

        Args:
        word (str): The word to delete.
        """
        def _delete(node, word, depth):
            if not node:
                return False

            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0  # Delete if leaf node

            char = word[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], word, depth + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0
            return False

        _delete(self.root, word, 0)
