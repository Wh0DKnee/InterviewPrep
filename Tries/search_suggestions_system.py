from typing import List


class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root

        for c in word:
            index = ord(c) - 97
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.isWord = True

    def get_suggestions(self, prefix):
        start = self.root

        for c in prefix:
            index = ord(c) - 97
            start = start.children[index]
            if start is None:
                return []

        res = []

        def dfs(node, cur_str):
            if len(res) == 3:
                return
            if node.isWord:
                res.append(cur_str)

            for idx, child in enumerate(node.children):
                if child is not None:
                    dfs(child, cur_str + chr(idx + 97))

        dfs(start, prefix)
        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.add(p)

        res = []
        for i in range(1, len(searchWord) + 1):
            suggestions = trie.get_suggestions(searchWord[0:i])
            res.append(suggestions)

        return res







