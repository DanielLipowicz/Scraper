import json


class Publciation:
    def __init__(self, title=None, authors=[], year=None, key_words=[], bibliography=[]):

        self.title = title
        self.authors = authors
        self.year = year
        self.key_words = key_words
        self.bibliography = bibliography

    def print_publication(self, i):
        print('lp. ', i)
        print(self.title)
        print(self.authors)
        print(self.year)
        print(self.key_words)
        print(self.bibliography)

    def to_json(self):
        to_json = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
        return str(to_json)

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