import os.path
import sys
from src.PageObjects import main_search_page

def file_path(file_name = 'newFile'):
    file_path_name = os.path.join(os.path.dirname(sys.argv[0]), 'data/')+file_name
    print(file_path_name)
    return file_path_name

def save_to_file(scraped):# os.pathrealpath(__file__)) represent script file path
    file_name = file_path('scraped.json')

    scraped_len = len(scraped)-1
    file = open(file_name, 'w')
    file.writelines('{\n')
    print(scraped_len, 'scraped len')

    for i in range(scraped_len+1):
        print(i, 'iteracja ')
        if scraped[i] != scraped[scraped_len]:  # not last element
            file.writelines('"publication": \n')
            file.writelines(scraped[i].to_json())
            file.writelines(", \n")
            print('1')
        else:
            file.writelines('"publication": \n')  # last element
            file.writelines(scraped[i].to_json())
            print('2')
    file.writelines("}")
    file.close()


#  sample data scraping
def scrap_page(Browser):
    page = main_search_page.MainSearchPage(Browser)
    page = page.search_by_keyword("analiza fundamentalna")
    scraped = []
    json_file = []
    for j in range(1):# range(page.number_of_results_pages): # range(1):  #
        for i in range(2): #  range(len(page.results)):
            #  create publication_page; scrap publication data; kill publication_page
            publication_page = page.go_to_result_index(i)
            scraped.append(publication_page.create_publication())
            publication_page = None
            page.driver.back()
            page.get_refresh_page_object()
        page = page.go_to_next_result_page()
    print(scraped)
    print('pobrano dane ')
    return scraped
