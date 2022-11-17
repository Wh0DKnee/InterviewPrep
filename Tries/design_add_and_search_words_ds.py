class Node:

    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index >= len(word):
                return node.isWord
            if word[index] == ".":
                for c in node.children:
                    if dfs(node.children[c], index + 1):
                        return True
                return False
            elif word[index] not in node.children:
                return False
            else:
                return dfs(node.children[word[index]], index + 1)

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)