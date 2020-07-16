from ixnetwork_restpy.errors import *


def test_operation_returns_400_error (ixnetwork):
    try:
        ixnetwork.ConnectCardById('2323232')
        raise Exception('Error should have been raised')
    except Exception as e:
        print(e)

def test_operation_returns_404_error (ixnetwork):
    try:
        ixnetwork.ConnectCardById('2323232', 'asdf')
        raise Exception('Error should have been raised')
    except Exception as e:
        print(e)
