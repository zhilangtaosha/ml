import requests

def join_lists(urls1, urls2):
    ary = []
    for url in urls1:

        if url not in ary:
            ary.append(url)

    for url in urls2:

        if url not in ary:
            ary.append(url)

    return ary

def get_link(text):
    href_number = text.find("href=")
    if href_number == -1:
        return None,0

    start_number = text.find('"',href_number)
    end_number = text.find('"', start_number + 1)
    url = text[start_number + 1:end_number]
    return url, end_number

def get_all_links(initial_url):

    page = requests.get(initial_url)
    text = page.text
    ary = []
    
    while True:
        url, end_postion = get_link(text)
        if url:
            #print(url)
            text = text[end_postion:]
            ary.append(url)
        else:
            return ary

#initial_url = "https://diveintocode-crawling-sample.herokuapp.com/"
#print(get_all_links(initial_url))

# !!! 以下のコードを変更しました !!!
crawl_urls = ["https://diveintocode-crawling-sample.herokuapp.com/"]
already_crawled_urls = []
# 小課題1 pop関数をcrawl_urlsに使用し、返却された要素でクローリングさせる !!!  
#scheduled_to_crawl = crawl_urls.pop()

#obtained_urls = get_all_links(scheduled_to_crawl)

# !!! 小課題2 以下にcrawl_urlsにobtained_urlsを結合させるコードを記述する !!!

#total_urls = []
#for obtained_url in obtained_urls:
#    total_urls.extend(get_all_links(obtained_url))
#crawl_urls = total_urls

while True:
    try:
        scheduled_to_crawl = crawl_urls.pop()
    except IndexError:
        break

    if scheduled_to_crawl not in already_crawled_urls:

        obtained_urls = get_all_links(scheduled_to_crawl)
        crawl_urls = join_lists(crawl_urls, obtained_urls)
        already_crawled_urls.append(scheduled_to_crawl)
    
        print(already_crawled_urls)

#    print(len(join_lists(crawl_urls, obtained_urls)))


# ['https://diveintocode-crawling-sample.herokuapp.com/careers', 'https://diveintocode-crawling-sample.herokuapp.com/weather', 'https://diveintocode-crawling-sample.herokuapp.com/curriculum', 'https://diveintocode-crawling-sample.herokuapp.com/']
