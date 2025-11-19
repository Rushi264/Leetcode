class TrieNode:
    def __init__(self):
        # Each node stores its children and whether a word ends here
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        # Root of the Trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Insert a word into the Trie
        cur = self.root
        for c in word:
            # Create child node if it doesn't exist
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # Mark end of this word
        cur.word = True

    def search(self, word: str) -> bool:
        # DFS allows us to explore wildcard '.' characters
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                # If we hit a '.', try all possible children
                if c == ".":
                    for child in cur.children.values():
                        # If any branch returns True, the word matches
                        if dfs(i + 1, child):
                            return True
                    return False

                # Normal character: must exist in the Trie
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            # If we finish processing all characters, return True only if
            # this node marks the end of a valid inserted word
            return cur.word

        # Start DFS from the root node
        return dfs(0, self.root)
