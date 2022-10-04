import requests
from bs4 import BeautifulSoup


class ArticleList:
    def get_list(self, start=0, end=10):
        pass


class Article:
    def get_title(self):
        pass

    def get_body(self):
        pass


class RmplArticle(Article):
    def __init__(self, url):
        self._url = url
        self._page = requests.get(self._url)

    def get_title(self):
        soup = BeautifulSoup(self._page.content, "html.parser")
        title = soup.find(itemprop="description").text
        return title

    def get_body(self):
        soup = BeautifulSoup(self._page.content, "html.parser")
        body = soup.find(itemprop="articleBody")
        paragraphs = body.findAll("p")
        article_text = ""
        for paragraph in paragraphs:
            if paragraph.text == "* * *":
                break
            article_text += paragraph.text + "\n"
        return article_text


class RmplArticleList(ArticleList):
    def __init__(self, url):
        self._link_start = "https://www.realmadryt.pl"
        self._url = url
        self._articles = []

    def get_list(self, start=0, end=10):
        if start % 10 == 0:
            site_number = int(start / 10)
        else:
            site_number = int(start / 10) + 1
            url = self._url + "/" + str(site_number)
            self.set_site_articles(url)
        i = start
        infos = []
        while i < end:
            if i % 10 == 0:
                site_number += 1
                url = self._url + "/" + str(site_number)
                self.set_site_articles(url)
            info = self._articles[i % 10].find(class_="cf shift-margin_2-bottom")
            link = ""
            title = ""
            for a in info.find_all('a', href=True):
                link = self._link_start + a["href"]
                title = a.text
            infos.append([link, i, title])
            i += 1
        return infos

    def set_site_articles(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        self._articles = soup.find_all("li", class_="news-article")
