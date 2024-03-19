import pytest


class Article:
    def __init__(self, author, magazine, title):
        print("Initializing Article...")
        print("Title:", title)
        if not isinstance(title, str):
            print("Title is not a string.")
            raise ValueError("Article title must be a string.")
        if not (5 <= len(title) <= 50):
            print("Title length is invalid.")
            raise ValueError("Article title must be between 5 and 50 characters.")
        print("Title is valid.")
        self._author = author
        self._magazine = magazine
        self._title = title
        print("Article initialized successfully.")

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

