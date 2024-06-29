# На момент написания тестов на магазин умер интернет в лабе, теперь Anydesk не работает. Он думает, я его не переиграю, с#ка.

import pytest

# Basic tests for the Shop class.
# The functionality of the Shop class is mainly about operating with books in its library (add-delete) and working with orders.
# The orders implementation will be made after we finish with the Client order functionality.

# The Shop parameters are:
# shop_name     : string
# shop_password : string
# library       : dict of Books or empty dict
# orders        : dict of orders or empty dict

from libstore.shop import Shop
from libstore.book import Book
from libstore.id import Id

def test_addNewBooksToLib():
  book = Book(book_id = 1, title = "Warriors")
  shop = Shop()
  shop.addNewBooksToLib(book)
  assert shop.library[book.book_id].title == "Warriors"

def test_removeBooksFromLib():
  book = Book(book_id = 1, title = "Warriors")
  shop = Shop(library = {book.book_id : book})
  shop.removeBookFromLib(book.book_id)
  with pytest.raises(KeyError):
    print(shop.library[book.book_id].title)

#added tests for better coverage
def test_additional_removeBook():
  shop = Shop(library = {})
  with pytest.raises(KeyError):
    shop.removeBookFromLib(book_id = 1)
