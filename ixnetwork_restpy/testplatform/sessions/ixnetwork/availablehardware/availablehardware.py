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


class AvailableHardware(Base):
    """DEPRECATED This is the hierachy of the available hardware.
    The AvailableHardware class encapsulates a required availableHardware resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "availableHardware"
    _SDM_ATT_MAP = {
        "IsLocked": "isLocked",
        "IsOffChassis": "isOffChassis",
        "OffChassisHwM": "offChassisHwM",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AvailableHardware, self).__init__(parent, list_op)

    @property
    def Chassis(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis.Chassis): An instance of the Chassis class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis import (
            Chassis,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Chassis", None) is not None:
                return self._properties.get("Chassis")
        return Chassis(self)

    @property
    def VirtualChassis(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.virtualchassis.VirtualChassis): An instance of the VirtualChassis class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.virtualchassis import (
            VirtualChassis,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VirtualChassis", None) is not None:
                return self._properties.get("VirtualChassis")
        return VirtualChassis(self)._select()

    @property
    def IsLocked(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, locks the Hardware Manager.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLocked"])

    @property
    def IsOffChassis(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, the Hardware Manager is Off Chassis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsOffChassis"])

    @IsOffChassis.setter
    def IsOffChassis(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsOffChassis"], value)

    @property
    def OffChassisHwM(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Enables the Off Chassis Hardware Manager. The Hardware Manager is an IxOS component that manages the resources on an Ixia chassis. IxNetwork communicates with a chassis through Hardware Manager. Normally, Hardware Manager runs on the chassis itself; however, it can also be installed and run on a separate PC. This configuration is known as an Off-Chassis Hardware Manager.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OffChassisHwM"])

    @OffChassisHwM.setter
    def OffChassisHwM(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OffChassisHwM"], value)

    def update(self, IsOffChassis=None, OffChassisHwM=None):
        # type: (bool, str) -> AvailableHardware
        """Updates availableHardware resource on the server.

        Args
        ----
        - IsOffChassis (bool): If true, the Hardware Manager is Off Chassis.
        - OffChassisHwM (str): Enables the Off Chassis Hardware Manager. The Hardware Manager is an IxOS component that manages the resources on an Ixia chassis. IxNetwork communicates with a chassis through Hardware Manager. Normally, Hardware Manager runs on the chassis itself; however, it can also be installed and run on a separate PC. This configuration is known as an Off-Chassis Hardware Manager.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, IsLocked=None, IsOffChassis=None, OffChassisHwM=None):
        # type: (bool, bool, str) -> AvailableHardware
        """Finds and retrieves availableHardware resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve availableHardware resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all availableHardware resources from the server.

        Args
        ----
        - IsLocked (bool): If true, locks the Hardware Manager.
        - IsOffChassis (bool): If true, the Hardware Manager is Off Chassis.
        - OffChassisHwM (str): Enables the Off Chassis Hardware Manager. The Hardware Manager is an IxOS component that manages the resources on an Ixia chassis. IxNetwork communicates with a chassis through Hardware Manager. Normally, Hardware Manager runs on the chassis itself; however, it can also be installed and run on a separate PC. This configuration is known as an Off-Chassis Hardware Manager.

        Returns
        -------
        - self: This instance with matching availableHardware resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of availableHardware data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the availableHardware resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
