class key_word:
    def __init__(self, keyword):
        self.keyword = keyword
        #  dictionary:
        #  {keyword: quantity_of_related_keywords}
        self.related_keywords = {}
        print('Created object: ', self.keyword)


def merge_two_related_keyword_dictionary(dictionary1, dictionary2):
    dictionary1_keys = dictionary1.related_keywords
    dictionary2_keys = dictionary2.related_keywords
    keywords_to_search = []

    for keyword in dictionary1_keys:
        if keyword not in keywords_to_search:
            keywords_to_search.append(keyword)
    for keyword in dictionary2_keys:
        if keyword not in keywords_to_search:
            keywords_to_search.append(keyword)
    merged_list = []
    merged_list.append(['no', 'dictionary1', 'dictionary2', 'keyword'])
    i = 1
    for each in keywords_to_search:
        merged_list.append([i, dictionary1_keys.get(each), dictionary2_keys.get(each), each])
        # print([i], [dictionary1_keys.get(each)], [dictionary2_keys.get(each)], [each])
        i += 1
    print(merged_list)
    return merged_list


def filter_data_list_by_density(data_list, density):
    filtered_list = []
    for each in data_list[1:]:
        if each[1] is None:
            each[1] = 0
        if each[2] is None:
            each[2] = 0
        if each[1] >= density or each[2] >= density:
            filtered_list.append(each)
    i = 1
    for each in filtered_list:
        each[0] = i
        i += 1
    return filtered_list



















