from typing import List


class Node:

    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0


class Trie:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        cur.refs += 1

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            cur.refs += 1

        cur.isWord = True

    def removeWord(self, word: str) -> bool:
        cur = self.root
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(i, j, node, word):
            c = board[i][j]
            if c not in node.children or node.children[c].refs < 1:
                return
            node = node.children[c]
            word += c
            if node.isWord:
                res.add(word)
                trie.removeWord(word)
                node.isWord = False     # needed to prevent removing the same word twice, which ruins longer words
                                        # starting with this word as a prefix.
            visited.add((i, j))
            valid_neighbors = self.getValidNeighbors(board, i, j)
            for ni, nj in valid_neighbors:
                if (ni, nj) not in visited:
                    dfs(ni, nj, node, word)
            visited.remove((i, j))

        for r in range(ROWS):
            for c in range(COLS):
                visited.clear()
                dfs(r, c, trie.root, "")

        return list(res)

    def getValidNeighbors(self, board, i, j):
        neighbors = []
        if i >= 1:
            neighbors.append((i - 1, j))
        if i < len(board) - 1:
            neighbors.append((i + 1, j))
        if j >= 1:
            neighbors.append((i, j - 1))
        if j < len(board[0]) - 1:
            neighbors.append((i, j + 1))
        return neighbors
