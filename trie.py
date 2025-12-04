from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children = {}  # Map from character to TrieNode
        self.is_end_of_word = False  # True if node represents end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0
    
    # Insert word function
    def insert(self, word: str) -> None:
        # Insert word into trie
        if not word:
            return
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.word_count += 1
    
    # Search word function
    def search(self, word: str) -> bool:       
        if not word:
            return False
        node = self._find_node(word.lower())
        return node is not None and node.is_end_of_word
    
    # Starts with prefix function
    def starts_with(self, prefix: str) -> bool:
        if not prefix:
            return True
        return self._find_node(prefix.lower()) is not None
    
    # Get words with prefix function
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        results = []
        prefix_lower = prefix.lower()
        node = self._find_node(prefix_lower)
        if node is None:
            return results
        self._collect_words(node, prefix_lower, results)
        return results
    
    # Delete word function
    def delete(self, word: str) -> bool:
        if not word:
            return False
        word_lower = word.lower()
        return self._delete_helper(self.root, word_lower, 0)
    
    # Size function
    def size(self) -> int:
        return self.word_count
    
    # Find node helper function
    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    # Collect words helper function
    def _collect_words(self, node: TrieNode, current_word: str, results: List[str]) -> None:
        if node.is_end_of_word:
            results.append(current_word)
        for char, child_node in sorted(node.children.items()):
            self._collect_words(child_node, current_word + char, results)
    
    # Delete helper function
    def _delete_helper(self, node: TrieNode, word: str, depth: int) -> bool:
        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            self.word_count -= 1
            return len(node.children) == 0
        char = word[depth]
        if char not in node.children:
            return False
        child = node.children[char]
        should_delete_child = self._delete_helper(child, word, depth + 1)
        if should_delete_child:
            del node.children[char]
            return not node.is_end_of_word and len(node.children) == 0
        return False
