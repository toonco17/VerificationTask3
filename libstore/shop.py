from libstore.book import Book
from libstore.client import Client
from libstore.id import Id
from libstore.order import Order

class Shop:
  def __init__(self,
               shop_name = "My Shop",
               shop_password = "0000",
               library = dict(),
               orders =  dict()):

    self.shop_name = shop_name
    self.shop_password = shop_password
    self.library = library
    self.orders = orders

  def addNewBooksToLib(self):
    pass

  def showAllBooksInLib(self):
    pass

  def removeBookFromLib(self):
    pass
    
  def editLibBooks(self):
    pass

#  def showAllOrders(self):
#    pass

#  def deliverOrders(self):
#    pass
    
#  def declineOrders(self):
#    pass
    
  def changeShopName(self):
    pass
  
  def changeShopPassword(self):
    pass
