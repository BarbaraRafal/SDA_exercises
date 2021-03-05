from datetime import datetime
from typing import Tuple


class Book:
    ALLOWED_GENRES: Tuple = (
        "Fantasy",
        "Science Fiction",
        "Thriller",
        "Historical",
        "Romance",
        "Horror",
    )

    def __init__(self, title: str, author: str, book_genre: str) -> None:
        self.title = self.validate_title(title)
        self.author = author
        self.book_genre = self.validate_genre(book_genre)

    def validate_title(self, title: str) -> str:
        if not isinstance(title, str) or title == "":
            raise ValueError("Title is incorrect!")
        return title

    def validate_genre(self, genre: str) -> str:
        if genre not in self.ALLOWED_GENRES:
            raise ValueError(f"Genre:{genre} is incorrect")
        return genre

    def __repr__(self) -> str:
        return self.title


class Author:
    def __init__(self, name: str, year_of_birth: int) -> None:
        self._name = name
        self._year_of_birth = year_of_birth
        self._book_list = []

    def add_book(self, title: str, book_genre: str) -> None:
        self._book_list.append(self._create_book(title, book_genre))

    def _create_book(self, title: str, book_genre: str) -> Book:
        return Book(title, self._name, book_genre)

    @property
    def age(self):
        author_age = datetime.now().year - self._year_of_birth
        return author_age

    @property
    def name(self):
        return self._name

    @property
    def book_list(self):
        return self._book_list

    # def get_content_from_google(self):
    #     """This method is used to help understanding mocks"""
    #     content = requests.get("https://www.google.com")
    #     # print(content.text)
    #     return content.status_code


author1 = Author("Jan Kowalski", 1985)
author1.add_book("Tytuł", "Fantasy")
# author1.get_content_from_google()
