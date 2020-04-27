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


class Interface(Base):
    """This object holds the information for a single interface on the mplsTp router.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def LspPwRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lsppwrange_ca73b78dcf729adb366c26fdc1b10cea.LspPwRange): An instance of the LspPwRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lsppwrange_ca73b78dcf729adb366c26fdc1b10cea import LspPwRange
        return LspPwRange(self)

    @property
    def DutMacAddress(self):
        """
        Returns
        -------
        - str: This signifies the MAC address of the DUT.
        """
        return self._get_attribute('dutMacAddress')
    @DutMacAddress.setter
    def DutMacAddress(self, value):
        self._set_attribute('dutMacAddress', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: This signifies the enablement of the use of this interface for the simulated router.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): This signifies the Interface that has been assigned for this range.
        """
        return self._get_attribute('interfaces')
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute('interfaces', value)

    def update(self, DutMacAddress=None, Enabled=None, Interfaces=None):
        """Updates interface resource on the server.

        Args
        ----
        - DutMacAddress (str): This signifies the MAC address of the DUT.
        - Enabled (bool): This signifies the enablement of the use of this interface for the simulated router.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This signifies the Interface that has been assigned for this range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, DutMacAddress=None, Enabled=None, Interfaces=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - DutMacAddress (str): This signifies the MAC address of the DUT.
        - Enabled (bool): This signifies the enablement of the use of this interface for the simulated router.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This signifies the Interface that has been assigned for this range.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DutMacAddress=None, Enabled=None, Interfaces=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - DutMacAddress (str): This signifies the MAC address of the DUT.
        - Enabled (bool): This signifies the enablement of the use of this interface for the simulated router.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This signifies the Interface that has been assigned for this range.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
