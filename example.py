# Example for pytest

def add( a, b ):
    return a + b

def test_add ():
    assert add( 2, 3 ) == 5
    assert add( 'space', 'ship' ) == 'spaceship'

def subtract( a, b ):
    return a + b    # <--- fix this in step 8

# uncomment the following in step 5
#def test subtract ():
#    assert subtract( 3, 3) == -1
