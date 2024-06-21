from libstore.book import Book
from libstore.order import Order
from libstore.id import Id

class Client:
  def __init__(self,
               client_id = 0,
               client_password = "0000",
               basket = dict()):

    self.client_id = client_id
    self.client_password = client_password
    self.basket = basket

    if (type(self.client_id) != int or self.client_id < 0):
      raise ValueError("client_id must be non-negative int")

    if (type(self.client_password) != str):
      raise TypeError("Client pass must be a string")

  def addBooksToBasket(self, book):
    self.basket[book.book_id] = book

  def removeBooksFromBasket(self, book_id):
    if book_id in self.basket:
      del self.basket[book_id]
    else:
      raise KeyError("There is no such book in the basket.")

  def checkoutAnOrder(self, all_orders : dict, ids : Id):
    pass

  def cancelOrder(self, order_id, all_orders):
    pass

# Выяснилось, что циркулярную инициализацию делать нельзя (что нормальным людям очевидно, но я ж особенный),
# поэтому придется вынести взаимодействие клиента и магазина во внешний словарь all_orders.
