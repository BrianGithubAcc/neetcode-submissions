class TreeNode:

    def __init__(self):
        self.children={}
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root=TreeNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.children:
                curr.children[i]=TreeNode()
            curr=curr.children[i]
        curr.end=True

    def search(self, word: str) -> bool:
        curr=self.root
        for j in word:
            if j in curr.children:
                curr=curr.children[j] 
            else:
                return False
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for i in prefix:
            if i in curr.children:
                curr=curr.children[i]
            else:
                return False
        return True
        