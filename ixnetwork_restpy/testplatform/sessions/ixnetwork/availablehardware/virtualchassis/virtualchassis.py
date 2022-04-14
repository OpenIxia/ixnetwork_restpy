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


class VirtualChassis(Base):
    """Virtual Chassis is used to get and to manage a Virtual Chassis topology and get  the list of discovered appliances
    The VirtualChassis class encapsulates a required virtualChassis resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "virtualChassis"
    _SDM_ATT_MAP = {
        "EnableLicenseCheck": "enableLicenseCheck",
        "Hostname": "hostname",
        "LicenseServer": "licenseServer",
        "NtpServer": "ntpServer",
        "StartTxDelay": "startTxDelay",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(VirtualChassis, self).__init__(parent, list_op)

    @property
    def DiscoveredAppliance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.discoveredappliance.discoveredappliance.DiscoveredAppliance): An instance of the DiscoveredAppliance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.discoveredappliance.discoveredappliance import (
            DiscoveredAppliance,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DiscoveredAppliance", None) is not None:
                return self._properties.get("DiscoveredAppliance")
        return DiscoveredAppliance(self)

    @property
    def Hypervisor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.hypervisor.hypervisor.Hypervisor): An instance of the Hypervisor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.hypervisor.hypervisor import (
            Hypervisor,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Hypervisor", None) is not None:
                return self._properties.get("Hypervisor")
        return Hypervisor(self)

    @property
    def IxVmCard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.ixvmcard.ixvmcard.IxVmCard): An instance of the IxVmCard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.ixvmcard.ixvmcard import (
            IxVmCard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IxVmCard", None) is not None:
                return self._properties.get("IxVmCard")
        return IxVmCard(self)

    @property
    def EnableLicenseCheck(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables license check on port connect
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLicenseCheck"])

    @EnableLicenseCheck.setter
    def EnableLicenseCheck(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLicenseCheck"], value)

    @property
    def Hostname(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Virtual Chassis hostname or IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["Hostname"])

    @property
    def LicenseServer(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The address of the license server
        """
        return self._get_attribute(self._SDM_ATT_MAP["LicenseServer"])

    @LicenseServer.setter
    def LicenseServer(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LicenseServer"], value)

    @property
    def NtpServer(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The address of the NTP server
        """
        return self._get_attribute(self._SDM_ATT_MAP["NtpServer"])

    @NtpServer.setter
    def NtpServer(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NtpServer"], value)

    @property
    def StartTxDelay(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The delay amount for transmit
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartTxDelay"])

    @StartTxDelay.setter
    def StartTxDelay(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartTxDelay"], value)

    def update(
        self,
        EnableLicenseCheck=None,
        LicenseServer=None,
        NtpServer=None,
        StartTxDelay=None,
    ):
        # type: (bool, str, str, str) -> VirtualChassis
        """Updates virtualChassis resource on the server.

        Args
        ----
        - EnableLicenseCheck (bool): Enables license check on port connect
        - LicenseServer (str): The address of the license server
        - NtpServer (str): The address of the NTP server
        - StartTxDelay (str): The delay amount for transmit

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableLicenseCheck=None,
        Hostname=None,
        LicenseServer=None,
        NtpServer=None,
        StartTxDelay=None,
    ):
        # type: (bool, str, str, str, str) -> VirtualChassis
        """Finds and retrieves virtualChassis resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve virtualChassis resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all virtualChassis resources from the server.

        Args
        ----
        - EnableLicenseCheck (bool): Enables license check on port connect
        - Hostname (str): Virtual Chassis hostname or IP
        - LicenseServer (str): The address of the license server
        - NtpServer (str): The address of the NTP server
        - StartTxDelay (str): The delay amount for transmit

        Returns
        -------
        - self: This instance with matching virtualChassis resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of virtualChassis data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the virtualChassis resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
