class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        word = []
        path = path + "/"  # so we dont have to handle the last word separately outside of the loop

        for i, c in enumerate(path):
            if c == "/":
                if not word:
                    continue
                if path[i - 1] != "/":  # word finished
                    word = ''.join(word)
                    if word == ".." and stack:
                        stack.pop()
                    elif word != "." and word != "..":
                        stack.append(word)
                    word = []
            else:
                word.append(c)

        return "/" + '/'.join(stack)
