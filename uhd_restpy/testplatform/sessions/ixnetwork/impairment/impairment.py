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


class Impairment(Base):
    """Allows the user to emulate WAN links with impairments such as packet delay and drop.
    The Impairment class encapsulates a required impairment resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'impairment'
    _SDM_ATT_MAP = {
        'Errors': 'errors',
        'State': 'state',
        'Warnings': 'warnings',
    }
    _SDM_ENUM_MAP = {
        'state': ['applyingChanges', 'changesPending', 'errorOccurred', 'ready'],
    }

    def __init__(self, parent, list_op=False):
        super(Impairment, self).__init__(parent, list_op)

    @property
    def DefaultProfile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.defaultprofile.DefaultProfile): An instance of the DefaultProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.defaultprofile import DefaultProfile
        if len(self._object_properties) > 0:
            if self._properties.get('DefaultProfile', None) is not None:
                return self._properties.get('DefaultProfile')
        return DefaultProfile(self)._select()

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.link.link.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.link.link import Link
        if len(self._object_properties) > 0:
            if self._properties.get('Link', None) is not None:
                return self._properties.get('Link')
        return Link(self)

    @property
    def Profile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.profile.profile.Profile): An instance of the Profile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.profile.profile import Profile
        if len(self._object_properties) > 0:
            if self._properties.get('Profile', None) is not None:
                return self._properties.get('Profile')
        return Profile(self)

    @property
    def Errors(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of errors which occurred while applying changes to the impairment configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str(applyingChanges | changesPending | errorOccurred | ready): Indicates whether changes are being applied to the impairment configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def Warnings(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of warnings which occurred while applying changes to the impairment configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Warnings'])

    def find(self, Errors=None, State=None, Warnings=None):
        # type: (List[str], str, List[str]) -> Impairment
        """Finds and retrieves impairment resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve impairment resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all impairment resources from the server.

        Args
        ----
        - Errors (list(str)): List of errors which occurred while applying changes to the impairment configuration.
        - State (str(applyingChanges | changesPending | errorOccurred | ready)): Indicates whether changes are being applied to the impairment configuration.
        - Warnings (list(str)): List of warnings which occurred while applying changes to the impairment configuration.

        Returns
        -------
        - self: This instance with matching impairment resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of impairment data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the impairment resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies traffic impairments defined by user.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('apply', payload=payload, response_object=None)
