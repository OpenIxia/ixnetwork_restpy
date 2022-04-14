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


class Bgp4VpnBgpAdVplsRange(Base):
    """This object holds the available options for the AD VPLS Range.
    The Bgp4VpnBgpAdVplsRange class encapsulates a list of bgp4VpnBgpAdVplsRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the Bgp4VpnBgpAdVplsRange.find() method.
    The list can be managed by using the Bgp4VpnBgpAdVplsRange.add() and Bgp4VpnBgpAdVplsRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "bgp4VpnBgpAdVplsRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "RouteDistinguisherAsNumber": "routeDistinguisherAsNumber",
        "RouteDistinguisherAsNumberStep": "routeDistinguisherAsNumberStep",
        "RouteDistinguisherAssignedNumber": "routeDistinguisherAssignedNumber",
        "RouteDistinguisherAssignedNumberStep": "routeDistinguisherAssignedNumberStep",
        "RouteDistinguisherIpAddress": "routeDistinguisherIpAddress",
        "RouteDistinguisherIpAddressStep": "routeDistinguisherIpAddressStep",
        "RouteDistinguisherType": "routeDistinguisherType",
        "RouteTargetAsNumber": "routeTargetAsNumber",
        "RouteTargetAsNumberStep": "routeTargetAsNumberStep",
        "RouteTargetAssignedNumber": "routeTargetAssignedNumber",
        "RouteTargetAssignedNumberStep": "routeTargetAssignedNumberStep",
        "RouteTargetIpAddress": "routeTargetIpAddress",
        "RouteTargetIpAddressStep": "routeTargetIpAddressStep",
        "RouteTargetType": "routeTargetType",
        "UseRouteDistinguisherAsRouteTarget": "useRouteDistinguisherAsRouteTarget",
        "UseVplsIdAsRouteDistinguisher": "useVplsIdAsRouteDistinguisher",
        "VplsCount": "vplsCount",
        "VplsIdAsNumber": "vplsIdAsNumber",
        "VplsIdAsNumberStep": "vplsIdAsNumberStep",
        "VplsIdAssignedNumber": "vplsIdAssignedNumber",
        "VplsIdAssignedNumberStep": "vplsIdAssignedNumberStep",
        "VplsIdIpAddress": "vplsIdIpAddress",
        "VplsIdIpAddressStep": "vplsIdIpAddressStep",
        "VplsIdType": "vplsIdType",
        "VsiId": "vsiId",
        "VsiIdAssignedNumber": "vsiIdAssignedNumber",
    }
    _SDM_ENUM_MAP = {
        "routeDistinguisherType": ["asNumber", "ipAddress"],
        "routeTargetType": ["asNumber", "ipAddress"],
        "vplsIdType": ["asNumber", "ipAddress"],
        "vsiId": ["concatenatePeAddress", "concatenateAssignedNumber"],
    }

    def __init__(self, parent, list_op=False):
        super(Bgp4VpnBgpAdVplsRange, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables one BGP AD VPLS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def RouteDistinguisherAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This option is available for use if Distinguish Type is set to AS. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherAsNumber"])

    @RouteDistinguisherAsNumber.setter
    def RouteDistinguisherAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherAsNumber"], value)

    @property
    def RouteDistinguisherAsNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This option is available for use if Distinguish Type is set to AS. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherAsNumberStep"])

    @RouteDistinguisherAsNumberStep.setter
    def RouteDistinguisherAsNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherAsNumberStep"], value)

    @property
    def RouteDistinguisherAssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The distinguisher assigned number. The default is 0.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RouteDistinguisherAssignedNumber"]
        )

    @RouteDistinguisherAssignedNumber.setter
    def RouteDistinguisherAssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RouteDistinguisherAssignedNumber"], value
        )

    @property
    def RouteDistinguisherAssignedNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The distinguisher assigned number. The default is 0.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RouteDistinguisherAssignedNumberStep"]
        )

    @RouteDistinguisherAssignedNumberStep.setter
    def RouteDistinguisherAssignedNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RouteDistinguisherAssignedNumberStep"], value
        )

    @property
    def RouteDistinguisherIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Available for use only if the IPv4 Input is set to IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherIpAddress"])

    @RouteDistinguisherIpAddress.setter
    def RouteDistinguisherIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherIpAddress"], value)

    @property
    def RouteDistinguisherIpAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Available for use only if the IPv4 Input is set to IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherIpAddressStep"])

    @RouteDistinguisherIpAddressStep.setter
    def RouteDistinguisherIpAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherIpAddressStep"], value)

    @property
    def RouteDistinguisherType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(asNumber | ipAddress): The RD type, one of AS and IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherType"])

    @RouteDistinguisherType.setter
    def RouteDistinguisherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherType"], value)

    @property
    def RouteTargetAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Available for use only if Distinguish Type is set to AS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetAsNumber"])

    @RouteTargetAsNumber.setter
    def RouteTargetAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetAsNumber"], value)

    @property
    def RouteTargetAsNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Available for use only if Target AS Number is set to AS. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetAsNumberStep"])

    @RouteTargetAsNumberStep.setter
    def RouteTargetAsNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetAsNumberStep"], value)

    @property
    def RouteTargetAssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The target assigned number. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetAssignedNumber"])

    @RouteTargetAssignedNumber.setter
    def RouteTargetAssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetAssignedNumber"], value)

    @property
    def RouteTargetAssignedNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The target assigned number. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetAssignedNumberStep"])

    @RouteTargetAssignedNumberStep.setter
    def RouteTargetAssignedNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetAssignedNumberStep"], value)

    @property
    def RouteTargetIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Available for use only if the IPv4 Input is set to IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetIpAddress"])

    @RouteTargetIpAddress.setter
    def RouteTargetIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetIpAddress"], value)

    @property
    def RouteTargetIpAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Available for use only if it is set to IP. The default is 0.0.0.0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetIpAddressStep"])

    @RouteTargetIpAddressStep.setter
    def RouteTargetIpAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetIpAddressStep"], value)

    @property
    def RouteTargetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(asNumber | ipAddress): The RT format, one of AS and IP. The default is AS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetType"])

    @RouteTargetType.setter
    def RouteTargetType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetType"], value)

    @property
    def UseRouteDistinguisherAsRouteTarget(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the route distinginguisher is used as the route target.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["UseRouteDistinguisherAsRouteTarget"]
        )

    @UseRouteDistinguisherAsRouteTarget.setter
    def UseRouteDistinguisherAsRouteTarget(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["UseRouteDistinguisherAsRouteTarget"], value
        )

    @property
    def UseVplsIdAsRouteDistinguisher(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the VPLS Id is used as the route distinguisher.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseVplsIdAsRouteDistinguisher"])

    @UseVplsIdAsRouteDistinguisher.setter
    def UseVplsIdAsRouteDistinguisher(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseVplsIdAsRouteDistinguisher"], value)

    @property
    def VplsCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Integer value that indicates the number of VPLS instance emulated using this VPLS range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsCount"])

    @VplsCount.setter
    def VplsCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsCount"], value)

    @property
    def VplsIdAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Available for use if VPLS Id Type is set to AS. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsIdAsNumber"])

    @VplsIdAsNumber.setter
    def VplsIdAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsIdAsNumber"], value)

    @property
    def VplsIdAsNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Available for use only if VPLS Id Type is set to AS. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsIdAsNumberStep"])

    @VplsIdAsNumberStep.setter
    def VplsIdAsNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsIdAsNumberStep"], value)

    @property
    def VplsIdAssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The indicated value for the VPLS Id Assigned Number attribute. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsIdAssignedNumber"])

    @VplsIdAssignedNumber.setter
    def VplsIdAssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsIdAssignedNumber"], value)

    @property
    def VplsIdAssignedNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The indicated number for the VPLS Id Assigned Number attribute. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsIdAssignedNumberStep"])

    @VplsIdAssignedNumberStep.setter
    def VplsIdAssignedNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsIdAssignedNumberStep"], value)

    @property
    def VplsIdIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsIdIpAddress"])

    @VplsIdIpAddress.setter
    def VplsIdIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsIdIpAddress"], value)

    @property
    def VplsIdIpAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsIdIpAddressStep"])

    @VplsIdIpAddressStep.setter
    def VplsIdIpAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsIdIpAddressStep"], value)

    @property
    def VplsIdType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(asNumber | ipAddress): The VPLS ID type, one of AS and IP. Default is AS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VplsIdType"])

    @VplsIdType.setter
    def VplsIdType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VplsIdType"], value)

    @property
    def VsiId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(concatenatePeAddress | concatenateAssignedNumber): The VSI ID, one of concatenatePeAddress and concatenateAssignedNumber.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VsiId"])

    @VsiId.setter
    def VsiId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VsiId"], value)

    @property
    def VsiIdAssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The indicated value for the VSI ID Assigned Number attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VsiIdAssignedNumber"])

    @VsiIdAssignedNumber.setter
    def VsiIdAssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VsiIdAssignedNumber"], value)

    def update(
        self,
        Enabled=None,
        RouteDistinguisherAsNumber=None,
        RouteDistinguisherAsNumberStep=None,
        RouteDistinguisherAssignedNumber=None,
        RouteDistinguisherAssignedNumberStep=None,
        RouteDistinguisherIpAddress=None,
        RouteDistinguisherIpAddressStep=None,
        RouteDistinguisherType=None,
        RouteTargetAsNumber=None,
        RouteTargetAsNumberStep=None,
        RouteTargetAssignedNumber=None,
        RouteTargetAssignedNumberStep=None,
        RouteTargetIpAddress=None,
        RouteTargetIpAddressStep=None,
        RouteTargetType=None,
        UseRouteDistinguisherAsRouteTarget=None,
        UseVplsIdAsRouteDistinguisher=None,
        VplsCount=None,
        VplsIdAsNumber=None,
        VplsIdAsNumberStep=None,
        VplsIdAssignedNumber=None,
        VplsIdAssignedNumberStep=None,
        VplsIdIpAddress=None,
        VplsIdIpAddressStep=None,
        VplsIdType=None,
        VsiId=None,
        VsiIdAssignedNumber=None,
    ):
        # type: (bool, int, int, int, int, str, str, str, int, int, int, int, str, str, str, bool, bool, int, int, int, int, int, str, str, str, str, int) -> Bgp4VpnBgpAdVplsRange
        """Updates bgp4VpnBgpAdVplsRange resource on the server.

        Args
        ----
        - Enabled (bool): If true, enables one BGP AD VPLS.
        - RouteDistinguisherAsNumber (number): This option is available for use if Distinguish Type is set to AS. The default is 0.
        - RouteDistinguisherAsNumberStep (number): This option is available for use if Distinguish Type is set to AS. The default is 0.
        - RouteDistinguisherAssignedNumber (number): The distinguisher assigned number. The default is 0.
        - RouteDistinguisherAssignedNumberStep (number): The distinguisher assigned number. The default is 0.
        - RouteDistinguisherIpAddress (str): Available for use only if the IPv4 Input is set to IP
        - RouteDistinguisherIpAddressStep (str): Available for use only if the IPv4 Input is set to IP.
        - RouteDistinguisherType (str(asNumber | ipAddress)): The RD type, one of AS and IP.
        - RouteTargetAsNumber (number): Available for use only if Distinguish Type is set to AS.
        - RouteTargetAsNumberStep (number): Available for use only if Target AS Number is set to AS. The default is 0.
        - RouteTargetAssignedNumber (number): The target assigned number. The default is 0.
        - RouteTargetAssignedNumberStep (number): The target assigned number. The default is 0.
        - RouteTargetIpAddress (str): Available for use only if the IPv4 Input is set to IP.
        - RouteTargetIpAddressStep (str): Available for use only if it is set to IP. The default is 0.0.0.0.
        - RouteTargetType (str(asNumber | ipAddress)): The RT format, one of AS and IP. The default is AS.
        - UseRouteDistinguisherAsRouteTarget (bool): If true, the route distinginguisher is used as the route target.
        - UseVplsIdAsRouteDistinguisher (bool): If true, the VPLS Id is used as the route distinguisher.
        - VplsCount (number): The Integer value that indicates the number of VPLS instance emulated using this VPLS range.
        - VplsIdAsNumber (number): Available for use if VPLS Id Type is set to AS. The default is 0.
        - VplsIdAsNumberStep (number): Available for use only if VPLS Id Type is set to AS. The default is 0.
        - VplsIdAssignedNumber (number): The indicated value for the VPLS Id Assigned Number attribute. The default is 0.
        - VplsIdAssignedNumberStep (number): The indicated number for the VPLS Id Assigned Number attribute. The default is 0.
        - VplsIdIpAddress (str): Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        - VplsIdIpAddressStep (str): Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        - VplsIdType (str(asNumber | ipAddress)): The VPLS ID type, one of AS and IP. Default is AS.
        - VsiId (str(concatenatePeAddress | concatenateAssignedNumber)): The VSI ID, one of concatenatePeAddress and concatenateAssignedNumber.
        - VsiIdAssignedNumber (number): The indicated value for the VSI ID Assigned Number attribute.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        RouteDistinguisherAsNumber=None,
        RouteDistinguisherAsNumberStep=None,
        RouteDistinguisherAssignedNumber=None,
        RouteDistinguisherAssignedNumberStep=None,
        RouteDistinguisherIpAddress=None,
        RouteDistinguisherIpAddressStep=None,
        RouteDistinguisherType=None,
        RouteTargetAsNumber=None,
        RouteTargetAsNumberStep=None,
        RouteTargetAssignedNumber=None,
        RouteTargetAssignedNumberStep=None,
        RouteTargetIpAddress=None,
        RouteTargetIpAddressStep=None,
        RouteTargetType=None,
        UseRouteDistinguisherAsRouteTarget=None,
        UseVplsIdAsRouteDistinguisher=None,
        VplsCount=None,
        VplsIdAsNumber=None,
        VplsIdAsNumberStep=None,
        VplsIdAssignedNumber=None,
        VplsIdAssignedNumberStep=None,
        VplsIdIpAddress=None,
        VplsIdIpAddressStep=None,
        VplsIdType=None,
        VsiId=None,
        VsiIdAssignedNumber=None,
    ):
        # type: (bool, int, int, int, int, str, str, str, int, int, int, int, str, str, str, bool, bool, int, int, int, int, int, str, str, str, str, int) -> Bgp4VpnBgpAdVplsRange
        """Adds a new bgp4VpnBgpAdVplsRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, enables one BGP AD VPLS.
        - RouteDistinguisherAsNumber (number): This option is available for use if Distinguish Type is set to AS. The default is 0.
        - RouteDistinguisherAsNumberStep (number): This option is available for use if Distinguish Type is set to AS. The default is 0.
        - RouteDistinguisherAssignedNumber (number): The distinguisher assigned number. The default is 0.
        - RouteDistinguisherAssignedNumberStep (number): The distinguisher assigned number. The default is 0.
        - RouteDistinguisherIpAddress (str): Available for use only if the IPv4 Input is set to IP
        - RouteDistinguisherIpAddressStep (str): Available for use only if the IPv4 Input is set to IP.
        - RouteDistinguisherType (str(asNumber | ipAddress)): The RD type, one of AS and IP.
        - RouteTargetAsNumber (number): Available for use only if Distinguish Type is set to AS.
        - RouteTargetAsNumberStep (number): Available for use only if Target AS Number is set to AS. The default is 0.
        - RouteTargetAssignedNumber (number): The target assigned number. The default is 0.
        - RouteTargetAssignedNumberStep (number): The target assigned number. The default is 0.
        - RouteTargetIpAddress (str): Available for use only if the IPv4 Input is set to IP.
        - RouteTargetIpAddressStep (str): Available for use only if it is set to IP. The default is 0.0.0.0.
        - RouteTargetType (str(asNumber | ipAddress)): The RT format, one of AS and IP. The default is AS.
        - UseRouteDistinguisherAsRouteTarget (bool): If true, the route distinginguisher is used as the route target.
        - UseVplsIdAsRouteDistinguisher (bool): If true, the VPLS Id is used as the route distinguisher.
        - VplsCount (number): The Integer value that indicates the number of VPLS instance emulated using this VPLS range.
        - VplsIdAsNumber (number): Available for use if VPLS Id Type is set to AS. The default is 0.
        - VplsIdAsNumberStep (number): Available for use only if VPLS Id Type is set to AS. The default is 0.
        - VplsIdAssignedNumber (number): The indicated value for the VPLS Id Assigned Number attribute. The default is 0.
        - VplsIdAssignedNumberStep (number): The indicated number for the VPLS Id Assigned Number attribute. The default is 0.
        - VplsIdIpAddress (str): Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        - VplsIdIpAddressStep (str): Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        - VplsIdType (str(asNumber | ipAddress)): The VPLS ID type, one of AS and IP. Default is AS.
        - VsiId (str(concatenatePeAddress | concatenateAssignedNumber)): The VSI ID, one of concatenatePeAddress and concatenateAssignedNumber.
        - VsiIdAssignedNumber (number): The indicated value for the VSI ID Assigned Number attribute.

        Returns
        -------
        - self: This instance with all currently retrieved bgp4VpnBgpAdVplsRange resources using find and the newly added bgp4VpnBgpAdVplsRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgp4VpnBgpAdVplsRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        RouteDistinguisherAsNumber=None,
        RouteDistinguisherAsNumberStep=None,
        RouteDistinguisherAssignedNumber=None,
        RouteDistinguisherAssignedNumberStep=None,
        RouteDistinguisherIpAddress=None,
        RouteDistinguisherIpAddressStep=None,
        RouteDistinguisherType=None,
        RouteTargetAsNumber=None,
        RouteTargetAsNumberStep=None,
        RouteTargetAssignedNumber=None,
        RouteTargetAssignedNumberStep=None,
        RouteTargetIpAddress=None,
        RouteTargetIpAddressStep=None,
        RouteTargetType=None,
        UseRouteDistinguisherAsRouteTarget=None,
        UseVplsIdAsRouteDistinguisher=None,
        VplsCount=None,
        VplsIdAsNumber=None,
        VplsIdAsNumberStep=None,
        VplsIdAssignedNumber=None,
        VplsIdAssignedNumberStep=None,
        VplsIdIpAddress=None,
        VplsIdIpAddressStep=None,
        VplsIdType=None,
        VsiId=None,
        VsiIdAssignedNumber=None,
    ):
        # type: (bool, int, int, int, int, str, str, str, int, int, int, int, str, str, str, bool, bool, int, int, int, int, int, str, str, str, str, int) -> Bgp4VpnBgpAdVplsRange
        """Finds and retrieves bgp4VpnBgpAdVplsRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgp4VpnBgpAdVplsRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgp4VpnBgpAdVplsRange resources from the server.

        Args
        ----
        - Enabled (bool): If true, enables one BGP AD VPLS.
        - RouteDistinguisherAsNumber (number): This option is available for use if Distinguish Type is set to AS. The default is 0.
        - RouteDistinguisherAsNumberStep (number): This option is available for use if Distinguish Type is set to AS. The default is 0.
        - RouteDistinguisherAssignedNumber (number): The distinguisher assigned number. The default is 0.
        - RouteDistinguisherAssignedNumberStep (number): The distinguisher assigned number. The default is 0.
        - RouteDistinguisherIpAddress (str): Available for use only if the IPv4 Input is set to IP
        - RouteDistinguisherIpAddressStep (str): Available for use only if the IPv4 Input is set to IP.
        - RouteDistinguisherType (str(asNumber | ipAddress)): The RD type, one of AS and IP.
        - RouteTargetAsNumber (number): Available for use only if Distinguish Type is set to AS.
        - RouteTargetAsNumberStep (number): Available for use only if Target AS Number is set to AS. The default is 0.
        - RouteTargetAssignedNumber (number): The target assigned number. The default is 0.
        - RouteTargetAssignedNumberStep (number): The target assigned number. The default is 0.
        - RouteTargetIpAddress (str): Available for use only if the IPv4 Input is set to IP.
        - RouteTargetIpAddressStep (str): Available for use only if it is set to IP. The default is 0.0.0.0.
        - RouteTargetType (str(asNumber | ipAddress)): The RT format, one of AS and IP. The default is AS.
        - UseRouteDistinguisherAsRouteTarget (bool): If true, the route distinginguisher is used as the route target.
        - UseVplsIdAsRouteDistinguisher (bool): If true, the VPLS Id is used as the route distinguisher.
        - VplsCount (number): The Integer value that indicates the number of VPLS instance emulated using this VPLS range.
        - VplsIdAsNumber (number): Available for use if VPLS Id Type is set to AS. The default is 0.
        - VplsIdAsNumberStep (number): Available for use only if VPLS Id Type is set to AS. The default is 0.
        - VplsIdAssignedNumber (number): The indicated value for the VPLS Id Assigned Number attribute. The default is 0.
        - VplsIdAssignedNumberStep (number): The indicated number for the VPLS Id Assigned Number attribute. The default is 0.
        - VplsIdIpAddress (str): Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        - VplsIdIpAddressStep (str): Available for use only if the route VPLS Id Type is set to IP. The default is 0.0.0.0
        - VplsIdType (str(asNumber | ipAddress)): The VPLS ID type, one of AS and IP. Default is AS.
        - VsiId (str(concatenatePeAddress | concatenateAssignedNumber)): The VSI ID, one of concatenatePeAddress and concatenateAssignedNumber.
        - VsiIdAssignedNumber (number): The indicated value for the VSI ID Assigned Number attribute.

        Returns
        -------
        - self: This instance with matching bgp4VpnBgpAdVplsRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgp4VpnBgpAdVplsRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgp4VpnBgpAdVplsRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
