class TrieNode:
    def __init__(self):
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        root = self.root
        for i in word:
            if not i in root.children:
                root.children[i] = TrieNode()
            root = root.children[i]
        
    def search(self, word: str) -> bool:
        m = len(word)
        stack = [(self.root, 0)]
        while stack:
            node, pos = stack.pop()
            if pos == m: return True
            if word[pos] == ".":
                for child in node.children:
                    stack.append((child, pos + 1))
            else:
                if word[pos] in node.children:
                    stack.append((node.children[word[pos]], pos + 1))
d = WordDictionary()
d.addWord("bad")
d.addWord("dad")
d.addWord("mad")
d.addWord("pad")

d.search(".ad")
d.search("b..")