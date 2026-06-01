class Node:
    def __init__(self) -> None:
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
            node.words.append(word)

    def search(self, word: str) -> list[str]:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return []
            node = node.children[ch]

        return node.words


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        root = Trie()

        for word in products:
            root.insert(word)

        result = []

        for i in range(len(searchWord)):
            found = root.search(searchWord[: i + 1])
            if found:
                result.append(sorted(found)[:3])
            else:
                result.append([])

        return result
