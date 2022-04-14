import pytest
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
import time
import threading


def thread_function(thread_id, ip, rest_port, results):
    tp = TestPlatform(ip_address=ip, rest_port=rest_port, trace=TestPlatform.TRACE_ALL)

    tp.info("connection formed and checking initial values")
    assert tp._connection._async_operation.request is None
    assert tp._connection._async_operation.poll_url is None
    assert tp._connection._async_operation.poll_headers is None
    assert tp._connection._async_operation.async_response is None

    if thread_id == 1:
        results.append(tp._connection._async_operation)
        tp.info("thread 1 will change values")
        tp._connection._async_operation.request = "changes done by thread 1"
        tp._connection._async_operation.poll_url = "http://my_url"
    else:
        tp.info("thread 2 will wait for the change to be completed by thread 1")
        time.sleep(5)
        results.append(tp._connection._async_operation)


def test_thread_safe_nature_of_connection_object(server):
    print(server)
    ip = server.split(":")[0]
    port = server.split(":")[1]
    results = []
    t1 = threading.Thread(
        target=thread_function, args=(1, ip, port, results), name="One"
    )
    t2 = threading.Thread(
        target=thread_function, args=(2, ip, port, results), name="Two"
    )
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    assert results[0].request == "changes done by thread 1"
    assert results[0].poll_url == "http://my_url"
    assert results[0].poll_headers is None
    assert results[0].async_response is None

    assert results[1].request is None
    assert results[1].poll_url is None
    assert results[1].poll_headers is None
    assert results[1].async_response is None


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
