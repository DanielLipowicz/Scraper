class Publciation:
    def __init__(self):

        self.title = None
        self.authors = []
        self.year = None
        self.key_words = []
        self.bibliography = []

    def print_publication(self, i):
        print('lp. ', i)
        print(self.title)
        print(self.authors)
        print(self.year)
        print(self.key_words)
        print(self.bibliography)

    def return_list(self):
        to_return = []
        to_return.append(self.title)
        for each in self.authors:
            to_return.append(each)
        to_return.append(self.year)
        for each in self.key_words:
            to_return.append(each)
        for each in self.bibliography:
            to_return.append(each)
        return to_return