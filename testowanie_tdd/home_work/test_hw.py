import unittest
from home_work.home_work_jadwiga import Book


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

    def test_if_author_attr_is_correct(self):
        book = Book(**self.book_kwargs)
        self.assertEqual(self.book_kwargs["author"], book.author)

    def test_repr_method_returns_correct_value(self):
        book = Book(**self.book_kwargs)
        self.assertEqual(str(book), book.title)

    def test_title_when_string_is_given(self):
        book = Book(**self.book_kwargs)
        self.assertIsInstance(book.title, str)

    def test_title_when_not_string_is_given(self):
        self.book_kwargs["title"] = 123
        with self.assertRaises(ValueError):
            Book(**self.book_kwargs)

    def test_title_cannot_be_empty(self):
        self.book_kwargs["title"] = ""
        with self.assertRaises(ValueError):
            Book(**self.book_kwargs)

    def test_not_valid_genre_raises_value_error(self):
        self.book_kwargs["book_genre"] = "Not valid"
        with self.assertRaises(ValueError):
            Book(**self.book_kwargs)

    def test_not_valid_genre_raises_value_error_with_correct_message(self):
        self.book_kwargs["book_genre"] = "Not valid"
        error_msg_regex = f"^Genre:{self.book_kwargs['book_genre']} is incorrect$"
        with self.assertRaisesRegex(ValueError, error_msg_regex):
            Book(**self.book_kwargs)

    def test_title_when_not_string_is_given_error_msg(self):
        self.book_kwargs["title"] = 123
        with self.assertRaisesRegex(ValueError, "^Title is incorrect!$"):
            Book(**self.book_kwargs)
