from random_word import RandomWords
r = RandomWords()


class TestNode:
    def __init__(self):
        self.child = {}
        self.isWord = False

class Test:
    def __init__(self):
        self.root = TestNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.child.keys():
                node.child[char] = TestNode()
            node = node.child[char]
        node.isWord = True
        print(f"inserted: {word}")

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.child.keys():
                print("not found")
                return
            node = node.child[char]
        if node.isWord:
            print("found")
        else:
            print("not found")

    def starts_with(self, char, node, word=""):
        word = word + char
        if node.isWord:
            print(word)
            return word
        else:
            for char in node.child.keys():
                self.starts_with(char, node.child[char], word)

    def find_all(self):
        node = self.root
        for i in node.child.keys():
            self.starts_with(i, test.root.child[i])

    def suggest(self, word):
        node = self.root
        for i in word:
            node = node.child[i]

        for i in node.child.keys():
            self.starts_with(i, node.child[i], "")
            

test = Test()
##a = ["help", "hello", "halo", "abc", "acd", "abd"]

##for i in a:
##    test.insert(i)
##    test.search(i)

for i in range(100):
    temp = r.get_random_word()
    test.insert(temp)
    print("-"*20)

test.find_all()
print("-"*100)
test.suggest("a")
print("-"*100)
test.suggest("b")
print("-"*100)
test.suggest("c")

