import pytest
from ixnetwork_restpy import TestPlatform


def test_can_create_multiple_sessions_and_remove_all(test_platform):
    """
    multiple sessions can be created and all should be deleted
    :given: test_platform: a test platform object of restpy
    :when: add multiple sessions
    :then: should be able to remove all sessions
    """
    if test_platform.Platform == "linux":
        test_platform.Trace = TestPlatform.TRACE_INFO
        test_platform.Authenticate("admin", "admin")
        session_count = len(test_platform.Sessions.find())
        test_platform.info("{} existing sessions".format(session_count))
        sessions = (
            test_platform.Sessions.add().add().add().add().add().add().add().add()
        )
        test_platform.info("Starting remove of {} new sessions".format(len(sessions)))
        sessions.remove()
        test_platform.info(
            "{} sessions remaining".format(len(test_platform.Sessions.find()))
        )
        assert len(test_platform.Sessions.find()) == session_count
    else:
        pytest.skip("Test is not valid for %s platform" % test_platform.Platform)


if __name__ == "__main__":
    pytest.main(
        ["-s", "--server", "ajb-ubuntu-vm.lbj.is.keysight.com:443:linux", __file__]
    )
