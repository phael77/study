class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word
    
    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
    

trie = Trie()

trie.insert("apple")
trie.insert("pen")
trie.insert("pineapple")
trie.insert("pera")

print(trie.search("apple"))       # True
print(trie.search("pen"))         # True
print(trie.search("pine"))        # False
print(trie.starts_with("pin"))    # True
print(trie.starts_with("pe"))     # True
print(trie.starts_with("banana")) # False