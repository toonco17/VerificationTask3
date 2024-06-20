import pytest

# Tests for the Order class.
# The order class is used in the Client class, in the Shop class and in the functions which
# operate with those (client account manager function, shop manager function, initialization functions and main, their templates aint't added yet).
# Order class only needs to know the Book class bc it conrains books. It also has parameters
# referring to the owner's id and its own id, and a status.
# As for functions, we might want to check or change that status, plus show the books in the
# order we are working with.

# The Order parameters are:
#    order_id     : non-negative int ONLY
#    client_id    : non-negative int ONLY
#    books        : dictionary, empty or with Book objects
#    order_status : string - "Awaiting confirmation", "Delivering", "Declined", "Delivered"

# Possible order statuses: {0 : "Awaiting confirmation", 1 : "Delivering", 2 : "Delivered", 3 : "Declined"}


from libstore.order import Order
from libstore.book import Book

# check initialization
def test_Order_order_id_incorrect():
    with pytest.raises(ValueError):
      ordr = Order(order_id = -1)

def test_Otder_client_id_incorrect():
    with pytest.raises(ValueError):
      ordr = Order(client_id = -1)
      
def test_Order_books_incorrect_book_id():
    with pytest.raises(ValueError):
      sample_book = Book()
      ordr = Order(books = {-1: sample_book})
      
def test_Order_books_incorrect_book_type():
    with pytest.raises(TypeError):
      sample_book = "shalala"
      ordr = Order(books = {-1: sample_book})

def test_Order_books_book_id_mismatch():
    with pytest.raises(ValueError):
      sample_book = Book(book_id = 0)
      ordr = Order(books = {1 : sample_book})

def test_Order_order_status_wrongValue():
    with pytest.raises(ValueError):
      ordr = Order(order_status = "shalala")

# check functions
def test_checkOrderStatus():
    ordr = Order(order_status = 0)
    assert ordr.checkOrderStatus() == print("Awaiting confirmation") 
    
def test_changeOrderStatus():
    ordr = Order(order_status = 0)
    ordr.changeOrderStatus(1)
    assert ordr.checkOrderStatus() == print("Delivering")

def test_changeOrderStatus_nonexistent():
    ordr = Order(order_status = 0)
    with pytest.raises(ValueError):
      ordr.changeOrderStatus(-1)

def test_changeOrderStatus_wrongType():
    ordr = Order(order_status = 0)
    with pytest.raises(TypeError):
      ordr.changeOrderStatus("kalashmala")

def test_showBooksInThisOrder_empty():
    ordr = Order()
    assert ordr.showBooksInThisOrder() == print("The order is empty")

### helper func###
def showInfo(book1 : Book, book2 : Book, fullInfo = False):
    book1.showInfo(fullInfo = fullInfo)
    book2.showInfo(fullInfo = fullInfo)

def test_showBooksInThisOrder_short():
    book1 = Book(book_id = 1)
    book2 = Book(book_id = 2)
    ordr = Order(books = {book1.book_id : book1, book2.book_id : book2})
    assert ordr.showBooksInThisOrder(False) == showInfo(book1, book2, False)

def test_showBooksInThisOrder_short():
    book1 = Book(book_id = 1)
    book2 = Book(book_id = 2)
    ordr = Order(books = {book1.book_id : book1, book2.book_id : book2})
    assert ordr.showBooksInThisOrder(True) == showInfo(book1, book2, True)
