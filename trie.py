import queue

# Implement Trie for Aho-Corasick String Matching Algorithm
START_CHAR = 'a'
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.eos = False
        self.children = [None]*27  # No of alphabets


class Trie:
    def __init__(self):
        self.root = TrieNode("0")

    def insert(self, word):
        curr = self.root
        for i in word:
            if curr.children[ord(i)-ord(START_CHAR)] == None:
                curr.children[ord(i)-ord(START_CHAR)] = TrieNode(i)
            curr = curr.children[ord(i)-ord(START_CHAR)]
        curr.eos = True

    def search(self, word):
        curr = self.root
        for i in word:
            if curr.children[ord(i)-ord(START_CHAR)] == None:
                return False
            else:
                curr = curr.children[ord(i) - ord(START_CHAR)]
        return curr.eos

    def print_trie(self):
        '''
        Prints trie in BFS
        :return: nothing, just prints the trie
        '''
        level_wise_elements = []
        queue_for_bfs = queue.Queue()
        queue_for_bfs.put([self.root, 0]) # Node and its level
        level_wise_elements.append([])
        while (not queue_for_bfs.empty()):
            next_node = queue_for_bfs.get()
            level_wise_elements[next_node[1]].append(next_node[0].val)
            if len(level_wise_elements) <= next_node[1]+1:
                level_wise_elements.append([])
            for i,child in enumerate(next_node[0].children):
                if child != None:
                    queue_for_bfs.put([next_node[0].children[i], next_node[1]+1])

        print(level_wise_elements)




my_trie = Trie()
my_trie.insert("he")
my_trie.insert("she")
my_trie.insert("here")
my_trie.insert("hello")
print(my_trie.search("h"), my_trie.search("he"))

my_trie.print_trie()





