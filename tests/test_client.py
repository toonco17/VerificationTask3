import pytest

# Basic tests for the Client class.
# As the Client class depends on the Shop class, and the same is true for the Shop on Client,
# we have to firstly implement the independent functions of both of them,
# and then make tests for and implement inerconnections.
# Basic Client class functionality is about working with the books and basket (cart, but i've lost
# the word, so it's basket now lol).

# The Client parameters are:
#    client_id         : non-negative int ONLY
#    client_password   : string
#    basket            : dict of Books, keys: book_id, or empty dict
#    orders            : dict of Orders, keys: order_id, or empty dict

from libstore.book import Book
from libstore.client import Client

# check initialization
def test_Client_client_id_incorrect():
    with pytest.raises(ValueError):
        client = Client(client_id = -1)

def test_Client_client_password_incorrect():
    with pytest.raises(TypeError):
        client = Client(client_password = 1234)

### i'm too lazy to check basket and orders initialization, ma sorry

def test_addBooksToBasket():
    book = Book(book_id = 1, title = "Warriors")
    client = Client()
    client.addBooksToBasket(book)
    assert client.basket[book.book_id].title == "Warriors"

def test_removeBooksFromBasket():
    book = Book(book_id = 1, title = "Warriors")
    client = Client(basket = {book.book_id : book})
    client.removeBooksFromBasket(book.book_id)
    with pytest.raises(KeyError):
        print(client[book.book_id])

# Я все еще не знаю, как написать тест на функцию, которая тупо печатает и ничего не возвращает
# Поэтому я не буду ее писать, лол, вообще ее имплементировать не буду
# Когда сломается - тогда и станет понятно, как надо было предсказывать это дерьмо
