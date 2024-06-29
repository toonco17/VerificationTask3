import pytest

# Tests for the Book class.
# The only function we would need here is the check that the created book
# has correct params: e.g. book_id is a positive integer, not NULL or str.
# By design, the function would check all the book's params and return
# a sequence of 0s and 1s, where 0 would be for a correct type, 1 - for an err.

# The book parameters are:
#    book_id   : non-negative integer ONLY
#    author    : string, list of strings, or None
#    title     : string
#    year      : non-negative integer or None
#    price     : non-negative float with precision 2, non-negative integer, or None
#    publisher : string or None
#    genre     : string, list of strings, or None

from libstore.book import Book

# tests for book_id
def test_checkParamTypes_book_id_default():
    book = Book()
    return_code = book.checkParamTypes()
    assert return_code[0] == 0

def test_checkParamTypes_book_id_manual():
    book = Book(book_id = 24)
    return_code = book.checkParamTypes()
    assert return_code[0] == 0

def test_checkParamTypes_book_id_negative():
    book = Book(book_id = -1)
    return_code = book.checkParamTypes()
    assert return_code[0] == 1

def test_checkParamTypes_book_id_nonint():
    book = Book(book_id = 17.23)
    return_code = book.checkParamTypes()
    assert return_code[0] == 1

def test_checkParamTypes_book_id_None():
    book = Book(book_id = None)
    return_code = book.checkParamTypes()
    assert return_code[0] == 1

def test_checkParamTypes_book_id_wrongType():
    book = Book(book_id = "kryakryamazafaka")
    return_code = book.checkParamTypes()
    assert return_code[0] == 1


# tests for author
def test_checkParamTypes_author_default():
    book = Book()
    return_code = book.checkParamTypes()
    assert return_code[1] == 0

def test_checkParamTypes_author_manual():
    book = Book(author = "Elma Trou")
    return_code = book.checkParamTypes()
    assert return_code[1] == 0

def test_checkParamTypes_author_None():
    book = Book(author = None)
    return_code = book.checkParamTypes()
    assert return_code[1] == 0 # We desided to consider Undefined author and None author to be both correct. The only params that cannot be None are book_id and title

def test_checkParamTypes_author_multiple():
    book = Book(author = ["Elma Trou", "Rau Ravellie"])
    return_code = book.checkParamTypes()
    assert return_code[1] == 0

def test_checkParamTypes_author_multiple_wrongType():
    book = Book(author = ["Elma Trou", 17.23])
    return_code = book.checkParamTypes()
    assert return_code[1] == 1

def test_checkParamTypes_author_wrongType():
    book = Book(author = 17.23)
    return_code = book.checkParamTypes()
    assert return_code[1] == 1


# tests for title
def test_checkParamTypes_title_default():
    book = Book()
    return_code = book.checkParamTypes()
    assert return_code[2] == 0

def test_checkParfamTypes_title_manual():
    book = Book(title = "Versatile Chronics")
    return_code = book.checkParamTypes()
    assert return_code[2] == 0

def test_checkParamTypes_title_None():
    book = Book(title = None)
    return_code = book.checkParamTypes()
    assert return_code[2] == 1 # We can be unaware of the book's author, but never about its title

def test_checkParamTypes_title_empty():
    book = Book(title = "")
    return_code = book.checkParamTypes()
    assert return_code[2] == 1

def test_checkParamTypes_title_wrongType():
    book = Book(title = 17.23)
    return_code = book.checkParamTypes()
    assert return_code[2] == 1

# tests for year
def test_checkParamTypes_year_defauld():
    book = Book()
    return_code = book.checkParamTypes()
    assert return_code[3] == 0

def test_checkParamTypes_year_manual():
    book = Book(year = 2025)
    return_code = book.checkParamTypes()
    assert return_code[3] == 0

def test_checkParamTypes_year_manual_negative():
    book = Book(year = -5000)
    return_code = book.checkParamTypes()
    assert return_code[3] == 0 # This seems strange, but negative values are for the b.c. epoch, so we consider them correct, too

def test_checkParamTypes_year_manual_nonint():
    book = Book(year = 17.23)
    return_code = book.checkParamTypes()
    assert return_code[3] == 1 # Meanwhile, whatever positive or negative, year must be an integer

def test_checkParamTypes_year_None():
    book = Book(year = None)
    return_code = book.checkParamTypes()
    assert return_code[3] == 0

