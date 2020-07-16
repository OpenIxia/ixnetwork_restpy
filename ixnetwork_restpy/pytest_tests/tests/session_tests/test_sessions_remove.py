import pytest


def test_can_create_multiple_sessions_and_remove_all(test_platform):
    """
        multiple sessions can be created and all should be deleted
        :given: test_platform: a test platform object of restpy
        :when: add multiple sessions 
        :then: should be able to remove all sessions
    """
    if test_platform.Platform == 'linux':
        test_platform.Authenticate('admin', 'admin')
        session_count = len(test_platform.Sessions.find())
        sessions = test_platform.Sessions.add().add()
        sessions.remove()
        assert(len(test_platform.Sessions.find()) == session_count)
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)

