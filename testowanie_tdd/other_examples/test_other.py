import unittest
from home_work.jadwiga_hw import Book
class BookTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.book_kwargs = {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "book_genre": "Fantasy",
        }
    def test_if_title_attr_is_correct(self):
        book = Book(**self.book_kwargs)
        self.assertEqual(book.title, self.book_kwargs["title"])
    def test_if_title_attr_is_correct_when_empty_string(self):
        title = ""
        self.book_kwargs["title"] = title
        book = Book(**self.book_kwargs)
        self.assertEqual(book.title, title)
    def test_if_author_attr_is_correct(self):
        author = "Book Author"
        self.book_kwargs["author"] = author
        book = Book(**self.book_kwargs)
        self.assertEqual(author, book.author)
    def test_repr_method_returns_correct_value(self):
        book = Book(**self.book_kwargs)
        print(self.book_kwargs)
        self.assertEqual(repr(book), book.title)