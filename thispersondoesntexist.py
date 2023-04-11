from concurrent.futures import ThreadPoolExecutor

import cloudscraper

import time
import os
import shutil

if not os.path.exists("femme"):
    os.mkdir("femme")
if not os.path.exists("homme"):
    os.mkdir("homme")


# timestamp milliseconds
def get_timestamp():
    return str(int(time.time() * 1000))


def random_pic_generator(gender):
    scraper = cloudscraper.create_scraper()
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    }
    req = scraper.get(
        'https://this-person-does-not-exist.com/new?time=' + get_timestamp() + '&gender='+gender+'&etnic=all',
        headers=header)
    url = req.json()['src']
    print('https://this-person-does-not-exist.com' + url)
    r2 = scraper.get('https://this-person-does-not-exist.com' + url, headers=header)
    print(r2.status_code)
    filename = url.split('/')[-1]
    if gender == 'male':

        with open("homme/" + filename, 'wb') as f:
            f.write(r2.content)
    else:
        with open("femme/" + filename, 'wb') as f:
            f.write(r2.content)



liste = ['female' for i in range(10000)]
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(random_pic_generator, liste)



