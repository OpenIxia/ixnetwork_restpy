from ixnetwork_restpy.errors import *


def test_operation_improper_name (ixnetwork):
    try:
        ixnetwork.NewConfig1()
        assert Exception('Error should have been raised')
    except AttributeError as e:
        pass

def test_operation_returns_404_error (ixnetwork):
    try:
        ixnetwork.LoadConfig('arg1', 'arg2', 'arg3')
        assert Exception('Error should have been raised')
    except NotFoundError as e:
        pass
