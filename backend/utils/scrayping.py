import re
# from urllib import request

from bs4 import BeautifulSoup


def get_page_content(response):
    # get page file
    # response = request.urlopen(url)

    # soup = BeautifulSoup(response)
    # response.close()

    soup = BeautifulSoup(response)

    # extract text
    main_text = soup.find('div', class_='main_text')
    tags_to_delete = main_text.find_all(['rp', 'rt'])
    for tag in tags_to_delete:
        tag.decompose()
    main_text = main_text.get_text()
    main_text = main_text.replace('\r', '').replace(
        '\n', '').replace('\u3000', '')

    main_text = re.sub('([！。])', r'\1\n', main_text)  # 。と！で改行
    text_list = main_text.splitlines()

    return text_list
