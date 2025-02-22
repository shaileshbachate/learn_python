class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def print_trie(self):
        curr = self.root
        self.print_trie_helper(curr, "")
    
    def print_trie_helper(self, node, prefix):
        if node.is_end:
            print(prefix + node.char)

        for child in node.children:
            self.print_trie_helper(child, prefix + node.char)

    # This function was generated with the help of AI # may or may not be correct
    def insert(self, word):
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.is_end = True
    
    # This function was generated with the help of AI # may or may not be correct
    def search(self, word):
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                return False
        return node.is_end


t = Trie()
t.insert("apple")
t.insert("app")
t.insert("apples")
t.insert("applet")
t.insert("appletree")
t.insert("mango")
t.insert("mangoes")

t.insert("orange")

t.insert("banana")
t.insert("ban")
t.insert("bananas")

t.print_trie()

print(t.search("appletree"))
print(t.search("app"))
print(t.search("apple2"))