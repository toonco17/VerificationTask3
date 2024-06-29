from libstore.book import Book
from libstore.id import Id
from libstore.order import Order

class Shop:
  def __init__(self, shop_name = "My Shop", shop_password = "0000", library = dict()):

    self.shop_name = shop_name
    self.shop_password = shop_password
    self.library = library

  def addNewBooksToLib(self, book : Book):
    self.library[book.book_id] = book
    
  def removeBookFromLib(self, book_id):
    if (book_id in self.library):
      del self.library[book_id]
    else: raise KeyError("No such book in the library")

  def deliverOrders(self, order_id, all_orders):
    if order_id in all_orders:
      for book_id in all_orders[order_id].books:
        if book_id not in self.library:
          raise KeyError("No such book in the library: book_id = ", book_id)
        else: continue
      all_orders[order_id].order_status = 2
      return all_orders
    else: raise KeyError("No such order in all_orders")
    
  def declineOrders(self, order_id, all_orders):
    if order_id in all_orders:
      all_orders[order_id].order_status = 3
      return all_orders
    else: raise KeyError("No such order in all_orders")
