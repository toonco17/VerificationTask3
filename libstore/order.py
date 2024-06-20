from libstore.book import Book

class Order:
  def __init__(self,
               order_id = 0,
               client_id = 0,
               books = dict(),
               order_status = "awaiting confirmation"):

    self.order_id = order_id
    self.client_id = client_id
    self.books = books
    self.order_status = order_status

  def checkOrderStatus(self):
    pass

  def changeOrderStatus(self):
    pass

  def showBooksInThisOrder(self):
    pass
