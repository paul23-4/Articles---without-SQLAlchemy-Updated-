import pytest
from article import Article
from author import Author
from magazine import Magazine

class TestArticle:
    def test_init(self):
        author = "John Doe"
        magazine = "Tech Magazine"
        title = "My Article"
        article = Article(author, magazine, title)
        assert article.author == author
        assert article.magazine == magazine
        assert article.title == title

    def test_author(self):
        author = "John Doe"
        magazine = "Tech Magazine"
        title = "My Article"
        article = Article(author, magazine, title)
        assert article.author == author

    def test_magazine(self):
        author = "John Doe"
        magazine = "Tech Magazine"
        title = "My Article"
        article = Article(author, magazine, title)
        assert article.magazine == magazine

    def test_title(self):
        author = "John Doe"
        magazine = "Tech Magazine"
        title = "My Article"
        article = Article(author, magazine, title)
        assert article.title == title
