#  Design Document

## Tree Selection

Why I choose this tree? It seemed to be the most straight forward and useful according to the internet. Its ideal for string based operations like autocomplete which is also why I did autocomplete. 

## Use Cases

Some of the following things are what the trie tree is good at, autcomplete sustem, spell checkings, IP routing, dictionary implementations, and word games. All due to its fast prefix validation and queries.

## Properties

The things that make this unqiue is that all words sharing the same prefix share the same path, so each node represents one character. For the time complexity insert, search, and delete are all O(m) where m is the word length, only is prefix search O(p+n*k) as p is the prefix length, n is the results, and k is the average word length. Space complexity could be relevant here and the total for worst case is O(alphabet size * n * n), where n is number of words. The best case is just O(total charaacters in all unique prefixes). But the key property is time complexiry indepdent of total number of words and only is dependdent on word and prefix length.


## Interface Design

This is the data strucutre

```python
class TrieNode:
    """Node in the Trie structure"""
    def __init__(self):
        self.children: Dict[str, TrieNode]  
        self.is_end_of_word: bool           
```

### Method Signatures

#### 1. insert(word: str) -> None

Description: Insert a word into the trie

Parameters: `word`: String to insert (case-insensitive)

Returns: None

Time Complexity: O(m) where m is length of word

Space Complexity: O(m) in worst case

---

#### 2. search(word: str) -> bool
Description: Check if exact word exists in trie

Parameters: `word`: String to search for (case-insensitive)

Returns: Boolean indicating if word exists

Time Complexity: O(m) where m is length of word

Space Complexity: O(1)

---

#### 3. starts_with(prefix: str) -> bool
Description: Check if any word has this prefix

Parameters: `prefix`: String prefix to check (case-insensitive)

Returns: Boolean indicating if prefix exists

Time Complexity: O(p) where p is prefix length

Space Complexity: O(1) 

---

#### 4. get_words_with_prefix(prefix: str) -> List[str]
Description: Return all words starting with given prefix

Parameters: `prefix`: String prefix to match (case-insensitive)

Returns: List of all matching words (sorted alphabetically)

Time Complexity: O(p + n*k)

Space Complexity: O(n*k)

---

#### 5. delete(word: str) -> bool
Description: Remove word from trie

Parameters: `word`: String to delete (case-insensitive)

Returns: Boolean indicating if word was found and deleted

Time Complexity: O(m) where m is word length

Space Complexity: O(1)

---

#### 6. size() -> int
Description: Return count of words in trie

Parameters: None

Returns: Integer count of total words

Time Complexity: O(1)

Space Complexity: O(1)


---

## Complexity Analysis Summary

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| insert | O(m) | O(m) | m = word length |
| search | O(m) | O(1) | m = word length |
| starts_with | O(p) | O(1) | p = prefix length |
| get_words_with_prefix | O(p + n*k) | O(n*k) | n = results, k = avg word length |
| delete | O(m) | O(1) | m = word length |
| size | O(1) | O(1) | Constant time counter |

