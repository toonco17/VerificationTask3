from book import Book
from order import Order
from shop import Shop
from id import Id

class Client:
  def __init__(self,
               client_id = 0,
               client_password = "0000",
               basket = dict(),
               orders = dict()):

    self.client_id = client_id
    self.client_password = client_password
    self.basket = basket
    self.orders = orders

  def addBooksToBasket(self):
    pass

  def removeBooksFromBasket(self):
    pass

  def showBasket(self, fullInfo = False):
    pass

  def showOrders(self):
    pass

  def checkoutAnOrder(self):
    pass

  def declineOrderOrSendBack(self):
    pass
