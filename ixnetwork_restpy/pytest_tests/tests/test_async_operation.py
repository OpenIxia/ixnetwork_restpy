"""Tests to verify the async=True functionality of operations
"""
import pytest
from ixnetwork_restpy import TestPlatform


def test_async_operation(ixnetwork):
    # uncomment the following to see the full request and response
    # from ixnetwork_restpy import TestPlatform
    # ixnetwork.parent.parent.Trace = TestPlatform.TRACE_ALL
    ixnetwork.parent.parent.Trace = TestPlatform.TRACE_INFO

    # clear the configuration asynchronously
    ixnetwork.info("new config executing async")
    ixnetwork.NewConfig(async_operation=True)
    ixnetwork.info("async code executing during new config")
    response = ixnetwork.get_async_response()
    ixnetwork.info("retrieved async response")
    assert response is None


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
