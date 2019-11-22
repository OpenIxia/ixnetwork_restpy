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


class Ipv4Multicast(Base):
    """The DCE ISIS Learned Information option fetches the learned information for the IPv4 Multicast Range of a particular DCE ISIS router.
    The Ipv4Multicast class encapsulates a list of ipv4Multicast resources that is managed by the system.
    A list of resources can be retrieved from the server using the Ipv4Multicast.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4Multicast'

    def __init__(self, parent):
        super(Ipv4Multicast, self).__init__(parent)

    @property
    def Ipv4UnicastItem(self):
        """An instance of the Ipv4UnicastItem class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicastitem_c8e7b959a27a780e381e1fb4ae39f99e.Ipv4UnicastItem)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicastitem_c8e7b959a27a780e381e1fb4ae39f99e import Ipv4UnicastItem
        return Ipv4UnicastItem(self)

    @property
    def Age(self):
        """This indicates the age in time, in seconds, since it was last refreshed.

        Returns:
            number
        """
        return self._get_attribute('age')

    @property
    def HostName(self):
        """The host name as retrieved from the related packets.

        Returns:
            str
        """
        return self._get_attribute('hostName')

    @property
    def Ipv4MulticastGroupAddress(self):
        """This indicates the IPv4 Multicast Group Address in the Group Record.

        Returns:
            str
        """
        return self._get_attribute('ipv4MulticastGroupAddress')

    @property
    def LspId(self):
        """This indicates the LSP identification number.

        Returns:
            str
        """
        return self._get_attribute('lspId')

    @property
    def SequenceNumber(self):
        """This indicates the sequence number of the LSP containing the route.

        Returns:
            number
        """
        return self._get_attribute('sequenceNumber')

    @property
    def VlanId(self):
        """This indicates the VLAN ID in the Group Record.

        Returns:
            number
        """
        return self._get_attribute('vlanId')

    def find(self, Age=None, HostName=None, Ipv4MulticastGroupAddress=None, LspId=None, SequenceNumber=None, VlanId=None):
        """Finds and retrieves ipv4Multicast data from the server.

        All named parameters support regex and can be used to selectively retrieve ipv4Multicast data from the server.
        By default the find method takes no parameters and will retrieve all ipv4Multicast data from the server.

        Args:
            Age (number): This indicates the age in time, in seconds, since it was last refreshed.
            HostName (str): The host name as retrieved from the related packets.
            Ipv4MulticastGroupAddress (str): This indicates the IPv4 Multicast Group Address in the Group Record.
            LspId (str): This indicates the LSP identification number.
            SequenceNumber (number): This indicates the sequence number of the LSP containing the route.
            VlanId (number): This indicates the VLAN ID in the Group Record.

        Returns:
            self: This instance with matching ipv4Multicast data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ipv4Multicast data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ipv4Multicast data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
