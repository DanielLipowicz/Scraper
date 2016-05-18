from src.databases import mogodbConfig


def select_distinct_key_words(collection):
    list = []
    for i in collection.distinct("key_words"):
        list.append(i)
        print(i)
    return list

con = mogodbConfig.mongoConnection()
# keywords_base = select_distinct_key_words(con.collection)


def find_key_word_in_database(conn, keyword, select):
    result = []
    for i in conn.collection.find({"key_words": keyword}, {"key_words": 1}):
        for j in i[select]:
            result.append(j)
    return result


def get_connected_keywords(conn, keyword):
    keywords_table = find_key_word_in_database(conn, keyword, "key_words")
    result = list(set(keywords_table))
    result.sort()
    density = {}
    for item in keywords_table:
        density[item] = density.get(item, 0) + 1

    order_density=[]
    for i in sorted(density.keys()):
        order_density.append([density[i], i])
       # print(i, (density[i]))
    print(order_density[:])
    return result


def get_connected_publication(conn, connectet_with_keyword):
    result = find_key_word_in_database(conn, connectet_with_keyword, "_id")
    return result

# for i in con.collection.find({"key_words": "Ekonometria"}, {"key_words": 1, "objectID": 1}):
#     print(i)

keywords = ["Big Data", "Hurtownie danych", "Analiza ekonometryczna",
            "Ekonometria"]
for i in range(3):
    print(keywords[i])
    print(get_connected_keywords(con, keywords[i]))
#word = get_connected_keywords(con, "Data Mining")


# print(word)
