class Publciation:
    def __init__(self):

        self.title = None
        self.authors = []
        self.year = None
        self.key_words = []
        self.bibliography = []


    def __repr__(self):

        print(self.title)
        print(self.authors)
        print(self.year)
        print(self.key_words)
        print(self.bibliography)
