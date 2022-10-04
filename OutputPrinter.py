import textwrap


class OutputPrinter:
    def __init__(self, wrap_chars):
        self._wrap_chars = wrap_chars

    def print_articles_list(self, list_):
        for element in list_:
            link, number, title = element
            print(number, title)

    def print_article(self, title, content):
        print(title, "\n\n")
        paragraphs = content.split('\n')
        for paragraph in paragraphs:
            text = textwrap.wrap(paragraph, self._wrap_chars)
            for line in text:
                print(line)
