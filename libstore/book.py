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
    return_code = ""

    #check book_id
    if (type(self.book_id) == int and (self.book_id >= 0)):
      return_code += "0"
    else:
      return_code += "1"

    #check author
    if (type(self.author) == str or self.author == None):
      return_code += "0"
    elif (type(self.author) == list):
      for auth in self.author:
        flag = 0
        if (type(auth) != str):
          return_code += "1"
          flag = 1
          break
      if (flag == 0):
        return_code += "0"

    # check title
    if (type(self.title) == str and self.title != ""):
      return_code += "0"
    else:
      return_code += "1"

    # check year
    if (type(self.year) == int or self.year == None):
      return_code += "0"
    else:
      return_code += "1"

    # check price
    if ((type(self.price) == int and self.price >= 0) or self.price == None):
      return_code += "0"
    elif (type(self.price == float) and self.price >= 0.00):
      str_price_reversed = (str(self.price))[::-1]
      if (str_price_reversed[2] != "."):
        if (str_price_reversed[1] == "."):
          return_code += "0"
        else:
          return_code += "1"
    else:
      return_code += "1"

    # check publisher
    if (type(self.publisher) != str and self.publisher != None):
      return_code += "1"
    else:
      return_code += "0"

    #check genre
    if (type(self.genre) == str or type(self.genre) == list or self.genre == None):
      if (type(self.genre) == list):
        flag = 0
        for gen in self.genre:
          if (type(gen) != str):
            return_code += "1"
            flag = 1
            break
        if (flag == 0):
          return_code += "0"
      else:
        return_code += "0"
    else:
      return_code += "1"

    return return_code
