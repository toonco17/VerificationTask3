class Book:
  def __init__(self,
               book_id = 0,
               author = None,
               title = "Undefined",
               year = None,
               price = None,
               publisher = None,
               genre = None):

    self.book_id = book_id
    self.author = author
    self.title = title
    self.year = year
    self.price = price
    self.publisher = publisher
    self.genre = genre

  def checkParamTypes(self):
      pass

###
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

  def showAllOrders(self):
    pass

  def deliverOrders(self):
    pass

###
class Client:
  def __init__(self,
               client_id = "0",
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

###
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

###
class Id:
  def __init__(self,
               client_id = 0,
               book_id = 0,
               order_id = 0):

    self.client_id = client_id
    self.book_id = book_id
    self.order_id = order_id

  def counterIncrease(self):
    pass
