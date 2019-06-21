# Copyright 1997 - 2018 by IXIA Keysight
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
            str
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

    def Start(self):
        """Starts the session

        Returns:
            None
        """
        if self._connection._platform != 'windows':
            response = self._execute('start', payload={'applicationType': self.ApplicationType})
            if response is not None:
                self._set_properties(response, clear=True)
    
    def find(self, Id=None):
        """Finds all child instances of Sessions on the server.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        responses = self._connection._read('%s/%s' % (self._parent.href, self._SDM_NAME))
        self._clear()
        for response in responses:
            if Id is not None:
                if str(response['id']) == str(Id):
                    self._set_properties(response)
            else:
                self._set_properties(response)
        return self

    def add(self):
        """Adds a new sessions node on the server and retrieves it in this instance.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        applicationType = 'ixnrest'
        self._create(locals())
        if self._connection._platform == 'linux':
            self.Start()
        return self

    def remove(self):
        """Deletes all the sessions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        try:
            self._execute('stop')
            self._delete()
        except IxNetworkError as e:
            if e._status_code not in [404, 405]:
                raise e
    
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