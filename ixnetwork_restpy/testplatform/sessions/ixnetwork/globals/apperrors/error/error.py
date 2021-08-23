# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
from ixnetwork_restpy.files import Files
from typing import List, Any, Union


class Error(Base):
    """This node is a specific application error instance
    The Error class encapsulates a list of error resources that are managed by the system.
    A list of resources can be retrieved from the server using the Error.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'error'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'ErrorCode': 'errorCode',
        'ErrorLevel': 'errorLevel',
        'InstanceCount': 'instanceCount',
        'LastModified': 'lastModified',
        'Name': 'name',
        'Provider': 'provider',
        'SourceColumns': 'sourceColumns',
        'SourceColumnsDisplayName': 'sourceColumnsDisplayName',
    }
    _SDM_ENUM_MAP = {
        'errorLevel': ['kAnalysis', 'kCount', 'kError', 'kMessage', 'kWarning'],
    }

    def __init__(self, parent, list_op=False):
        super(Error, self).__init__(parent, list_op)

    @property
    def Instance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.instance.instance.Instance): An instance of the Instance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.instance.instance import Instance
        if self._properties.get('Instance', None) is not None:
            return self._properties.get('Instance')
        else:
            return Instance(self)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The description of the error
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])

    @property
    def ErrorCode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The error code of the error
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorLevel(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kAnalysis | kCount | kError | kMessage | kWarning): The error level of the error
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorLevel'])

    @property
    def InstanceCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of instances of the error
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstanceCount'])

    @property
    def LastModified(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastModified'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the error
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def Provider(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The error provider of the error
        """
        return self._get_attribute(self._SDM_ATT_MAP['Provider'])

    @property
    def SourceColumns(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): If the error content originated from an xml meta file, these are the source column names if any for this error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceColumns'])

    @property
    def SourceColumnsDisplayName(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceColumnsDisplayName'])

    def add(self):
        """Adds a new error resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved error resources using find and the newly added error resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Description=None, ErrorCode=None, ErrorLevel=None, InstanceCount=None, LastModified=None, Name=None, Provider=None, SourceColumns=None, SourceColumnsDisplayName=None):
        # type: (str, int, str, int, str, str, str, List[str], List[str]) -> Error
        """Finds and retrieves error resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve error resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all error resources from the server.

        Args
        ----
        - Description (str): The description of the error
        - ErrorCode (number): The error code of the error
        - ErrorLevel (str(kAnalysis | kCount | kError | kMessage | kWarning)): The error level of the error
        - InstanceCount (number): The number of instances of the error
        - LastModified (str): 
        - Name (str): The name of the error
        - Provider (str): The error provider of the error
        - SourceColumns (list(str)): If the error content originated from an xml meta file, these are the source column names if any for this error.
        - SourceColumnsDisplayName (list(str)): 

        Returns
        -------
        - self: This instance with matching error resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of error data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the error resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
