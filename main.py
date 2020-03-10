import bs4 as bs
import requests


def define_source(link):
    source = requests.get(link)
    return source

def define_soup(source_link):
    soup = bs.BeautifulSoup(source_link.text, 'lxml')
    return soup

def get_components_list(sp):
    component_list = []
    ticker, company_name = ''
    component_table = sp.find('table', { 'class' : 'W(100%) M(0) BdB Bdc($finLightGray)'})
    component_table_body = component_table.find('tbody')
    for component_table_row in component_table_body:
        component_table_row.find_all('tr', { 'class' : 'BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s)'})
        for component_table_data in component_table_row.find_all('td', { 'class' : 'Py(10px) Ta(start) Pend(10px)'})[0].find('a'):
            ticker = component_table_data
        for component_table_data in component_table_row.find_all('td' , { 'class' : 'Py(10px) Ta(start) Pend(10px)'})[-1]:
            company_name = component_table_data
            
            




def open_files():
    file = open("links.txt", "r")
    for line in file:
        soup = define_soup(define_source(line))
        get_components_list(soup)
    file.close()

open_files()