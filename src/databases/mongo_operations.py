from src.databases import mogodbConfig
from src.data_visualisation import pyplot_usage



def select_distinct_key_words(collection):
    list = []
    for i in collection.distinct("key_words"):
        list.append(i)
    return list
con = mogodbConfig.mongoConnection()
# keywords_base = select_distinct_key_words(con.collection)


def find_in_database_by_keyword(conn, keyword, to_find='_id'):
    result = []
    for i in conn.collection.find({"key_words": keyword}, {"key_words": 1, to_find:1}):
        result.append(i[to_find])
    return result


def get_all_keywords_related(conn, keyword):
    related_keywords = []
    for i in conn.collection.find({'key_words:': keyword},{"key_words":1, "_id":0}):
        for j in i:
            print(j['key_words'])
            related_keywords.append(j)
    return related_keywords


def get_publications_with_keyword(conn, keyword):
    publication_id_table = find_in_database_by_keyword(conn, keyword, '_id')
    keywords_table = find_in_database_by_keyword(conn, keyword, "key_words")
    result = list(set(keywords_table))
    result.sort()
    print('get_publications_with_keyword result: ',result )
    return result


def get_connected_publication(conn, connectet_with_keyword):
    result = find_in_database_by_keyword(conn, connectet_with_keyword, "_id")
    return result


def get_density_of_keywords(keywords):
    density_list = {}
    for keyword in keywords:
        density_list[keyword] =density_list.get(keyword, 0) + 1
    order_density = []
    print('a',density_list)
    #  print(density)
    # for i in sorted(list.keys()):
    #     x = density[i]
    #     order_density.append([x, i])

    return sorted(density_list)


keywords = ["Big Data", "Hurtownie danych", "Analiza ekonometryczna",
            "Ekonometria"]
keywords_data = []
for i in range(3):
    print(keywords[i])
    data = get_publications_with_keyword(con, keywords[i])
    print('data ', data)
    density_of_keyword = get_density_of_keywords(data)
    keywords_with_density_bigger_than_one = []
    for element in density_of_keyword:
        print('el', element)
        # if element[1] >= 2:
        #     keywords_with_density_bigger_than_one.append(element)
    print('dentisity ', density_of_keyword)
    print('dentisity >2 ',keywords_with_density_bigger_than_one)
    keywords_data.append(density_of_keyword)



#word = get_connected_keywords(con, "Data Mining")


# print(word)
