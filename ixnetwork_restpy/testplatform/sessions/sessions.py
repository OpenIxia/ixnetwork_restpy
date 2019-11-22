from ixnetwork_restpy.base import Base
from ixnetwork_restpy.errors import IxNetworkError


class Sessions(Base):
    """Sessions class

    Manage IxNetwork sessions based on the connection information provided to the TestPlatform class.

    Child classes:  
        Sessions.Ixnetwork
    """
    _SDM_NAME = 'sessions'
    
    def __init__(self, parent):
        super(Sessions, self).__init__(parent)

    @property
    def Ixnetwork(self):
        """An instance of the Ixnetwork class
        
        Returns: 
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork.Ixnetwork):

        Raises: 
            ValueError: If the version of IxNetwork server is not suporrted. The minimum version supported is 8.42.
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
        ixnetwork = Ixnetwork(self)
        build_number = ixnetwork._connection._read('%s/ixnetwork/globals' % self.href)['buildNumber']
        from distutils.version import LooseVersion
        if LooseVersion(build_number) < LooseVersion('8.42'):
            raise ValueError('IxNetwork server version %s is not supported. The minimum version supported is 8.42' % build_number)
        ixnetwork._set_properties(ixnetwork._connection._read('%s/%s' % (self.href, Ixnetwork._SDM_NAME)))
        return ixnetwork
    
    @property
    def State(self):
        """The state of the session

        Returns:
            str
        """
        return self._properties['state'].upper()
    
    @property
    def ApplicationType(self):
        """The application type of the session

        Returns:
            str(ixnrest|quicktest)
        """
        return self._properties['applicationType']
    
    @property
    def Id(self):
        """The id of the session

        Returns:
            number
        """
        return self._properties['id']
    
    @property
    def UserId(self):
        """The user id of the session

        Returns:
            str
        """
        return self._properties['userId']
    
    @property
    def UserName(self):
        """The user name of the session

        Returns:
            str
        """
        return self._properties['userName']

    @property
    def Name(self):
        """The name of the session.
        Currently this is only supported on the linux API Server platform.

        Returns:
            str: if linux platform a valid session name else empty
        """
        return self._properties['name']
    @Name.setter
    def Name(self, value):
        if value is not None:
            if self._connection.platform == 'linux':
                self._connection._update('ixnetworkweb/api/v1/%s/%s' % (self._SDM_NAME, self.Id), payload={ 'sessionName': value })
                self._properties['name'] = value
            else:
                self.warn('Setting the session name is not supported on the %s platform' % self._connection.platform)
        elif self._connection.platform == 'linux' and 'name' not in self._properties:
            if 'sessionName' in self._properties:
                self._properties['name'] = self._properties['sessionName']
            else:
                self._properties['name'] = self._properties['configName']

    def Start(self):
        """Starts a session resource

        Returns:
            None
        """
        if self._connection.platform != 'windows':
            response = self._execute('start', payload={'applicationType': self.ApplicationType})
            if response is not None:
                self._set_properties(response, clear=True)
    
    def find(self, Id=None, Name=None):
        """Finds Sessions resources on the server and encapsulates the data in this instance.

        Args:
            Id (number): a valid session id
            Name (str): a valid session name
        
        Returns:
            obj(testplatform.sessions.sessions.Session): a Sessions object with found resources

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        responses = self._connection._read('%s/%s' % (self._parent.href, self._SDM_NAME))
        self._clear()
        for response in responses:
            if self._connection.platform == 'linux':
                if 'sessionName' in response:
                    response['name'] = response['sessionName']
                else:
                    response['name'] = response['configName']
            else:
                response['name'] = ''
            if response['applicationType'] == 'ixnetwork':
                response['applicationType'] = 'quicktest'
            if Id is not None and str(response['id']) == str(Id):
                self._set_properties(response)
            elif Name is not None and response['name'] == Name:
                self._set_properties(response)
            elif Id is None and Name is None:
                self._set_properties(response)
        return self

    def add(self, ApplicationType='ixnrest', Name=None):
        """Adds a new sessions resource on the server and encapsulates the data in this instance.
        Two types of sessions can be created, an ixnrest session or a quicktest web session.
        The quicktest web session can only be created when the TestPlatform.Platform type is 'linux'

        Args:
            ApplicationType (str[ixnrest|quicktest]): The type of session to be started
            Name (str): The name of the session

        Returns:
            obj(testplatform.sessions.sessions.Session): a Sessions object

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        if ApplicationType == 'quicktest' and self.parent.Platform == 'linux':
            applicationType = 'ixnetwork'
        elif ApplicationType == 'ixnrest':
            applicationType = 'ixnrest'
        else:
            raise ValueError('%s is not a supported SessionType' % ApplicationType)
        ApplicationType = None
        self._create(locals())
        if self._properties['applicationType'] == 'ixnetwork':
            self._object_properties[self.index]['applicationType'] = 'quicktest'
        if self._connection.platform == 'linux':
            self.Start()
        self.Name = Name
        return self

    def update(self, Name=None):
        self.Name = Name
        return self
        
    def remove(self):
        """Deletes all the encapsulated sessions resources from the server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        try:
            for properties in self._object_properties:
                self._connection._execute('%s/operations/stop' % properties['href'], payload=None)
            self._delete()
        except IxNetworkError as e:
            if e._status_code not in [404, 405]:
                raise e
        finally:
            self._clear()
    
    def GetObjectFromHref(self, href):
        """Given an href get the corresponding object
        
        References are used to establish relationships between disparate nodes.
        This allows a user to get an object using a reference from a node.
        For example:
            A /vport node has a ConnectedTo property that is a reference to an /availableHardware/chassis/card/port node.
            A user can get a vport and use this method to get the port node in order to clear ownership
        
        Args:
            href (str): A valid href reference

        Returns:
            obj | None: If the reference is valid an ixnetwork_restpy object or None if the reference cannot be resolved
        """
        try:
            node = self
            for piece in href[href.find('ixnetwork'):].split('/'):
                if piece.isdigit():
                    for item in node:
                        if item.href.split('/').pop() == piece:
                            node = node._read(item.href)
                            break
                else:
                    class_name = '%s%s' % (piece[0].upper(), piece[1:])
                    node = getattr(node, class_name)
                    if hasattr(node, 'find') is True:
                        node.find()
            return node
        except:
            return None

    def GetFileList(self, remote_directory=None):
        """Get a list of files from the IxNetwork session instance

        Args:
            remote_directory (str): A remote directory path

        Returns:
            dict(root_path, list(dict(filename, filesize)): A list of all the files for a given directory
        """
        href = '%s/ixnetwork/files' % self.href
        if remote_directory is not None:
            href = '%s?absolute=remote_directory'
        return self._connection._read(href)

    def DownloadFile(self, remote_filename, local_filename = None):
        """Download a file from the IxNetwork session instance

        Args:
            remote_fileanme (str): the name of the remote file
            local_filename (str): the name that the remote contents will be saved to
        
        Returns:
            str: the local file name
        """
        return self._connection._get_file('%s/ixnetwork' % self.href, remote_filename=remote_filename, local_filename=local_filename)
    
    def UploadFile(self, local_filename, remote_filename=None):
        """Upload a file to the IxNetwork session instance

        Args:
            local_filename (str): the name of the local file
            remote_filename (str): the name that will be used when saving the file on the IxNetwork sesson instance
        
        Returns:
            dict(filename, filesize): Details of the file that was uploaded
        """
        return self._connection._put_file('%s/ixnetwork' % self.href, local_filename=local_filename, remote_filename=remote_filename)