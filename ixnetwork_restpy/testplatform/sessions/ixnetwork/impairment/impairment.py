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

    def __init__(self, parent):
        super(Impairment, self).__init__(parent)

    @property
    def DefaultProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.defaultprofile.DefaultProfile): An instance of the DefaultProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.defaultprofile import DefaultProfile
        return DefaultProfile(self)._select()

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.link.link.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.link.link import Link
        return Link(self)

    @property
    def Profile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.profile.Profile): An instance of the Profile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.profile import Profile
        return Profile(self)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(str): List of errors which occurred while applying changes to the impairment configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def State(self):
        """
        Returns
        -------
        - str(applyingChanges | changesPending | errorOccurred | ready): Indicates whether changes are being applied to the impairment configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def Warnings(self):
        """
        Returns
        -------
        - list(str): List of warnings which occurred while applying changes to the impairment configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Warnings'])

    def Apply(self):
        """Executes the apply operation on the server.

        Applies traffic impairments defined by user.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)
