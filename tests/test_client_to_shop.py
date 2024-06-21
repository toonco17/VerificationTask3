import pytest

# Here we're ging to work with the client-to-shop functionality:
# A client can send their order to the shop. When they do it, an order is created with the current books
# from the basket. If an order is not confirmed yet, the client can cancel it.
# I gave up on some functions like setting delivery time and sending back the books after delivery,
# 'cause they seem to be a waste of time in the context of the task,
# so if you reeeeealy need them, I'll implement them later.

from libstore.client import Client
from libstore.shop import Shop
from libstore.order import Order
from libstore.id import Id
from libstore.book import Book

# Tests for checkout function
def test_checkoutAnOrder_shopAccept_book():
  book = Book(title = "Warriors")
  shop = Shop(library = {book[book_id] : book})
  client = Client(basket = {book[book_id] : book})
  ord_id = ids.order_id
  
  # This means we have 1 book, 1 client and 0 orders
  ids = Id(book_id = 1, client_id = 1, order_id = 0)
  
  client.checkOutAnOrder(shop = shop, ids = ids)
  assert shop.orders[ord_id].books[book.book_id].title == "Warriors"

def test_checkoutAnOrder_shopAccept_client_id_check():
  book = Book(title = "Warriors")
  shop = Shop(library = {book[book_id] : book})
  client = Client(basket = {book[book_id] : book}) 
  ord_id = ids.order_id
  
  ids = Id(book_id = 1, client_id = 1, order_id = 0)
  client.checkOutAnOrder(shop = shop, ids = ids)
  assert shop.orders[ord_id].client_id == client.client_id

def test_checkOutAnOrder_order_id_in_ids_increases():
  book = Book(title = "Warriors")
  shop = Shop(library = {book[book_id] : book})
  client = Client(basket = {book[book_id] : book}) 
  ord_id = ids.order_id
  
  ids = Id(book_id = 1, client_id = 1, order_id = 0)
  client.checkOutAnOrder(shop = shop, ids = ids)
  assert ids.order_id == 1

def test_checkoutAnOrder_basic_emptyOrder():
  client = Client(basket = {})
  shop = Shop(library = {book[book_id] : book})
  ord_id = ids.order_id
  ids = Id(book_id = 1, client_id = 1, order_id = 0)
  
  with pyrest.raises(KeyError):
    client.checkOutAnOrder(shop = shop, ids = ids)

def test_checkoutAnOrder_order_in_orders():
  book = Book(title = "Warriors")
  shop = Shop(library = {book[book_id] : book})
  client = Client(basket = {book[book_id] : book}, orders = {}) 
  ord_id = ids.order_id
  
  ids = Id(book_id = 1, client_id = 1, order_id = 0)
  client.checkOutAnOrder(shop = shop, ids = ids)
  assert len(client.order() == 1

# Tests for cancelling function
def test_cancelOrder_orderDeleteFromShop():
  book = Book(title = "Warriors")
  shop = Shop(library = {book[book_id] : book})
  ordr = Order(order_status = 0)
  client = Client(orders = { ordr.order_id : ordr })
  client.cancelOrder(ordr.order_id)
  assert len(shop.orders) == 0
