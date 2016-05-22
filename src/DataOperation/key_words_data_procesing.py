class key_word:
    def __init__(self, keyword):
        self.keyword = keyword
        #  dictionary:
        #  {keyword: quantity_of_related_keywords}
        self.related_keywords = {}
        print('Created object: ', self.keyword)


def merge_two_related_keyword_dictionary(dictionary1, dictionary2):
    print(dictionary1.related_keywords)
    print(dictionary2.related_keywords)
    # merged_list = []
    merged_list = [['no'], ['dictionary1'], ['dictionary2'], ['keyword']]
    if len(dictionary1.related_keywords) >= len(dictionary2.related_keywords):
        longer_dictionary = dictionary1.related_keywords
        shorter_dictionary = dictionary2.related_keywords
    else:
        longer_dictionary = dictionary2.related_keywords
        shorter_dictionary = dictionary1.related_keywords
    i = 1
    for each in longer_dictionary:
        merged_list.append([i], [longer_dictionary[each]], [shorter_dictionary[each]], [each])
        print([i], [longer_dictionary[each]], [shorter_dictionary[each]], [each])
        i += 1






















