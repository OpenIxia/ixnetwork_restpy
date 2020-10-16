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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class AppErrors(Base):
    """This node holds application errors.
    The AppErrors class encapsulates a list of appErrors resources that are managed by the system.
    A list of resources can be retrieved from the server using the AppErrors.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'appErrors'
    _SDM_ATT_MAP = {
        'ErrorCount': 'errorCount',
        'LastModified': 'lastModified',
        'WarningCount': 'warningCount',
    }

    def __init__(self, parent):
        super(AppErrors, self).__init__(parent)

    @property
    def Error(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.error.Error): An instance of the Error class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.error import Error
        return Error(self)

    @property
    def ErrorCount(self):
        """
        Returns
        -------
        - number: Total number of errors
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCount'])

    @property
    def LastModified(self):
        """
        Returns
        -------
        - str: Time of latest logged error or warning
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastModified'])

    @property
    def WarningCount(self):
        """
        Returns
        -------
        - number: Total number of warnings
        """
        return self._get_attribute(self._SDM_ATT_MAP['WarningCount'])

    def find(self, ErrorCount=None, LastModified=None, WarningCount=None):
        """Finds and retrieves appErrors resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve appErrors resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all appErrors resources from the server.

        Args
        ----
        - ErrorCount (number): Total number of errors
        - LastModified (str): Time of latest logged error or warning
        - WarningCount (number): Total number of warnings

        Returns
        -------
        - self: This instance with matching appErrors resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of appErrors data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the appErrors resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
