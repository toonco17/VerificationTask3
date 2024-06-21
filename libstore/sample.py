from book import Book
from client import Client

def showBooks(book1 : Book, book2 : Book, fullInfo = False):
    book1.showInfo(fullInfo = fullInfo)
    book2.showInfo(fullInfo = fullInfo)


def test_showBasket_short():
    book1 = Book(book_id = 1, title = "Warriors")
    book2 = Book(book_id = 2, title = "Shantaram")
    client = Client(basket = {book1.book_id : book1, book2.book_id : book2})
    client.showBasket(fullInfo = False)
    showBooks(book1, book2, False)

def test_showBasket_full():
    book1 = Book(book_id = 1, title = "Warriors")
    book2 = Book(book_id = 2, title = "Shantaram")
    client = Client(basket = {book1.book_id : book1, book2.book_id : book2})
    assert client.showBasket(fullInfo = True) == showBooks(book1, book2, True)
    
test_showBasket_short()
