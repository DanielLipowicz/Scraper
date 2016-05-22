from src import Browser

from src.DataOperation import scraping_data_operations
from src.DataOperation import json_open
from src.DataOperation import select_operations
from src.databases import mongo_operations
from src.DataOperation import key_words_data_procesing

#
# scraper
#

# should stay somewhere in code / everything in code works and it's fine
# def scrap_data():
#     keywords = ["analiza danych", "data warehouse", "hurtownie danych", "analiza ekonometryczna", "ekonometria"]
#     keywords = ["big data", "hurtownie danych", "analiza ekonometryczna",
#                 "ekonometria"]  # "data mining", "analiza danych","data warehouse",
#     browser = Browser.Browser()
#     for keyword in keywords:
#         print(keyword, ' starts-4')
#         scraped = scraping_data_operations.scrap_page(browser, keyword)
#         print(keyword, ' ends')
#     scraping_data_operations.file_path()
# scrap_data()
data_to_process = []

keywords = ["Big Data", "Hurtownie danych", "Analiza ekonometryczna",
            "Ekonometria"]

keywords_data = []
for i in range(len(keywords)):
    print(keywords[i])
    data_to_process.append(key_words_data_procesing.key_word(keywords[i]))

for each in data_to_process:
    # print(each.keyword)
    each.related_keywords = mongo_operations.get_data_about_keyword(each.keyword)
    # print(each.related_keywords)

key_words_data_procesing.merge_two_related_keyword_dictionary(data_to_process[0], data_to_process[1])
# scraper end
#
# data = json_open.read_json_file("data/ekonometria.json")
# print(type(data))
# print(data.keys())
# print(len(data['publication']))
# select_operations.read_all_publication(data)

print('end')
