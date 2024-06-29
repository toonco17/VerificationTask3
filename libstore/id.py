class Id:
  def __init__(self, client_id = 0, book_id = 0, order_id = 0):

    self.client_id = client_id
    self.book_id = book_id
    self.order_id = order_id

    if (type(self.client_id) != int):
      raise ValueError("client_id is not int")
    if (self.client_id < 0):
      raise ValueError("client_id is < 0")

    if (type(self.book_id) != int):
      raise ValueError("book_id is not int")
    if (self.book_id < 0):
      raise ValueError("book_id is < 0")

    if (type(self.order_id) != int):
      raise ValueError("order_id is not int")
    if (self.order_id < 0):
      raise ValueError("client_id is < 0")

  def counterIncrease(self, counter):
    match counter:
      case "c":
        self.client_id += 1

      case "b":
        self.book_id += 1

      case "o":
        self.order_id += 1

      case _:
        raise ValueError("Wrong counter code, please choose c - client_id, b - book_id or o - order_id")

