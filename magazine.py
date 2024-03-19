from article import Article


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author
            authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]

    def article_titles(self):
        return [article.title for article in self._articles]

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

# Example usage
if __name__ == "__main__":
    magazine_name = "Tech Magazine"
    magazine_category = "Technology"
    magazine = Magazine(magazine_name, magazine_category)
    
    print("Magazine Name:", magazine.name)
    print("Magazine Category:", magazine.category)
