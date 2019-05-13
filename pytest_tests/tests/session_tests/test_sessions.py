import pytest

def test_can_create_sessions(test_platform):
    """
        multiple sessions can be created
        :given: test_platform: a test platform object of restpy
        :when: called add session function
        :then: should create session
    """
    if test_platform._connection._platform == 'windows':
        pytest.skip('Test is not possible for windows platform')
    test_platform.Authenticate('admin','admin')
    num_of_sessions = 5
    session_list = list()
    for _ in range(num_of_sessions):
        session_list.append(test_platform.Sessions.add())

    for session in session_list:
        session.remove()

    assert len(session_list) == 5

def test_can_retrieve_sessions_by_id(test_platform):
    """
         sessions can be retrieved by ID
        :given: test_platform: a test platform object of restpy
        :when: add multiple sessions and call the sessions by id
        :then: should be able to retrieve sessions
    """
    if test_platform._connection._platform == 'windows':
        pytest.skip('Test is not possible for windows platform')
    test_platform.Authenticate('admin', 'admin')
    num_of_sessions = 5
    session_id_list = []
    for _ in range(num_of_sessions):
        session_id_list.append(test_platform.Sessions.add().Id)

    for id in session_id_list:
        session = test_platform.Sessions.find(Id=id)
        session.remove()


def test_should_return_no_session_when_wrong_session_id_provided(test_platform):
    """
             sessions should not be retrieved by wrong ID
            :given: test_platform: a test platform object of restpy
            :when: add a session and call the sessions by wrong id
            :then: should not be able to retrieve session
    """
    if test_platform._connection._platform == 'windows':
        pytest.skip('Test is not possible for windows platform')
    test_platform.Authenticate('admin', 'admin')
    session = test_platform.Sessions.add()
    assert len(test_platform.Sessions.find(Id=99999)) == 0
    session.remove()

def test_can_login_to_server_by_api_key(test_platform):
    """
             authentication can be done by api key
            :given: test_platform: a test platform object of restpy
            :when: provided appropriate api key
            :then: should get authenticate
    """
    if test_platform._connection._platform == 'windows':
        pytest.skip('Test is not possible for windows platform')

    import os
    test_platform.ApiKey = os.environ.get('API_KEY')
    test_platform.Sessions.find()

def test_should_fail_on_wrong_auth_creds(test_platform):
    """
                 authentication module should throw error on wrong creds
                :given: test_platform: a test platform object of restpy
                :when: provided inappropriate api key
                :then: should not get authenticate
    """
    if test_platform._connection._platform == 'windows':
        pytest.skip('Test is not possible for windows platform')

    from ixnetwork_restpy.errors import UnauthorizedError
    test_platform.ApiKey = 'abc'
    with pytest.raises(UnauthorizedError):
        test_platform.Authenticate('admin', 'admin2')


def test_should_fail_on_wrong_api_key(test_platform):
    """
                 authentication module should throw error on wrong creds
                :given: test_platform: a test platform object of restpy
                :when: provided inappropriate api key
                :then: should not get authenticate
    """
    if test_platform._connection._platform == 'windows':
        pytest.skip('Test is not possible for windows platform')

    from ixnetwork_restpy.errors import UnauthorizedError
    test_platform.ApiKey = 'abc'
    with pytest.raises(UnauthorizedError):
        test_platform.Authenticate('admin', 'admin2')