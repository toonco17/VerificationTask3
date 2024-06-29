from libstore.book import Book

class Order:
  def __init__(self, order_id = 0, client_id = 0, books = dict(), order_status = 0):

    self.order_id = order_id
    self.client_id = client_id
    self.books = books
    self.order_status = order_status
    
    self.possible_order_statuses = {0 : "Awaiting confirmation", 1 : "Delivering", 2 : "Delivered", 3 : "Declined"}

    if (type(self.order_id) != int):
      raise ValueError("order_id must be int")
    if (self.order_id < 0):
      raise ValueError("order_id must be > 0")

    if (type(self.client_id) != int):
      raise ValueError("client_id must be int")
    if (self.client_id < 0):
      raise ValueError("client_id must be > 0")

    for book_id in self.books:
      if (type(book_id) != int):
        raise ValueError("in books dict: some book_id is not int")
      if (book_id < 0):
        raise ValueError("in books dict: some book_id is < 0")
      if (type(self.books[book_id]) != Book):
        raise TypeError("Some book in the order is fucked: book_id = ", book_id)
      else: continue

    for book_id in self.books:
      if self.books[book_id].book_id != book_id:
        raise ValueError("book_ids' mismatch!")
      else: continue
    
    if (self.order_status not in [0, 1, 2, 3]):
      raise ValueError("Invalid order status")
    else: pass

  def checkOrderStatus(self):
    print(self.possible_order_statuses[self.order_status])

  def changeOrderStatus(self, newStatus = 0):
    if (type(newStatus) == int and newStatus not in [0, 1, 2, 3]):
      raise ValueError("Wrong status code value: choose 0-3")
    if (type(newStatus) != int):
      raise TypeError("Wrong status code type")
    else: pass
    self.order_status = newStatus

  def showBooksInThisOrder(self, fullInfo = False):
    for book_id in self.books:
      self.books[book_id].showInfo(fullInfo = fullInfo)
