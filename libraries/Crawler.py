from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, start_chapter=None, end_chapter=None):
        url_data = urlparse(start_chapter)
        self.base_url = "{}://{}".format(url_data.scheme, url_data.netloc)
        self.start_chapter = start_chapter
        self.end_chapter = end_chapter
        self.current_chapter = start_chapter

    def get_book_name(self):
        req = requests.get(self.start_chapter)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup.find('li', class_="caption").text.strip()

    def next_chapter_url(self):
        req = requests.get(self.current_chapter)
        soup = BeautifulSoup(req.text, 'html.parser')
        next_list_tag = soup.find('li', class_="next")
        anchor_tag = next_list_tag.find(class_="btn btn-link")
        link = anchor_tag.attrs.get('href')
        return link

    def get_chapter_content(self, url):
        print('[x] Getting content for', url)
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        story = soup.find('div', class_="fr-view")
        chapter_name = soup.find('div', class_="caption clearfix").text.strip()
        return chapter_name, '\n'.join(i.text for i in story.contents if i != '\n')

    def get_next_chapter_url_until_end(self):
        while True:
            next_chapter = self.next_chapter_url()
            full_chapter_url = self.base_url + next_chapter
            if full_chapter_url != self.end_chapter:
                self.current_chapter = full_chapter_url
                yield full_chapter_url
            else:
                break

    def start_crawling(self):
        first_chapter_name, first_chapter_content = self.get_chapter_content(self.start_chapter)
        yield first_chapter_name, first_chapter_content

        for next_chapter in self.get_next_chapter_url_until_end():
            chapter_name, content = self.get_chapter_content(next_chapter)
            yield chapter_name, content

        end_chapter_name, end_chapter_content = self.get_chapter_content(self.end_chapter)
        yield end_chapter_name, end_chapter_content

    def start(self):
        book_name = self.get_book_name()
        book_path = "book-files/{}.txt".format(book_name)
        with open(book_path, 'w') as book_file:
            for chapter_name, content in self.start_crawling():
                book_file.write(chapter_name)
                book_file.write('\n')
                book_file.write(content)
                book_file.write('\n')
        print("[x] Finished crawling {}".format(book_name))
        return book_name, book_path
