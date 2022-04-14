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


class RouteDistinguisher(Base):
    """This object controls route distinguisher configuration.
    The RouteDistinguisher class encapsulates a required routeDistinguisher resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "routeDistinguisher"
    _SDM_ATT_MAP = {
        "AsNumber": "asNumber",
        "AsNumberStep": "asNumberStep",
        "AssignedNumber": "assignedNumber",
        "AssignedNumberStep": "assignedNumberStep",
        "IpAddress": "ipAddress",
        "IpAddressStep": "ipAddressStep",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {
        "type": ["as", "ip", "asNumber2"],
    }

    def __init__(self, parent, list_op=False):
        super(RouteDistinguisher, self).__init__(parent, list_op)

    @property
    def AsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If the type was set to as or asNumber2, this is the AS number in the Administrator subfield of the Value field of the MVPN Route Distinguisher (RD). It is the Global part of the RD. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsNumber"])

    @AsNumber.setter
    def AsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsNumber"], value)

    @property
    def AsNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step for for the AS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsNumberStep"])

    @AsNumberStep.setter
    def AsNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsNumberStep"], value)

    @property
    def AssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Assigned Number sub-field of the Value field of the MVPN Route Distinguisher. It is a number from a numbering space, which the enterprise administers, for a given IP address or ASN space. It is the Local part of the RD. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignedNumber"])

    @AssignedNumber.setter
    def AssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignedNumber"], value)

    @property
    def AssignedNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step for for the assigned number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignedNumberStep"])

    @AssignedNumberStep.setter
    def AssignedNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignedNumberStep"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If the type was set to ip, this is the 4-byte IP address in the Administrator subfield of the Value field of the MVPN Route Distinguisher (RD). It is the Global part of the RD. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def IpAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment step for for the IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressStep"])

    @IpAddressStep.setter
    def IpAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressStep"], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(as | ip | asNumber2): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    def update(
        self,
        AsNumber=None,
        AsNumberStep=None,
        AssignedNumber=None,
        AssignedNumberStep=None,
        IpAddress=None,
        IpAddressStep=None,
        Type=None,
    ):
        # type: (int, int, int, int, str, str, str) -> RouteDistinguisher
        """Updates routeDistinguisher resource on the server.

        Args
        ----
        - AsNumber (number): If the type was set to as or asNumber2, this is the AS number in the Administrator subfield of the Value field of the MVPN Route Distinguisher (RD). It is the Global part of the RD. (default = 0)
        - AsNumberStep (number): The increment step for for the AS.
        - AssignedNumber (number): The Assigned Number sub-field of the Value field of the MVPN Route Distinguisher. It is a number from a numbering space, which the enterprise administers, for a given IP address or ASN space. It is the Local part of the RD. (default = 0)
        - AssignedNumberStep (number): The increment step for for the assigned number.
        - IpAddress (str): If the type was set to ip, this is the 4-byte IP address in the Administrator subfield of the Value field of the MVPN Route Distinguisher (RD). It is the Global part of the RD. (default = 0.0.0.0)
        - IpAddressStep (str): The increment step for for the IP address.
        - Type (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AsNumber=None,
        AsNumberStep=None,
        AssignedNumber=None,
        AssignedNumberStep=None,
        IpAddress=None,
        IpAddressStep=None,
        Type=None,
    ):
        # type: (int, int, int, int, str, str, str) -> RouteDistinguisher
        """Finds and retrieves routeDistinguisher resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeDistinguisher resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeDistinguisher resources from the server.

        Args
        ----
        - AsNumber (number): If the type was set to as or asNumber2, this is the AS number in the Administrator subfield of the Value field of the MVPN Route Distinguisher (RD). It is the Global part of the RD. (default = 0)
        - AsNumberStep (number): The increment step for for the AS.
        - AssignedNumber (number): The Assigned Number sub-field of the Value field of the MVPN Route Distinguisher. It is a number from a numbering space, which the enterprise administers, for a given IP address or ASN space. It is the Local part of the RD. (default = 0)
        - AssignedNumberStep (number): The increment step for for the assigned number.
        - IpAddress (str): If the type was set to ip, this is the 4-byte IP address in the Administrator subfield of the Value field of the MVPN Route Distinguisher (RD). It is the Global part of the RD. (default = 0.0.0.0)
        - IpAddressStep (str): The increment step for for the IP address.
        - Type (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.

        Returns
        -------
        - self: This instance with matching routeDistinguisher resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of routeDistinguisher data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the routeDistinguisher resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
