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
from ixnetwork_restpy.files import Files


class AncpGlobals(Base):
    """Global settings placeholder for AncpPlugin.
    The AncpGlobals class encapsulates a list of ancpGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the AncpGlobals.find() method.
    The list can be managed by the user by using the AncpGlobals.add() and AncpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ancpGlobals'

    def __init__(self, parent):
        super(AncpGlobals, self).__init__(parent)

    @property
    def AncpDslProfile(self):
        """An instance of the AncpDslProfile class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslprofile.ancpdslprofile.AncpDslProfile)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslprofile.ancpdslprofile import AncpDslProfile
        return AncpDslProfile(self)

    @property
    def AncpDslResyncProfile(self):
        """An instance of the AncpDslResyncProfile class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslresyncprofile.ancpdslresyncprofile.AncpDslResyncProfile)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpdslresyncprofile.ancpdslresyncprofile import AncpDslResyncProfile
        return AncpDslResyncProfile(self)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PortDownRate(self):
        """The number of Port Down event messages to send each second.

        Returns:
            number
        """
        return self._get_attribute('portDownRate')
    @PortDownRate.setter
    def PortDownRate(self, value):
        self._set_attribute('portDownRate', value)

    @property
    def PortUpRate(self):
        """The number of Port Up event messages to send each second.

        Returns:
            number
        """
        return self._get_attribute('portUpRate')
    @PortUpRate.setter
    def PortUpRate(self, value):
        self._set_attribute('portUpRate', value)

    @property
    def ResyncRate(self):
        """The number of Port Up event messages to send each second, to simulate DSL Resync events.

        Returns:
            number
        """
        return self._get_attribute('resyncRate')
    @ResyncRate.setter
    def ResyncRate(self, value):
        self._set_attribute('resyncRate', value)

    def update(self, PortDownRate=None, PortUpRate=None, ResyncRate=None):
        """Updates a child instance of ancpGlobals on the server.

        Args:
            PortDownRate (number): The number of Port Down event messages to send each second.
            PortUpRate (number): The number of Port Up event messages to send each second.
            ResyncRate (number): The number of Port Up event messages to send each second, to simulate DSL Resync events.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, PortDownRate=None, PortUpRate=None, ResyncRate=None):
        """Adds a new ancpGlobals node on the server and retrieves it in this instance.

        Args:
            PortDownRate (number): The number of Port Down event messages to send each second.
            PortUpRate (number): The number of Port Up event messages to send each second.
            ResyncRate (number): The number of Port Up event messages to send each second, to simulate DSL Resync events.

        Returns:
            self: This instance with all currently retrieved ancpGlobals data using find and the newly added ancpGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the ancpGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ObjectId=None, PortDownRate=None, PortUpRate=None, ResyncRate=None):
        """Finds and retrieves ancpGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve ancpGlobals data from the server.
        By default the find method takes no parameters and will retrieve all ancpGlobals data from the server.

        Args:
            ObjectId (str): Unique identifier for this object
            PortDownRate (number): The number of Port Down event messages to send each second.
            PortUpRate (number): The number of Port Up event messages to send each second.
            ResyncRate (number): The number of Port Up event messages to send each second, to simulate DSL Resync events.

        Returns:
            self: This instance with matching ancpGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ancpGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ancpGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
