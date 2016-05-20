from src.databases import mogodbConfig
import numpy as pn
import matplotlib.pyplot as plt


def select_distinct_key_words(collection):
    list = []
    for i in collection.distinct("key_words"):
        list.append(i)

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

    # plt.plot(order_density[:])
    return result


def get_connected_publication(conn, connectet_with_keyword):
    result = find_key_word_in_database(conn, connectet_with_keyword, "_id")
    return result

def get_dentisy_of_keyword(list):
    density = {}
    for item in list:
        print(item)
        density[item] = density.get(item, 0) + 1
    order_density = []

    print(density)

    for i in sorted(density.keys()):
        x = density[i]
        order_density.append([x, i])
    return order_density

# for i in con.collection.find({"key_words": "Ekonometria"}, {"key_words": 1, "objectID": 1}):
#     print(i)

keywords = ["Big Data", "Hurtownie danych", "Analiza ekonometryczna",
            "Ekonometria"]
keywords_data = []
for i in range(3):
    data = get_connected_keywords(con, keywords[i])
    density_of_keyword = get_dentisy_of_keyword(data)
    print(density_of_keyword)
    keywords_data.append(density_of_keyword)



#word = get_connected_keywords(con, "Data Mining")


# print(word)
