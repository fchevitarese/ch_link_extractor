import argparse
import requests

from subprocess import call

from bs4 import BeautifulSoup as bs


def parse_url(url):
    counter = 0
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    with open('urls.txt', 'w') as links:
        for link in soup.find_all('link', {'itemprop': 'contentUrl'}):
            links.write(link['href'])
            links.write('\n')
            counter += 1
    links.close()
    print('Found {counter} links.'.format(counter=counter))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', required='True')
    parser.add_argument('-d, --download')
    args = parser.parse_args()

    
    if args.link:
        parse_url(args.link)
    
    print(args)
    if 'download' in args:
        call('aria2c', '-i urls.txt')



if __name__ == '__main__':
    main()
