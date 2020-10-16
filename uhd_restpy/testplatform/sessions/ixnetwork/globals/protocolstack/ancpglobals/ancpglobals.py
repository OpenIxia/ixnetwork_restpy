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


class AncpGlobals(Base):
    """Global settings placeholder for AncpPlugin.
    The AncpGlobals class encapsulates a list of ancpGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the AncpGlobals.find() method.
    The list can be managed by using the AncpGlobals.add() and AncpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ancpGlobals'
    _SDM_ATT_MAP = {
        'ObjectId': 'objectId',
        'PortDownRate': 'portDownRate',
        'PortUpRate': 'portUpRate',
        'ResyncRate': 'resyncRate',
    }

    def __init__(self, parent):
        super(AncpGlobals, self).__init__(parent)

    @property
    def AncpDslProfile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslprofile.ancpdslprofile.AncpDslProfile): An instance of the AncpDslProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslprofile.ancpdslprofile import AncpDslProfile
        return AncpDslProfile(self)

    @property
    def AncpDslResyncProfile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslresyncprofile.ancpdslresyncprofile.AncpDslResyncProfile): An instance of the AncpDslResyncProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslresyncprofile.ancpdslresyncprofile import AncpDslResyncProfile
        return AncpDslResyncProfile(self)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def PortDownRate(self):
        """
        Returns
        -------
        - number: The number of Port Down event messages to send each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDownRate'])
    @PortDownRate.setter
    def PortDownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDownRate'], value)

    @property
    def PortUpRate(self):
        """
        Returns
        -------
        - number: The number of Port Up event messages to send each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortUpRate'])
    @PortUpRate.setter
    def PortUpRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortUpRate'], value)

    @property
    def ResyncRate(self):
        """
        Returns
        -------
        - number: The number of Port Up event messages to send each second, to simulate DSL Resync events.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResyncRate'])
    @ResyncRate.setter
    def ResyncRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResyncRate'], value)

    def update(self, PortDownRate=None, PortUpRate=None, ResyncRate=None):
        """Updates ancpGlobals resource on the server.

        Args
        ----
        - PortDownRate (number): The number of Port Down event messages to send each second.
        - PortUpRate (number): The number of Port Up event messages to send each second.
        - ResyncRate (number): The number of Port Up event messages to send each second, to simulate DSL Resync events.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, PortDownRate=None, PortUpRate=None, ResyncRate=None):
        """Adds a new ancpGlobals resource on the server and adds it to the container.

        Args
        ----
        - PortDownRate (number): The number of Port Down event messages to send each second.
        - PortUpRate (number): The number of Port Up event messages to send each second.
        - ResyncRate (number): The number of Port Up event messages to send each second, to simulate DSL Resync events.

        Returns
        -------
        - self: This instance with all currently retrieved ancpGlobals resources using find and the newly added ancpGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ancpGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ObjectId=None, PortDownRate=None, PortUpRate=None, ResyncRate=None):
        """Finds and retrieves ancpGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ancpGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ancpGlobals resources from the server.

        Args
        ----
        - ObjectId (str): Unique identifier for this object
        - PortDownRate (number): The number of Port Down event messages to send each second.
        - PortUpRate (number): The number of Port Up event messages to send each second.
        - ResyncRate (number): The number of Port Up event messages to send each second, to simulate DSL Resync events.

        Returns
        -------
        - self: This instance with matching ancpGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ancpGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ancpGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
