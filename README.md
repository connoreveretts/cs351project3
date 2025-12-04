# Autocomplete System using Trie

## Project Description

I chose to implement the Trie (Prefix Tree)

This give a autocomplete system for computer science and programming related terms. You can type a prefix and get back suggestions for matching words.

There is a couple of uses for who would use this, and mainly if it was implemented in software. For example you could use this in vscode in a markdown file while typing or if it was any text writing software.

I did this project by myself.

## Installation & Setup

You just need Python 3.7 or higher and no libraries are needed.

If you are viewing the read me you have the two files trie.py and autocomplete.py which if they are in the same directory as they are you should be able to just run the autocomplete file and start typing.

If you type py for example you will get the following:

  ```
  > py
  Suggestions for 'py':
    1. python
    2. polymorphism
  ```

You can add a word using the following:

- **Add word**: `add <word>`
  ```
  > add pytorch
  Added 'pytorch' to dictionary
  ```

You can remove a word using the following:

- **Remove word**: `remove <word>`
  ```
  > remove pytorch
  Removed 'pytorch' from dictionary
  ```

You can check a word using the following:

- **Check word**: `check <word>`
  ```
  > check python
  'python' exists in dictionary
  ```

Lastley you can do a total count:
- **Statistics**: `stats`
  ```
  > stats
  --- Autocomplete System Statistics ---
  Total words in dictionary: 45
  --------------------------------------
  ```

### Example

```
> alg
Suggestions for 'alg':
  1. algorithm

> add algorithm
Added 'algorithm' to dictionary

> stats
Total words in dictionary: 46

```

## Tree Implementation 

A trie is a tree where each one of the nodes represents a character and words are foremd by the following the paths from the root to nodes that are marked as end of word. This allows the prefixed based autofilling.

Each path from root a to a marked node represents a word, children are stored ina dictrionaty mapping characters to nodes, and sharped prefixed use the same path to help save space.


### Time/Space Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| insert | O(m) | O(m) worst case |
| search | O(m) | O(1) |
| starts_with | O(m) | O(1) |
| get_words_with_prefix | O(p + n*k) | O(n*k) |
| delete | O(m) | O(1) |
| size | O(1) | O(1) |

Where:
- m = length of word
- p = length of prefix
- n = number of matching words
- k = average length of matching words

### Implementation Choices


1. **Dictionary for children**: Using Python dictionaries provides O(1) character lookup
2. **Case-insensitive**: All words stored in lowercase for consistent matching
3. **Word counter**: Maintains count for O(1) size queries
4. **Recursive deletion**: Cleans up unused nodes to save memory

## Updates

The initial interface included only basic operations, like insert, search, starts with, and get words with prefix

I added a couple of additions like delete, size, and case insensitive. This way I can make it more interactive and dynamic.

### Lessons Learned

Building the application revealed that a tree interface needs to evolve based on real use cases. The initial design focused on core tree operations, but the application needed additional utility methods for a complete user experience.

## Challenges & Solutions

Some of the challenges and solutions I faced through out this were marking nodes as non endof word leaves unused nodes in the tree, to fixed this I added recursive deletion that removes nodes with no children and arent end of words. Another issue I faces was capitaliaztion like python or Python and this was a straight forward fix of normalizing all inputs to lowercase. Lastly was some prefixed could match hundreds of words so I added a max suggestions incase I had a lot more words.

## Why Trie Over Simple List?

I think Trie over a simple list is a obvoius answer but for the O(p) to find all words with prefix vs O(n*m) scanning a list, as well as for memory efficiecys ut shares prefixes stored once. This can be scaled forever without any decrading to performance and lastly words automally stored by prefix helps with effiecney in organization.

A example of this in a list it must scan all 45 words to find py, but trie just follows the 2 characters from root.

## Future Enhancements

To improve I think we could track the word usage to show most common suggestions first, and maybe suggest words even with typos.
