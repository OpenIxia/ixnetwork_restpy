import pytest


def test_can_create_sessions(test_platform):
    """A session can be created

        :given: test_platform: a test platform object of restpy
        :when: called add session function
        :then: should create one and only one session
    """
    if test_platform.Platform == 'linux':
        try:
            test_platform.Authenticate('admin', 'admin')
            session = test_platform.Sessions.add()
            assert(len(session) == 1)
        finally:
            if 'session' in locals() and len(session) > 0:
                session.remove()        
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_can_set_session_name(test_platform):
    """The session name can be changed on a linux session
        
        :given: test_platform: a test platform object of restpy
        :when: called add session function
        :then: should be able to change the session name
    """
    if test_platform.Platform == 'linux':
        try:
            test_platform.Authenticate('admin', 'admin')
            session = test_platform.Sessions.add()
            session.Name = 'a new session name'
            assert session.Name == test_platform.Sessions.find(Id=session.Id).Name
        finally:
            if 'session' in locals() and len(session) > 0:
                session.remove()        
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_can_retrieve_sessions_by_id(test_platform):
    """A session can be retrieved by Id
        
        :given: test_platform: a test platform object of restpy
        :when: called add a session
        :then: should be able to retrieve a session by its Id
    """
    if test_platform.Platform == 'linux':
        try:
            test_platform.Authenticate('admin', 'admin')
            session = test_platform.Sessions.add()
            assert session.Id == test_platform.Sessions.find(Id=session.Id).Id
        finally:
            if 'session' in locals() and len(session) > 0:
                session.remove()
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_should_return_no_session_when_wrong_session_id_provided(test_platform):
    """
             sessions should not be retrieved by wrong ID
            :given: test_platform: a test platform object of restpy
            :when: add a session and call the sessions by wrong id
            :then: should not be able to retrieve session
    """
    if test_platform.Platform == 'linux':
        test_platform.Authenticate('admin', 'admin')
        assert len(test_platform.Sessions.find(Id=99999)) == 0
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_can_login_to_server_by_api_key(test_platform):
    """Authentication can be done by api key

        :given: test_platform: a test platform object of restpy
        :when: provided an appropriate api key
        :then: an attempt to get Sessions should not fail 
    """
    if test_platform.Platform == 'linux':
        test_platform.Authenticate('admin', 'admin')
        test_platform.ApiKey = test_platform.ApiKey
        session = test_platform.Sessions.find()
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_should_fail_on_wrong_auth_creds(test_platform):
    """
                 authentication module should throw error on wrong creds
                :given: test_platform: a test platform object of restpy
                :when: provided invalid uid/pwd credentials
                :then: should get UnauthorizedError
    """
    if test_platform.Platform == 'linux':
        from ixnetwork_restpy.errors import UnauthorizedError
        with pytest.raises(UnauthorizedError):
            test_platform.Authenticate('admin', 'admin2')
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_should_fail_on_wrong_api_key(test_platform):
    """
                 authentication module should throw error on wrong creds
                :given: test_platform: a test platform object of restpy
                :when: provided invalid api key
                :then: should get UnauthorizedError
    """
    if test_platform.Platform == 'linux':
        from ixnetwork_restpy.errors import UnauthorizedError
        test_platform.ApiKey = 'abc'
        with pytest.raises(UnauthorizedError):
            test_platform.Sessions.find()
    else:
        pytest.skip('Test is not valid for %s platform' % test_platform.Platform)

		
def test_can_add_remove_session(test_platform):	
	if test_platform.Platform == 'windows':
		#Add / Remove sessions
		sessions = test_platform.Sessions.add()
		assert(len(sessions) == 1)
		sessions.remove()
	else:
		pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_can_fetch_invalid_session(test_platform):	
	if test_platform.Platform == 'windows':
		#Fetching an invalid session
		sessions = test_platform.Sessions.find(Id=6)
		assert(len(sessions) == 0)
	else:
		pytest.skip('Test is not valid for %s platform' % test_platform.Platform)


def test_can_fetch_valid_session(test_platform):	
	if test_platform.Platform == 'windows':
		#Fetching an valid session
		sessions = test_platform.Sessions.find(Id=1)
		assert(len(sessions) == 1)
	else:
		pytest.skip('Test is not valid for %s platform' % test_platform.Platform)

	