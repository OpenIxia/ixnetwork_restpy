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


class OAM(Base):
    """The Layer 1 Configuration is being configured for an Ethernet port and OAM is selected as the Payload Type.
    The OAM class encapsulates a required OAM resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "OAM"
    _SDM_ATT_MAP = {
        "EnableTlvOption": "enableTlvOption",
        "Enabled": "enabled",
        "IdleTimer": "idleTimer",
        "LinkEvents": "linkEvents",
        "Loopback": "loopback",
        "MacAddress": "macAddress",
        "MaxOAMPDUSize": "maxOAMPDUSize",
        "OrganizationUniqueIdentifier": "organizationUniqueIdentifier",
        "TlvType": "tlvType",
        "TlvValue": "tlvValue",
        "VendorSpecificInformation": "vendorSpecificInformation",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OAM, self).__init__(parent, list_op)

    @property
    def EnableTlvOption(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the tlv option.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTlvOption"])

    @EnableTlvOption.setter
    def EnableTlvOption(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTlvOption"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables OAM for the Ten Gig Lan port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IdleTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The timer used to ensure OAM sub layer adheres to maximum number of OAMPDUs per second and emits at least one OAMPDU per second. The default is 1, minimum value is 1 and maximum value is 10.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdleTimer"])

    @IdleTimer.setter
    def IdleTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IdleTimer"], value)

    @property
    def LinkEvents(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables link event interpreting support in Ixia port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkEvents"])

    @LinkEvents.setter
    def LinkEvents(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkEvents"], value)

    @property
    def Loopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the loopback. when an ixia port goes to loopback mode, then all non oam packets coming to that port gets looped back.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Loopback"])

    @Loopback.setter
    def Loopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Loopback"], value)

    @property
    def MacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Mac address of the local DTE. By default, the mac address is automatically generated from card, port and other related information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacAddress"])

    @MacAddress.setter
    def MacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacAddress"], value)

    @property
    def MaxOAMPDUSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the maximum OAMPDU size supported by local DTE. The default is 1500, minimum is 64, and maximum is 1500 in octets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxOAMPDUSize"])

    @MaxOAMPDUSize.setter
    def MaxOAMPDUSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxOAMPDUSize"], value)

    @property
    def OrganizationUniqueIdentifier(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This three-octet field contains a 24-bit Organizationally Unique Identifier. The default value is 00-01-00. Any three octets hex value can be given.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OrganizationUniqueIdentifier"])

    @OrganizationUniqueIdentifier.setter
    def OrganizationUniqueIdentifier(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OrganizationUniqueIdentifier"], value)

    @property
    def TlvType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the tlv type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TlvType"])

    @TlvType.setter
    def TlvType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TlvType"], value)

    @property
    def TlvValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Enters the tlv value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TlvValue"])

    @TlvValue.setter
    def TlvValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TlvValue"], value)

    @property
    def VendorSpecificInformation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Contains the vendor specific information that is used to differentiate a vendor's product modes/version. Default is 00000000.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorSpecificInformation"])

    @VendorSpecificInformation.setter
    def VendorSpecificInformation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorSpecificInformation"], value)

    def update(
        self,
        EnableTlvOption=None,
        Enabled=None,
        IdleTimer=None,
        LinkEvents=None,
        Loopback=None,
        MacAddress=None,
        MaxOAMPDUSize=None,
        OrganizationUniqueIdentifier=None,
        TlvType=None,
        TlvValue=None,
        VendorSpecificInformation=None,
    ):
        # type: (bool, bool, int, bool, bool, str, int, str, str, str, str) -> OAM
        """Updates OAM resource on the server.

        Args
        ----
        - EnableTlvOption (bool): If true, enables the tlv option.
        - Enabled (bool): If true, enables OAM for the Ten Gig Lan port.
        - IdleTimer (number): The timer used to ensure OAM sub layer adheres to maximum number of OAMPDUs per second and emits at least one OAMPDU per second. The default is 1, minimum value is 1 and maximum value is 10.
        - LinkEvents (bool): If true, enables link event interpreting support in Ixia port.
        - Loopback (bool): If true, enables the loopback. when an ixia port goes to loopback mode, then all non oam packets coming to that port gets looped back.
        - MacAddress (str): Mac address of the local DTE. By default, the mac address is automatically generated from card, port and other related information.
        - MaxOAMPDUSize (number): Indicates the maximum OAMPDU size supported by local DTE. The default is 1500, minimum is 64, and maximum is 1500 in octets.
        - OrganizationUniqueIdentifier (str): This three-octet field contains a 24-bit Organizationally Unique Identifier. The default value is 00-01-00. Any three octets hex value can be given.
        - TlvType (str): Indicates the tlv type.
        - TlvValue (str): Enters the tlv value.
        - VendorSpecificInformation (str): Contains the vendor specific information that is used to differentiate a vendor's product modes/version. Default is 00000000.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableTlvOption=None,
        Enabled=None,
        IdleTimer=None,
        LinkEvents=None,
        Loopback=None,
        MacAddress=None,
        MaxOAMPDUSize=None,
        OrganizationUniqueIdentifier=None,
        TlvType=None,
        TlvValue=None,
        VendorSpecificInformation=None,
    ):
        # type: (bool, bool, int, bool, bool, str, int, str, str, str, str) -> OAM
        """Finds and retrieves OAM resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve OAM resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all OAM resources from the server.

        Args
        ----
        - EnableTlvOption (bool): If true, enables the tlv option.
        - Enabled (bool): If true, enables OAM for the Ten Gig Lan port.
        - IdleTimer (number): The timer used to ensure OAM sub layer adheres to maximum number of OAMPDUs per second and emits at least one OAMPDU per second. The default is 1, minimum value is 1 and maximum value is 10.
        - LinkEvents (bool): If true, enables link event interpreting support in Ixia port.
        - Loopback (bool): If true, enables the loopback. when an ixia port goes to loopback mode, then all non oam packets coming to that port gets looped back.
        - MacAddress (str): Mac address of the local DTE. By default, the mac address is automatically generated from card, port and other related information.
        - MaxOAMPDUSize (number): Indicates the maximum OAMPDU size supported by local DTE. The default is 1500, minimum is 64, and maximum is 1500 in octets.
        - OrganizationUniqueIdentifier (str): This three-octet field contains a 24-bit Organizationally Unique Identifier. The default value is 00-01-00. Any three octets hex value can be given.
        - TlvType (str): Indicates the tlv type.
        - TlvValue (str): Enters the tlv value.
        - VendorSpecificInformation (str): Contains the vendor specific information that is used to differentiate a vendor's product modes/version. Default is 00000000.

        Returns
        -------
        - self: This instance with matching OAM resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of OAM data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the OAM resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
