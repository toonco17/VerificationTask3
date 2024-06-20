import pytest

# Tests for the Id class.
# An id class example is to be called from the main() function where all other
# initialisations happen. So, it only gotta have three counters: for books, for clients
# and for orders. This class is independent from the others, just like Book and Order classes.
# The counterIncrease function of Id class would have is the counter increaser for those three counters.
# Parallel runs are too complicated for me here, so the counters will work just so:
# given a command and a key - make counter++ for the needed counter.
# I'll also implement a check that an Id class sample with incorrect (negative or non-integer) ids will not pass,
# but it's not really supposed to be needed in the program structure Ive come up with.

# The id parameters are:
#    client_id   : non-negative integer ONLY
#    book_id     : non-negative integer ONLY
#    order_id    : non-negative integer ONLY

from libstore.id import Id

# tests for the incorrect ids values
def test_Id_initvalues_default():
    ids = Id()
    if (ids.client_id < 0):
      raise ValueError("client_id < 0. client_id must be > 0")
    if (type(ids.client_id) != int):
      raise TypeError("client_id is not int now. client_id must be int")
      
    if (ids.book_id < 0):
      raise ValueError("book_id < 0. book_id must be > 0")
    if (type(ids.book_id) != int):
      raise TypeError("book_id is not int now. book_id must be int")
      
    if (ids.order_id < 0):
      raise ValueError("order_id < 0. order_id must be > 0")
    if (type(ids.order_id) != int):
      raise TypeError("order_id is not int now. order_id must be int")

# wrongly initialized sample tests
def test_Id_init_client_id_incorrect():
    with pytest.raises(ValueError("Wrong client_id initialized. client_id must be > 0")):
      ids = Id(client_id = -1)

def test_Id_init_book_id_incorrect():
    with pytest.raises(ValueError("Wrong book_id initialized. book_id must be > 0")):
      ids = Id(book_id = -1)

def test_Id_init_order_id_incorrect():
    with pytest.raises(ValueError("Wrong order_id initialized. order_id must be > 0")):
      ids = Id(book_id = -1)

# tests for correctly printed increments
def test_Id_incr_client_id():
    ids = Id(client_id = 0)
    ids.counterIncrease("c")   
    assert ids.client_id == 1

def test_Id_incr_book_id():
    ids = Id(book_id = 0)
    ids.counterIncrease("b")
    assert ids.book_id == 1

def test_Id_incr_order_id():
    ids = Id(order_id = 0)
    ids.counterIncrease("o")
    assert ids.order_id == 1

#tests for wrongly printer increments
def test_Id_incr_wrongCode():
    ids = Id()
    with pytest.raises(ValueError("Wrong code. Please, choose between c - client_id, b - book_id, o - order_id increments")):
      ids.counterIncrease("abracadabra123")
        
def test_Id_incr_emptyCode():
    ids = Id()
    with pytest.raises(ValueError("Wrong code. Please, choose between c - client_id, b - book_id, o - order_id increments")):
      ids.counterIncrease("")

def test_Id_incr_wrongTypeCode():
    ids = Id()
    with pytest.raises(TypeError("Wrong code. Please, choose between c - client_id, b - book_id, o - order_id increments")):
      ids.counterIncrease(1)
