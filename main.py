import requests
from bs4 import BeautifulSoup

def _save_metadata_into_file(i, metadata):
    file_num = str(i)+".txt"
    f = open(file_num, "w+")
    f.write(metadata)
    f.close()

def _remove_attrs(soup):
    without_tag = []
    for tag in soup:
        without_tag.append(tag.text.strip())
    return without_tag

url = 'https://eur-lex.europa.eu/search.html?name=browse-by%3Aeu-parliament-regulations&type=named&qid=1635890648945'
web_page = requests.get(url).text

"meta-data"
soup = BeautifulSoup(web_page, 'lxml')
all_meta = soup.findAll(class_ ="SearchResult")
i = 1
for meta in all_meta:

    url_html = meta.findAll('a', class_ ="piwik_download")
    page_url = url_html[1].attrs.get('href')

    "name of the document"
    get_name = meta.findAll(class_ = "title")
    name = get_name[0].contents[0]

    "rest of metadata: celex num, languages, author, date"
    metadata = meta.findAll('dd')
    notag_metadata = _remove_attrs(metadata)

    "code of doc"
    code = meta.findAll('p')
    notag_code = _remove_attrs(code)

    all_meta = []
    all_meta.append(name)
    all_meta.append(notag_metadata)
    all_meta.append(notag_code)

    _save_metadata_into_file(i, all_meta)
    i = i + 1


