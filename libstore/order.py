from libstore.book import Book

class Order:
  def __init__(self,
               order_id = 0,
               client_id = 0,
               books = dict(),
               order_status = 0):

    self.order_id = order_id
    self.client_id = client_id
    self.books = books
    self.order_status = order_status
    
    self.possible_order_statuses = {0 : "Awaiting confirmation", 1 : "Delivering", 2 : "Delivered", 3 : "Declined"}

  def checkOrderStatus(self):
    print(self.possible_order_statuses[self.order_status])

  def changeOrderStatus(self, newStatus = 0):
    self.order_status = newStatus

  def showBooksInThisOrder(self, fullInfo = False):
    for book_id in self.books:
      self.books[book_id].showInfo(fullInfo = fullInfo)
