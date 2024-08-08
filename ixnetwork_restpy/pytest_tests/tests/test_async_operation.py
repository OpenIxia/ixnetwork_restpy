"""Tests to verify the async=True functionality of operations
"""

import pytest
from ixnetwork_restpy import TestPlatform, BadRequestError


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


def test_async_operation_for_errors(ixnetwork):
    # uncomment the following to see the full request and response
    # from src.ixnetwork_restpy import TestPlatform
    # ixnetwork.parent.parent.Trace = TestPlatform.TRACE_ALL
    ixnetwork.parent.parent.Trace = TestPlatform.TRACE_INFO

    # checking if async code returns proper errors or not
    ixnetwork.info("traffic apply executing async")
    ixnetwork.Traffic.Apply(async_operation=True)
    ixnetwork.info("async code executing during traffic apply")
    try:
        ixnetwork.get_async_response()
    except BadRequestError as e:
        ixnetwork.info("retrieved async response error")
        assert e.status_code == 400
        assert "Error in L2/L3 Traffic Apply" in e.message


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
