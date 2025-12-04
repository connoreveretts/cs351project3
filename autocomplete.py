from trie import Trie
from typing import List
import os

class AutocompleteSystem:    
    def __init__(self):
        self.trie = Trie()
        self.load_default_words()
    
    # Terms
    def load_default_words(self):
        words = [
            # Programming languages
            "python", "java", "javascript", "typescript", "rust",
            "cpp", "csharp", "ruby", "swift",
            # Data structures
            "array", "list", "tree", "graph", "stack", "queue",
            "heap", "trie", "hashtable", "linkedlist",
            # Algorithms
            "sort", "search", "binary", "quicksort", "mergesort",
            "algorithm", "recursion", "iteration", "dynamic",
            # Cs terms
            "function", "variable", "class", "object", "method",
            "interface", "abstrat", "inheritance", "polymorphism",
            "encapsulation", "debugging", "testing", "compilation",
            # Web terms
            "html", "css", "database", "server", "client",
            "api", "backend", "frontend", "framework", "library"
        ]
        
        for word in words:
            self.trie.insert(word)
    
    # Add words function
    def add_word(self, word: str) -> None:
        self.trie.insert(word)
    
    # Get suggestions function
    def get_suggestions(self, prefix: str, max_suggestions: int = 10) -> List[str]:
        suggestions = self.trie.get_words_with_prefix(prefix)
        return suggestions[:max_suggestions]
    
    # Remove word function
    def remove_word(self, word: str) -> bool:
        return self.trie.delete(word)
    
    # Check word existence function
    def word_exists(self, word: str) -> bool:
        return self.trie.search(word)
    
    # Display stats function
    def display_stats(self) -> None:
        print(f"\n--- Autocomplete System Statistics ---")
        print(f"Total words in dictionary: {self.trie.size()}")
        print(f"--------------------------------------\n")


# Demo function
def run_demo():
    system = AutocompleteSystem()
    print("=" * 50)
    print("   Autocomplete System Demo (Trie-based)")
    print("=" * 50)
    print("\nCommands:")
    print("  - Type a prefix to see suggestions")
    print("  - 'add <word>' to add a new word")
    print("  - 'remove <word>' to remove a word")
    print("  - 'check <word>' to check if word exists")
    print("  - 'stats' to see statistics")
    print("  - 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("\n> ").strip()
        
        if not user_input:
            continue
        if user_input.lower() == 'quit':
            print("Bye")
            break
        if user_input.lower() == 'stats':
            system.display_stats()
            continue
        if user_input.lower().startswith('add '):
            word = user_input[4:].strip()
            if word:
                system.add_word(word)
                print(f"Added '{word}' to dictionary")
            continue
        if user_input.lower().startswith('remove '):
            word = user_input[7:].strip()
            if word:
                if system.remove_word(word):
                    print(f"Removed '{word}' from dictionary")
                else:
                    print(f"Word '{word}' not found")
            continue
        if user_input.lower().startswith('check '):
            word = user_input[6:].strip()
            if word:
                if system.word_exists(word):
                    print(f"'{word}' exists in dictionary")
                else:
                    print(f"'{word}' not found in dictionary")
            continue
        suggestions = system.get_suggestions(user_input)
        if suggestions:
            print(f"\nSuggestions for '{user_input}':")
            for i, word in enumerate(suggestions, 1):
                print(f"  {i}. {word}")
        else:
            print(f"No suggestions found for '{user_input}'")

if __name__ == "__main__":
    run_demo()
