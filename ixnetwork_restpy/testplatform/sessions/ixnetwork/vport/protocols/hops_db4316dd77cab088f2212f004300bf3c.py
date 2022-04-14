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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Hops(Base):
    """This signifies the number of hops.
    The Hops class encapsulates a list of hops resources that are managed by the system.
    A list of resources can be retrieved from the server using the Hops.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "hops"
    _SDM_ATT_MAP = {
        "DownStreamAddressInfo": "downStreamAddressInfo",
        "DownStreamLabelsInfo": "downStreamLabelsInfo",
        "DownStreamMultiPathInfo": "downStreamMultiPathInfo",
        "DownStreamReturnCode": "downStreamReturnCode",
        "DownStreamReturnSubCode": "downStreamReturnSubCode",
        "ErrorTlvType": "errorTlvType",
        "InterfaceLabelStackTlvInterface": "interfaceLabelStackTlvInterface",
        "InterfaceLabelStackTlvIpAddress": "interfaceLabelStackTlvIpAddress",
        "InterfaceLabelStackTlvLabels": "interfaceLabelStackTlvLabels",
        "ReturnCode": "returnCode",
        "ReturnSubcode": "returnSubcode",
        "SrcIp": "srcIp",
        "Ttl": "ttl",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Hops, self).__init__(parent, list_op)

    @property
    def DownStreamAddressInfo(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the downstream Address information received in traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownStreamAddressInfo"])

    @property
    def DownStreamLabelsInfo(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the downstream label stack received in traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownStreamLabelsInfo"])

    @property
    def DownStreamMultiPathInfo(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the downstream Multipath information received in traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownStreamMultiPathInfo"])

    @property
    def DownStreamReturnCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the downstream return code received in traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownStreamReturnCode"])

    @property
    def DownStreamReturnSubCode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the downstream return sub code received in traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownStreamReturnSubCode"])

    @property
    def ErrorTlvType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Error TLV in received traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorTlvType"])

    @property
    def InterfaceLabelStackTlvInterface(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the inclusion of the Interface Id within Interface and Label Stack TLV in received traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceLabelStackTlvInterface"])

    @property
    def InterfaceLabelStackTlvIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the inclusion of the IP Address within Interface and Label Stack TLV in received traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceLabelStackTlvIpAddress"])

    @property
    def InterfaceLabelStackTlvLabels(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the inclusion of the Label stack in Interface and Label Stack TLV in received traceroute echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceLabelStackTlvLabels"])

    @property
    def ReturnCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the return code in MPLS echo reply sent by traceroute hop.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReturnCode"])

    @property
    def ReturnSubcode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the return subcode in MPLS echo reply sent by traceroute hop.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReturnSubcode"])

    @property
    def SrcIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the source IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcIp"])

    @property
    def Ttl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the MPLS Time To Live value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ttl"])

    def add(self):
        """Adds a new hops resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved hops resources using find and the newly added hops resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DownStreamAddressInfo=None,
        DownStreamLabelsInfo=None,
        DownStreamMultiPathInfo=None,
        DownStreamReturnCode=None,
        DownStreamReturnSubCode=None,
        ErrorTlvType=None,
        InterfaceLabelStackTlvInterface=None,
        InterfaceLabelStackTlvIpAddress=None,
        InterfaceLabelStackTlvLabels=None,
        ReturnCode=None,
        ReturnSubcode=None,
        SrcIp=None,
        Ttl=None,
    ):
        # type: (str, str, str, str, int, int, int, str, str, str, int, str, int) -> Hops
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
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

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
