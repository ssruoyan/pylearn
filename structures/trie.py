# 前缀树实现 https://zh.wikipedia.org/wiki/Trie
# 前缀树是一种特殊的数据结构。
# 键不是直接保存在节点中，而是由节点在树中的位置决定。一个节点的所有子孙都有相同的前缀。

class TrieNode:
    def __init__(self, ch):
        self.char = ch
        self.links = {}
        self.word_end = False
        self.count = 0

    def contains(self, ch):
        return self.links.get(ch) is not None

    def get(self, ch):
        return self.links.get(ch)

    def put(self, ch, node):
        self.links[ch] = node
        return self.get(ch)


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root
        for ch in word:
            if node.contains(ch):
                node.count = node.count + 1
                node = node.get(ch)
            else:
                node = node.put(ch, TrieNode(ch))
        node.word_end = True

    def searchPrefix(self, prefix):
        node = self.root
        for ch in prefix:
            if node.contains(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word):
        node = self.searchPrefix(word)

        if node is not None:
            return node.word_end
        return False

    def startsWith(self, prefix):
        node = self.searchPrefix(prefix)
        return node is not None

    def print(self):
        print(self.stringify(self.root))

    def stringify(self, node):
        dic = {}
        for ch in node.links:
            dic[ch] = {
                "char": node.char,
                "links": self.stringify(node.links.get(ch)),
                "count": node.count
            }
        return dic
