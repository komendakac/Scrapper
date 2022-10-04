import OutputPrinter
import Scrapper
import argparse
news = "https://www.realmadryt.pl/aktualnosci"

parser = argparse.ArgumentParser(prog='siteview', description='View the internet site in terminal')
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-n', '--number', action='store', required=False, type=int, help='number of article to open')
group.add_argument('-l', '--link', action='store', required=False, type=str, help='link to article')
group.add_argument('-a', '--article-list', action='store_true', required=False, default=False, help='article list')
parser.add_argument('-r', action='store', required=False, type=int, nargs=2, help='Number of first and last article')
parser.add_argument('-w', action='store', required=False, type=int, help='Number of chars before warp')

args = parser.parse_args()
arguments = vars(args)

if arguments['w'] is not None:
    printer = OutputPrinter.OutputPrinter(arguments['w'])
else:
    printer = OutputPrinter.OutputPrinter(100)

if arguments['article_list'] is True:
    news_list = Scrapper.RmplArticleList(news)
    if arguments['r'] is not None:
        articles_list = news_list.get_list(arguments['r'][0], arguments['r'][1])
    else:
        articles_list = news_list.get_list()
    printer.print_articles_list(articles_list)
elif arguments['number'] is not None:
    news_list = Scrapper.RmplArticleList(news)
    article_link = news_list.get_list(arguments['number'], arguments['number'] + 1)[0][0]
    article = Scrapper.RmplArticle(article_link)
    printer.print_article(article.get_title(), article.get_body())
else:
    article_link = arguments['link']
    article = Scrapper.RmplArticle(article_link)
    printer.print_article(article.get_title(), article.get_body())
