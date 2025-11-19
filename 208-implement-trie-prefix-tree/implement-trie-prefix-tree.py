class TrieNode:
    def __init__(self):
        # Each node stores children in a hash map { character: TrieNode }
        self.children = {}
        # Marks if a word ends at this node
        self.endOfWord = False


class Trie:
    def __init__(self):
        # Trie always starts with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Insert each character into the Trie one by one
        cur = self.root
        for c in word:
            # If the character is not present, create a new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node
            cur = cur.children[c]
        # After inserting all characters, mark the end of the word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Check if a full word exists in the Trie
        cur = self.root
        for c in word:
            # If any character is missing, the word doesn't exist
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # Word exists only if endOfWord flag is True at last char
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Check if a prefix exists in the Trie
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # If traversal succeeded, the prefix exists
        return True
