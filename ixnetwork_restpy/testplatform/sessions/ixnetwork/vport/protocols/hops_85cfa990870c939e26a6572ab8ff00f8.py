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


class Hops(Base):
    """This signifies the number of hops.
    The Hops class encapsulates a list of hops resources that are managed by the system.
    A list of resources can be retrieved from the server using the Hops.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'hops'

    def __init__(self, parent):
        super(Hops, self).__init__(parent)

    @property
    def DownStreamAddressInfo(self):
        """
        Returns
        -------
        - str: This signifies the downstream Address information received in traceroute echo reply message.
        """
        return self._get_attribute('downStreamAddressInfo')

    @property
    def DownStreamLabelsInfo(self):
        """
        Returns
        -------
        - str: This signifies the downstream label stack received in traceroute echo reply message.
        """
        return self._get_attribute('downStreamLabelsInfo')

    @property
    def DownStreamMultiPathInfo(self):
        """
        Returns
        -------
        - str: This signifies the downstream Multipath information received in traceroute echo reply message.
        """
        return self._get_attribute('downStreamMultiPathInfo')

    @property
    def DownStreamReturnCode(self):
        """
        Returns
        -------
        - str: This signifies the downstream return code received in traceroute echo reply message.
        """
        return self._get_attribute('downStreamReturnCode')

    @property
    def DownStreamReturnSubCode(self):
        """
        Returns
        -------
        - number: This signifies the downstream return sub code received in traceroute echo reply message.
        """
        return self._get_attribute('downStreamReturnSubCode')

    @property
    def ErrorTlvType(self):
        """
        Returns
        -------
        - number: This signifies the Error TLV in received traceroute echo reply message.
        """
        return self._get_attribute('errorTlvType')

    @property
    def InterfaceLabelStackTlvInterface(self):
        """
        Returns
        -------
        - number: This signifies the inclusion of the Interface Id within Interface and Label Stack TLV in received traceroute echo reply message.
        """
        return self._get_attribute('interfaceLabelStackTlvInterface')

    @property
    def InterfaceLabelStackTlvIpAddress(self):
        """
        Returns
        -------
        - str: This signifies the inclusion of the IP Address within Interface and Label Stack TLV in received traceroute echo reply message.
        """
        return self._get_attribute('interfaceLabelStackTlvIpAddress')

    @property
    def InterfaceLabelStackTlvLabels(self):
        """
        Returns
        -------
        - str: This signifies the inclusion of the Label stack in Interface and Label Stack TLV in received traceroute echo reply message.
        """
        return self._get_attribute('interfaceLabelStackTlvLabels')

    @property
    def ReturnCode(self):
        """
        Returns
        -------
        - str: This signifies the return code in MPLS echo reply sent by traceroute hop.
        """
        return self._get_attribute('returnCode')

    @property
    def ReturnSubcode(self):
        """
        Returns
        -------
        - number: This signifies the return subcode in MPLS echo reply sent by traceroute hop.
        """
        return self._get_attribute('returnSubcode')

    @property
    def SrcIp(self):
        """
        Returns
        -------
        - str: This signifies the source IP address.
        """
        return self._get_attribute('srcIp')

    @property
    def Ttl(self):
        """
        Returns
        -------
        - number: This signifies the MPLS Time To Live value.
        """
        return self._get_attribute('ttl')

    def find(self, DownStreamAddressInfo=None, DownStreamLabelsInfo=None, DownStreamMultiPathInfo=None, DownStreamReturnCode=None, DownStreamReturnSubCode=None, ErrorTlvType=None, InterfaceLabelStackTlvInterface=None, InterfaceLabelStackTlvIpAddress=None, InterfaceLabelStackTlvLabels=None, ReturnCode=None, ReturnSubcode=None, SrcIp=None, Ttl=None):
        """Finds and retrieves hops resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve hops resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all hops resources from the server.

        Args
        ----
        - DownStreamAddressInfo (str): This signifies the downstream Address information received in traceroute echo reply message.
        - DownStreamLabelsInfo (str): This signifies the downstream label stack received in traceroute echo reply message.
        - DownStreamMultiPathInfo (str): This signifies the downstream Multipath information received in traceroute echo reply message.
        - DownStreamReturnCode (str): This signifies the downstream return code received in traceroute echo reply message.
        - DownStreamReturnSubCode (number): This signifies the downstream return sub code received in traceroute echo reply message.
        - ErrorTlvType (number): This signifies the Error TLV in received traceroute echo reply message.
        - InterfaceLabelStackTlvInterface (number): This signifies the inclusion of the Interface Id within Interface and Label Stack TLV in received traceroute echo reply message.
        - InterfaceLabelStackTlvIpAddress (str): This signifies the inclusion of the IP Address within Interface and Label Stack TLV in received traceroute echo reply message.
        - InterfaceLabelStackTlvLabels (str): This signifies the inclusion of the Label stack in Interface and Label Stack TLV in received traceroute echo reply message.
        - ReturnCode (str): This signifies the return code in MPLS echo reply sent by traceroute hop.
        - ReturnSubcode (number): This signifies the return subcode in MPLS echo reply sent by traceroute hop.
        - SrcIp (str): This signifies the source IP address.
        - Ttl (number): This signifies the MPLS Time To Live value.

        Returns
        -------
        - self: This instance with matching hops resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of hops data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the hops resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
