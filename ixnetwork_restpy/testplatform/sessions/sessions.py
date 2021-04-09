# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.errors import IxNetworkError
from ixnetwork_restpy.multivalue import Multivalue
import time


class Sessions(Base):
    """The Sessions class encapsulates a list of sessions resources that are managed by the user.
    A list of resources can be retrieved from the server using the Sessions.find() method.
    The list can be managed by the user by using the Sessions.add() and Sessions.remove() methods.
    """
    _SDM_NAME = 'sessions'
    
    def __init__(self, parent):
        super(Sessions, self).__init__(parent)
        self._build_numbers = []

    @property
    def Ixnetwork(self):
        """      
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork.Ixnetwork): An instance of the Ixnetwork class

        Raises
        ------
        - ValueError: Version of IxNetwork server is not supported. Minimum version supported is 8.52.
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
        ixnetwork = Ixnetwork(self)
        response = ixnetwork._connection._read('%s/ixnetwork/globals' % self.href)
        build_number = response['buildNumber']
        if build_number not in self._build_numbers:
            user_name = response['username']
            from distutils.version import LooseVersion
            if len(build_number) == 0:
                self.warn('Using DEBUG version of IxNetwork api server')
            elif LooseVersion(build_number) < LooseVersion('8.52'):
                raise ValueError('IxNetwork api server version %s is not supported. The minimum version supported is 8.52' % build_number)
            else:
                self.info('Using IxNetwork api server version %s' % (build_number))
                self.info('User info %s' % (user_name))
            self._build_numbers.append(build_number)
        ixnetwork._set_properties(ixnetwork._connection._read('%s/%s' % (self.href, Ixnetwork._SDM_NAME)))
        return ixnetwork
    
    @property
    def State(self):
        """The state of the session

        Returns
        -------
        - str: The state of the session
        """
        return self._properties['state'].upper()
    
    @property
    def ApplicationType(self):
        """The application type of the session

        Returns
        -------
        - str(ixnrest | quicktest): The application type of the session
        """
        return self._properties['applicationType']
    
    @property
    def Id(self):
        """The id of the session

        Returns
        -------
        - number: The instance identifier of the session
        """
        return self._properties['id']
    
    @property
    def UserId(self):
        """The user id of the session

        Returns
        -------
        - str: The user id of the session
        """
        return self._properties['userId']
    
    @property
    def UserName(self):
        """The user name of the session

        Returns
        -------
        - str: The username of the session
        """
        return self._properties['userName']

    @property
    def Name(self):
        """The name of the session.

        Returns
        -------
        - str: The name of the session. If the platform is linux then it is a valid session name else empty
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

        Returns
        -------
        - obj(testplatform.sessions.sessions.Session): self

        Raises
        ------
        - NotFoundError: The server was unable to find the session to be started
        - BadRequestError: The server was unable to start the session
        - ServerError: The server has encountered an uncategorized error condition
        """
        id = self.Id
        if self.parent.Platform == 'linux' and self._properties['state'].upper() != 'ACTIVE':
            # linux and windows offer async operation status on session start
            self._execute('start', payload={'applicationType': self.ApplicationType})
        elif self.parent.Platform == 'connection_manager' and 'IN USE' not in self._properties['subState']:
            # connection manager does not offer async operation status on session start
            self._execute('start', payload={'applicationType': self.ApplicationType})
            start = time.time()
            while True:
                response = self._connection._read('%s/%s/%s' % (self._parent.href, self._SDM_NAME, id))
                if response['state'] == 'ACTIVE' and 'IN USE' in response['subState']:
                    self._properties['state'] = response['state']
                    self._properties['subState'] = response['subState']
                    break
                elif time.time() - start > 300:
                    raise BadRequestError('Unable to start session %s after %s seconds' % (id, time.time() - start))
                time.sleep(5)
        return self

    def find(self, Id=None, Name=None):
        """Finds Sessions resources on the server and encapsulates the data in this instance.

        Args
        ----
        - Id (number): a valid session id
        - Name (str): a valid session name
        
        Returns
        -------
        - obj(testplatform.sessions.sessions.Session): a Sessions object with found resources

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
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
        if len(self) == 1 and self.parent.Platform == 'connection_manager':
            self.Start()
        return self

    def add(self, ApplicationType='ixnrest', Name=None):
        """Adds a new sessions resource on the server and encapsulates the data in this instance.
        Two types of sessions can be created, an ixnrest session or a quicktest web session.
        The quicktest web session can only be created when the TestPlatform.Platform type is 'linux'

        Args
        ----
        - ApplicationType (str[ixnrest|quicktest]): The type of session to be started
        - Name (str): The name of the session

        Returns
        -------
        - obj(testplatform.sessions.sessions.Session): a Sessions object

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
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
        self.Start()
        self.Name = Name
        return self

    def update(self, Name=None):
        """Updates the current encapsulated sessions resource on the server.

        Args
        ----
        - Name (str): The new name of the session. This is only supported when the platform is linux

        Returns
        -------
        - self: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self.Name = Name
        return self
        
    def remove(self):
        """Deletes all the encapsulated sessions resources from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        exceptions = ''
        for properties in self._object_properties:
            try:
                self._connection._execute('%s/operations/stop' % properties['href'], payload=None)
                self._connection._delete(properties['href'])
            except IxNetworkError as e:
                if e._status_code not in [400, 404, 405]:
                    exceptions += '%s\n' % e.message
        self._clear()
        if len(exceptions) > 0:
            raise exceptions
    
    def GetObjectFromHref(self, href):
        """Given an href get the corresponding object
        
        References are used to establish relationships between disparate nodes.
        This allows a user to get an object using a reference from a node.
        For example:
            A /vport node has a ConnectedTo property that is a reference to an /availableHardware/chassis/card/port node.
            A user can get a vport and use this method to get the port node in order to clear ownership
        
        Args
        ----
        - href (str): A valid href reference

        Returns
        -------
            obj: If the reference is valid an ixnetwork_restpy object or None if the reference cannot be resolved
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
                    if class_name == 'Multivalue':
                        return Multivalue(node, href)
                    else:
                        node = getattr(node, class_name)
                        if hasattr(node, 'find') is True:
                            node.find()
            return node
        except Exception as e:
            self.warn(e)
            return None

    def GetFileList(self, remote_directory=None):
        """Get a list of files from the IxNetwork session instance

        Args
        ----
        - remote_directory (str): A remote directory path

        Returns
        -------
        - dict(root_path, list(dict(filename, filesize)): A list of all the files for a given directory
        """
        href = '%s/ixnetwork/files' % self.href
        if remote_directory is not None:
            href = '%s?absolute=%s' % (href, remote_directory)
        return self._connection._read(href)

    def DownloadFile(self, remote_filename, local_filename=None):
        """Download a file from the IxNetwork session instance

        Args
        ----
        - remote_fileanme (str): the name of the remote file
        - local_filename (str): the name that the remote contents will be saved to
        
        Returns
        -------
        - str: the local file name
        """
        if self._parent.Platform == 'linux':
            remote_filename = remote_filename.replace('\\', '/')
        return self._connection._get_file('%s/ixnetwork' % self.href, 
            remote_filename=remote_filename, local_filename=local_filename)
    
    def UploadFile(self, local_filename, remote_filename=None):
        """Upload a file to the IxNetwork session instance

        Args
        ----
        - local_filename (str): the name of the local file
        - remote_filename (str): the name that will be used when saving the file on the IxNetwork sesson instance
        
        Returns
        -------
        - dict(filename, filesize): Details of the file that was uploaded
        """
        if self._parent.Platform == 'linux' and remote_filename is not None:
            remote_filename = remote_filename.replace('\\', '/')
        return self._connection._put_file('%s/ixnetwork' % self.href, 
            local_filename=local_filename, remote_filename=remote_filename)

    def RemoveFile(self, remote_filename):
        if self._parent.Platform == 'linux' and remote_filename is not None:
            remote_filename = remote_filename.replace('\\', '/')
        return self._connection._delete_file('%s/ixnetwork' % self.href, remote_filename=remote_filename)
