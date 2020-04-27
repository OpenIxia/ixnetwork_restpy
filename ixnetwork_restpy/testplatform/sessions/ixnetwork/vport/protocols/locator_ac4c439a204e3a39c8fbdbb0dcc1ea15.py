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


class Locator(Base):
    """It gives details about the locator
    The Locator class encapsulates a list of locator resources that are managed by the user.
    A list of resources can be retrieved from the server using the Locator.find() method.
    The list can be managed by using the Locator.add() and Locator.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'locator'

    def __init__(self, parent):
        super(Locator, self).__init__(parent)

    @property
    def Address(self):
        """
        Returns
        -------
        - str: It gives details about the Ip
        """
        return self._get_attribute('address')
    @Address.setter
    def Address(self, value):
        self._set_attribute('address', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: It True, it enables the protocol
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Family(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): It gives details about the family
        """
        return self._get_attribute('family')
    @Family.setter
    def Family(self, value):
        self._set_attribute('family', value)

    @property
    def LispInterfaceId(self):
        """
        Returns
        -------
        - number: It gives details about the LISP interface id
        """
        return self._get_attribute('lispInterfaceId')
    @LispInterfaceId.setter
    def LispInterfaceId(self, value):
        self._set_attribute('lispInterfaceId', value)

    @property
    def LocalLocator(self):
        """
        Returns
        -------
        - bool: If True, It gives the address of the local locator
        """
        return self._get_attribute('localLocator')
    @LocalLocator.setter
    def LocalLocator(self, value):
        self._set_attribute('localLocator', value)

    @property
    def MPriority(self):
        """
        Returns
        -------
        - number: It denotes the m priority
        """
        return self._get_attribute('mPriority')
    @MPriority.setter
    def MPriority(self, value):
        self._set_attribute('mPriority', value)

    @property
    def MWeight(self):
        """
        Returns
        -------
        - number: It denotes the m weight
        """
        return self._get_attribute('mWeight')
    @MWeight.setter
    def MWeight(self, value):
        self._set_attribute('mWeight', value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: It gives the priority
        """
        return self._get_attribute('priority')
    @Priority.setter
    def Priority(self, value):
        self._set_attribute('priority', value)

    @property
    def ProtocolInterfaceIpItemId(self):
        """
        Returns
        -------
        - number: It gives details about the protocol interface ip item id
        """
        return self._get_attribute('protocolInterfaceIpItemId')
    @ProtocolInterfaceIpItemId.setter
    def ProtocolInterfaceIpItemId(self, value):
        self._set_attribute('protocolInterfaceIpItemId', value)

    @property
    def Reachability(self):
        """
        Returns
        -------
        - bool: If true, it defines the reachability
        """
        return self._get_attribute('reachability')
    @Reachability.setter
    def Reachability(self, value):
        self._set_attribute('reachability', value)

    @property
    def Weight(self):
        """
        Returns
        -------
        - number: It gives details about the weight
        """
        return self._get_attribute('weight')
    @Weight.setter
    def Weight(self, value):
        self._set_attribute('weight', value)

    def update(self, Address=None, Enabled=None, Family=None, LispInterfaceId=None, LocalLocator=None, MPriority=None, MWeight=None, Priority=None, ProtocolInterfaceIpItemId=None, Reachability=None, Weight=None):
        """Updates locator resource on the server.

        Args
        ----
        - Address (str): It gives details about the Ip
        - Enabled (bool): It True, it enables the protocol
        - Family (str(ipv4 | ipv6)): It gives details about the family
        - LispInterfaceId (number): It gives details about the LISP interface id
        - LocalLocator (bool): If True, It gives the address of the local locator
        - MPriority (number): It denotes the m priority
        - MWeight (number): It denotes the m weight
        - Priority (number): It gives the priority
        - ProtocolInterfaceIpItemId (number): It gives details about the protocol interface ip item id
        - Reachability (bool): If true, it defines the reachability
        - Weight (number): It gives details about the weight

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, Address=None, Enabled=None, Family=None, LispInterfaceId=None, LocalLocator=None, MPriority=None, MWeight=None, Priority=None, ProtocolInterfaceIpItemId=None, Reachability=None, Weight=None):
        """Adds a new locator resource on the server and adds it to the container.

        Args
        ----
        - Address (str): It gives details about the Ip
        - Enabled (bool): It True, it enables the protocol
        - Family (str(ipv4 | ipv6)): It gives details about the family
        - LispInterfaceId (number): It gives details about the LISP interface id
        - LocalLocator (bool): If True, It gives the address of the local locator
        - MPriority (number): It denotes the m priority
        - MWeight (number): It denotes the m weight
        - Priority (number): It gives the priority
        - ProtocolInterfaceIpItemId (number): It gives details about the protocol interface ip item id
        - Reachability (bool): If true, it defines the reachability
        - Weight (number): It gives details about the weight

        Returns
        -------
        - self: This instance with all currently retrieved locator resources using find and the newly added locator resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained locator resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Address=None, Enabled=None, Family=None, LispInterfaceId=None, LocalLocator=None, MPriority=None, MWeight=None, Priority=None, ProtocolInterfaceIpItemId=None, Reachability=None, Weight=None):
        """Finds and retrieves locator resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve locator resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all locator resources from the server.

        Args
        ----
        - Address (str): It gives details about the Ip
        - Enabled (bool): It True, it enables the protocol
        - Family (str(ipv4 | ipv6)): It gives details about the family
        - LispInterfaceId (number): It gives details about the LISP interface id
        - LocalLocator (bool): If True, It gives the address of the local locator
        - MPriority (number): It denotes the m priority
        - MWeight (number): It denotes the m weight
        - Priority (number): It gives the priority
        - ProtocolInterfaceIpItemId (number): It gives details about the protocol interface ip item id
        - Reachability (bool): If true, it defines the reachability
        - Weight (number): It gives details about the weight

        Returns
        -------
        - self: This instance with matching locator resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of locator data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the locator resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
