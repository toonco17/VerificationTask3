from libstore.book import Book
from libstore.id import Id
from libstore.order import Order

class Shop:
  def __init__(self,
               shop_name = "My Shop",
               shop_password = "0000",
               library = dict()):

    self.shop_name = shop_name
    self.shop_password = shop_password
    self.library = library

  def addNewBooksToLib(self, book : Book):
    self.library[book.book_id] = book
    
  def removeBookFromLib(self, book_id):
    if (book_id in self.library):
      del self.library[book_id]
    else:
      raise KeyError("No such book in the library")

  def deliverOrders(self):
    pass
    
  def declineOrders(self):
    pass
