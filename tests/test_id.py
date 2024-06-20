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

# wrongly initialized sample tests
def test_Id_init_client_id_incorrect():
    with pytest.raises(ValueError):
      ids = Id(client_id = -1)

def test_Id_init_book_id_incorrect():
    with pytest.raises(ValueError):
      ids = Id(book_id = -1)

def test_Id_init_order_id_incorrect():
    with pytest.raises(ValueError):
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
    with pytest.raises(ValueError):
      ids.counterIncrease("abracadabra123")
        
def test_Id_incr_emptyCode():
    ids = Id()
    with pytest.raises(ValueError):
      ids.counterIncrease("")

def test_Id_incr_wrongTypeCode():
    ids = Id()
    with pytest.raises(TypeError):
      ids.counterIncrease(1)
