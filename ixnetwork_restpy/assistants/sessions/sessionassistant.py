"""High level assistant class to consolidate and simplify the following:

    Creating IxNetwork session or connecting to an IxNetwork session
    Renaming an IxNetwork session
    Get the TestPlatform instance
    Get the Sessions instance
    Get the Ixnetwork instance
    Get a PortMapAssistant instance
    Get a StatViewAssistant instance
"""
from ixnetwork_restpy.connection import Connection
from ixnetwork_restpy.errors import *
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
from ixnetwork_restpy.assistants.statistics.statviewassistant import StatViewAssistant
from ixnetwork_restpy.assistants.ports.portmapassistant import PortMapAssistant


class SessionAssistant(object):
    LOGLEVEL_NONE = Connection.TRACE_NONE
    LOGLEVEL_INFO = Connection.TRACE_INFO
    LOGLEVEL_WARNING = Connection.TRACE_WARNING
    LOGLEVEL_REQUEST = Connection.TRACE_REQUEST
    LOGLEVEL_REQUEST_RESPONSE = Connection.TRACE_REQUEST_RESPONSE
    LOGLEVEL_ALL = Connection.TRACE_ALL
    APP_TYPE_IXNETWORK = 'ixnrest'
    APP_TYPE_QUICKTEST = 'quicktest'

    def __init__(self, **kwargs):
        """Create a session or connect to an existing session. 
        Provides access to the TestPlatform, Sessions, Ixnetwork, PortMapAssistant and StatViewAssistant classes.

        Description
        -----------
            If SessionId is None and SessionName is None a new session will be created.
            If SessionId is not None then an attempt will be made to connect to a session with that id.
            If SessionId is None and SessionName is not None then an attempt will be to connect to a session with that name. 
            If Sessionid is not None and SessionName is not None then an attempt will be made to connect to a session with that id and if successful the session will be renamed to SessionName
            Set the LogLevel parameter to LOGLEVEL_INFO for more information on the connection attempts to the TestPlatform.

        Args
        ----
            IpAddress (str): The ip address of the TestPlatform to connect to where test sessions will be created or connected to. 
                The default is 127.0.0.1
            RestPort (int): The rest port of the TestPlatform to connect to.
                The default is 11009
            UserName (str): The username to be used for authentication
                The default is admin
            Password (str): The password to be used for authentication
                The default is admin
            ApiKey (str): The api key to be used for authentication
                The default is None
                If set the ApiKey will override the UserName and Password 
            IgnoreEnvProxy (bool): Ignore the environment proxy bypass settings.
                The default is False
            VerifyCertificates (bool): Verify the certificate
                The default is False
            LogFilename (str): The name of the logger log filename.
                The default is None and all logger output will be directed to the console.
            LogLevel (str(LOGLEVEL_NONE|LOGLEVEL_INFO)): The logger log level that will be set.
                The default is LOGLEVEL_NONE and there should be no logger output
            SessionId (int): The id of the session to connect to. 
                The default is None
            SessionName (str): The name of the session to connect to.  
                The default is None
            ApplicationType (str(APP_TYPE_IXNETWORK|APP_TYPE_QUICKTEST)): The type of IxNetwork middleware test session to create
                The default is APP_TYPE_IXNETWORK
            ClearConfig (bool): Clear the current configuration
                The default is False

        Raises
        ------
            ConnectionError: If the TestPlatform cannot be reached. 
            UnauthorizedError: Authentication failed, access is unauthorized
            NotFoundError: The SessionId was not found on the test platform
            ValueError: If the version of IxNetwork server is not supported. The minimum version supported is 8.42.
        """
        IpAddress = kwargs.get('IpAddress', '127.0.0.1')
        RestPort = kwargs.get('RestPort', 11009)
        UserName = kwargs.get('UserName', 'admin')
        Password = kwargs.get('Password', 'admin')
        ApiKey = kwargs.get('ApiKey', None)
        IgnoreEnvProxy = kwargs.get('IgnoreEnvProxy', False)
        VerifyCertificates = kwargs.get('VerifyCertificates', False)
        LogFilename = kwargs.get('LogFilename', None)
        LogLevel = kwargs.get('LogLevel', SessionAssistant.LOGLEVEL_NONE)
        SessionId = kwargs.get('SessionId', None)
        SessionName = kwargs.get('SessionName', None)
        ApplicationType = kwargs.get('ApplicationType', SessionAssistant.APP_TYPE_IXNETWORK)
        ClearConfig = kwargs.get('ClearConfig', False)

        testplatform = TestPlatform(ip_address=IpAddress, 
            rest_port=RestPort, 
            log_file_name=LogFilename, 
            ignore_env_proxy=IgnoreEnvProxy,
            verify_cert=VerifyCertificates,
            trace=LogLevel)
        if ApiKey is not None:
            testplatform.Authenticate = ApiKey
        elif UserName is not None and Password is not None:
            testplatform.Authenticate(UserName, Password)
        session = None
        if SessionId is not None:
            session = testplatform.Sessions.find(Id=SessionId)
            if len(session) == 0:
                raise NotFoundError('Session %s does not exist on %s:%s', (SessionId, testplatform.Hostname, testplatform.RestPort))
            session.Name = SessionName
        elif SessionName is not None:
            session = testplatform.Sessions.find(Name=SessionName)
        if session is None or len(session) == 0:
            session = testplatform.Sessions.add(ApplicationType, Name=SessionName)
        self._ixnetwork = session.Ixnetwork
        if ClearConfig is True:
            self._ixnetwork.NewConfig()

    @property
    def TestPlatform(self):
        return self._ixnetwork.parent.parent

    @property
    def Session(self):
        return self._ixnetwork.parent

    @property
    def Ixnetwork(self):
        return self._ixnetwork

    def PortMapAssistant(self):
        """Get an instance of the PortMapAssistant class
        """
        return PortMapAssistant(self._ixnetwork)

    def StatViewAssistant(self, ViewName, Timeout=180, LocalCsvStorage=None):
        """Get an instance of the StatViewAssistant class
        """
        return StatViewAssistant(self._ixnetwork, ViewName, Timeout, LocalCsvStorage)
        