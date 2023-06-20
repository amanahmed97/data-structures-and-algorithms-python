"""
https://leetcode.com/problems/implement-trie-prefix-tree/

"""
class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False


class Trie:

    def __init__(self):
        self.root = self.getTrieNode()

    def getTrieNode(self):
        return TrieNode()

    def getIndex(self, c):
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        pCrawl = self.root

        for level in range(len(word)):
            index = self.getIndex(word[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()

            pCrawl = pCrawl.children[index]

        pCrawl.isEndofWord = True

    def search(self, word: str) -> bool:
        pCrawl = self.root

        for level in range(len(word)):
            index = self.getIndex(word[level])
            if not pCrawl.children[self.getIndex(word[level])]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndofWord

    def startsWith(self, prefix: str) -> bool:
        pCrawl = self.root

        level = 0
        while level < len(prefix):
            index = self.getIndex(prefix[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
            level += 1

        return level == len(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)