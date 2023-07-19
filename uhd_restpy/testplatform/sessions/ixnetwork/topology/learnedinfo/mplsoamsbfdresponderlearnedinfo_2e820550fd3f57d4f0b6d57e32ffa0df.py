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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class MplsoamSbfdResponderLearnedInfo(Base):
    """GUI columns and TCL attributes for SBFD Responder Learned Information
    The MplsoamSbfdResponderLearnedInfo class encapsulates a list of mplsoamSbfdResponderLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the MplsoamSbfdResponderLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'mplsoamSbfdResponderLearnedInfo'
    _SDM_ATT_MAP = {
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(MplsoamSbfdResponderLearnedInfo, self).__init__(parent, list_op)

    def add(self):
        """Adds a new mplsoamSbfdResponderLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved mplsoamSbfdResponderLearnedInfo resources using find and the newly added mplsoamSbfdResponderLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self):
        """Finds and retrieves mplsoamSbfdResponderLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mplsoamSbfdResponderLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mplsoamSbfdResponderLearnedInfo resources from the server.

        Returns
        -------
        - self: This instance with matching mplsoamSbfdResponderLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mplsoamSbfdResponderLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mplsoamSbfdResponderLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def PauseSessions(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the pauseSessions operation on the server.

        Pause selected learned SBFD sessions at Responder e.g. to allow data to switch to backup path at the ingress.Only applicable for sessions not already in Paused state.

        pauseSessions(Arg2=list, async_operation=bool)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices of the learned sessions from SBFD Initiator which has to be paused.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('pauseSessions', payload=payload, response_object=None)

    def ResumeSessions(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumeSessions operation on the server.

        Resume selected learned SBFD sessions at Responder e.g. to allow data to switch to primary path at the ingress.Only applicable for sessions in Paused state.

        resumeSessions(Arg2=list, async_operation=bool)list
        ---------------------------------------------------
        - Arg2 (list(number)): List of indices of the learned sessions from SBFD Initiator which has to be resumed.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumeSessions', payload=payload, response_object=None)
