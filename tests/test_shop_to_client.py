import pytest

# The nearly same as for client, nah
# The shop making delivery is literally changing the status and that's all lol
# The "delivering" status seem not to be used now, bc i'm tired lol

from libstore.shop import Shop
from libstore.order import Order
from libstore.book import Book

def test_deliverOrders_normal():
  book = Book()
  shop = Shop(library = {book.book_id : book})
  ordr = Order(books = {book.book_id : book})
  all_orders = {ordr.order_id : ordr}
  all_orders = shop.deliverOrders(order_id = ordr.order_id, all_orders = all_orders)
  assert all_orders[ordr.order_id].order_status == 2

def test_deliverOrders_emptyOrder():
  book = Book(book_id = 5)
  shop = Shop(library = {book.book_id : book})
  ordr = Order(books = {})
  all_orders = {}
  with pytest.raises(KeyError):
    all_orders = shop.deliverOrders(order_id = ordr.order_id, all_orders = all_orders)

def test_deliverOrders_noBookInLib():
  book = Book(book_id = 5)
  shop = Shop(library = {})
  ordr = Order(books = {book.book_id : book})
  all_orders = {ordr.order_id : ordr}
  with pytest.raises(KeyError):
    all_orders = shop.deliverOrders(order_id = book.book_id, all_orders = all_orders)

def test_declineOrders():
  book = Book(book_id = 5)
  ordr = Order(books = {book.book_id : book})
  shop = Shop(library = {book.book_id : book})
  all_orders = {}
  all_orders[ordr.order_id] = ordr
  all_orders = shop.declineOrders(ordr.order_id, all_orders)
  assert all_orders[ordr.order_id].order_status == 3

#additional tests for better coverage
def test_additional_deliverOrders():
  shop = Shop(library = {})
  book = Book()
  all_orders = dict()
  ordr = Order(books = {book.book_id : book})
  all_orders.append(ordr)
  with pytest.raises(KeyError):
    shop.deliverOrders(order_id = ordr.order_id, all_orders = all_orders)
