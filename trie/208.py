class Node:
    def __init__(self) -> None:
        self.children = {}
        self.terminal = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.terminal = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("adventure")
obj.insert("advent")
obj.insert("banana")
obj.insert("ban")

print(obj.search("adventure"), True)
print(obj.search("advent"), True)
print(obj.search("adv"), False)
print(obj.search("adventurer"), False)
print(obj.startsWith("ba"), True)
print(obj.startsWith("banana"), True)
print(obj.startsWith("ban"), True)
