import os.path
import sys
from src.PageObjects import main_search_page


def create_file_and_set_json_starting_brackets(file_name):
    file = open(file_name, 'w')
    file.writelines('{\n')
    return file


def close_file_and_set_json_ending_bracets(file):
    file.writelines("}")
    file.close()


def write_scraped_data_to_file(file, scraped_data):
    scraped_len = len(scraped_data)-1
    for i in range(scraped_len+1):
        print(i, 'iteracja ')
        if scraped_data[i] != scraped_data[scraped_len]:  # not last element
            file.writelines('"publication": \n')
            file.writelines(scraped_data[i].to_json())
            file.writelines(", \n")
            print('1')
        else:
            file.writelines('"publication": \n')  # last element
            file.writelines(scraped_data[i].to_json())
            print('2')


def create_file_path(file_name='newFile'):
    file_path_name = os.path.join(os.path.dirname(sys.argv[0]), 'data/')+file_name
    print(file_path_name)
    return file_path_name

# stat main functionality
def save_to_file(scraped):
    file_name = create_file_path('scraped.json')

    scraped_len = len(scraped)-1
    file = create_file_and_set_json_starting_brackets(file_name)
    print(scraped_len, 'scraped len')
    write_scraped_data_to_file(file, scraped)
    close_file_and_set_json_ending_bracets(file)


#  sample data scraping
def scrap_page(Browser):
    page = main_search_page.MainSearchPage(Browser)
    page = page.search_by_keyword("analiza fundamentalna")
    scraped = []
    for j in range(1):  # range(page.number_of_results_pages): # range(1):  #
        for i in range(2):  # range(len(page.results)):
            # create publication_page; scrap publication data; kill publication_page
            publication_page = page.go_to_result_index(i)
            scraped.append(publication_page.create_publication())
            page.driver.back()
            page.get_refresh_page_object()
        page = page.go_to_next_result_page()
    print('pobrano dane ')
    return scraped

