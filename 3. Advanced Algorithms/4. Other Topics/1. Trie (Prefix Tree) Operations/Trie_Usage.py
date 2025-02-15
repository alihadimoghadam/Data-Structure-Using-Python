from Trie_Algorithm import Trie

if __name__ == "__main__":
    # Initialize Trie
    trie = Trie()
    
    # Insert words
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    trie.insert("band")
    trie.insert("bat")
    trie.insert("cat")

    # Search for words
    print("Search 'apple':", trie.search("apple"))  # True
    print("Search 'app':", trie.search("app"))      # True
    print("Search 'bat':", trie.search("bat"))      # True
    print("Search 'can':", trie.search("can"))      # False

    # Check prefixes
    print("Starts with 'ba':", trie.starts_with("ba"))  # True
    print("Starts with 'ca':", trie.starts_with("ca"))  # True
    print("Starts with 'cap':", trie.starts_with("cap"))  # False

    # Delete a word
    trie.delete("bat")
    print("Search 'bat' after deletion:", trie.search("bat"))  # False
