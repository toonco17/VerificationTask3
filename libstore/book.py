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