def test_checkParamTypes_year_wrongType():
    book = Book(year = "kryakryamazafaka")
    return_code = book.checkParamTypes()
    assert return_code[3] == 1


# tests for price
def test_checkParamTypes_price_default():
    book = Book()
    return_code = book.checkParamTypes()
    assert return_code[4] == 0

def test_checkParamTypes_price_manual_int():
    book = Book(price = 1999)
    return_code = book.checkParamTypes()
    assert return_code[4] == 0

def test_checkParamTypes_price_manual_float():
    book = Book(price = 1999.99)
    return_code = book.checkParamTypes()
    assert return_code[4] == 0

def test_checkParamTypes_price_manual_float_wrongPrecision1():
    book = Book(price = 1999.9)
    return_code = book.checkParamTypes()
    assert return_code[4] == 0

def test_checkParamTypes_price_manual_float_wrongPrecision2():
    book = Book(price = 1999.999)
    return_code = book.checkParamTypes()
    assert return_code[4] == 1

def test_checkParamTypes_price_manual_float_mootPrecision():
    book = Book(price = 1999.90)
    return_code = book.checkParamTypes()
    assert return_code[4] == 0

def test_checkParamTypes_price_manual_negative():
    book = Book(price = -1999)
    return_code = book.checkParamTypes()
    assert return_code[4] == 1

def test_checkParamTypes_price_None():
    book = Book(price = None)
    return_code = book.checkParamTypes()
    assert return_code[4] == 0

def test_checkParamTypes_price_wrongType():
    book = Book(price = "oohyoutouchmytralala")
    return_code = book.checkParamTypes()
    assert return_code[4] == 1


# tests for publisher
def test_checkParamTypes_publisher_default():
    book = Book()
    return_code = book.checkParamTypes()
    assert return_code[5] == 0

def test_checkParamTypes_publisher_manual():
    book = Book(publisher = "AST")
    return_code = book.checkParamTypes()
    assert return_code[5] == 0

def test_checkParamTypes_publisher_None():
    book = Book(publisher = None)
    return_code = book.checkParamTypes()
    assert return_code[5] == 0

def test_checkParamTypes_publisher_wrongType():
    book = Book(publisher = 17.23)
    return_code = book.checkParamTypes()
    assert return_code[5] == 1


#tests for genre
def test_checkParamTypes_genre_default():
    book = Book()
    return_code = book.checkParamTypes()
    assert return_code[6] == 0

def test_checkParamTypes_genre_manual():
    book = Book(genre = "dark fantazy")
    return_code = book.checkParamTypes()
    assert return_code[6] == 0

def test_checkParamTypes_genre_None():
    book = Book(genre = None)
    return_code = book.checkParamTypes()
    assert return_code[6] == 0

def test_checkParamTypes_genre_wrongType():
    book = Book(genre = 17.23)
    return_code = book.checkParamTypes()
    assert return_code[6] == 1

def test_checkParamTypes_genre_multiple():
    book = Book(genre = ["dark fantazy", "autobiography"])
    return_code = book.checkParamTypes()
    assert return_code[6] == 0

def test_checkParamTypes_genre_multiple_wrongType():
    book = Book(genre = ["dark fantazy", 17.23])
    return_code = book.checkParamTypes()
    assert return_code[6] == 1

# I had to think about the additional function, showInfo(), showing the book parameters, because this func seems to be needed several times here and there,
# including the tests for Order class lol =D
# It's more about refactoring already, but still I'm to implement it within the batch of the basic functionality

### idk how to test it another way lol ###
def printBookInfo(book : Book, fullInfo = False):
    print("book_id = ", book.book_id)
    print("author = ",  book.author)
    print("title = ", book.title)

    if (fullInfo == True):
      print("year = ", book.year)
      print("price = ", book.price)
      print("publisher = ", book.publisher)
      print("genre = ", book.genre)

      print("\n")

def test_showInfo_short():
    book = Book()
    assert book.showInfo(False) == printBookInfo(book, False)
    
def test_showInfo_full():
    book = Book()
    assert book.showInfo(True) == printBookInfo(book, True)

#additional tests (for better coverage lol)
#check author
def test_book_additional_checkParamTypes_check_author_severalAuthors_flagZero():
    book = Book(author = ["Elma Trou", "toonco17"])
    return_code = book.checkParamTypes()
    assert return_code[1] == 0

def test_book_additional_checkParamTypes_check_author_flagNonzero():
    book = Book(author = 17)
    return_code = book.checkParamTypes()
    assert return_code[1] == 1
