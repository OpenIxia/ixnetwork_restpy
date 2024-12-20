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


class Locations(Base):
    """
    The Locations class encapsulates a list of locations resources that are managed by the user.
    A list of resources can be retrieved from the server using the Locations.find() method.
    The list can be managed by using the Locations.add() and Locations.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "locations"
    _SDM_ATT_MAP = {
        "CableLength": "cableLength",
        "ChainTopology": "chainTopology",
        "ConnectRetries": "connectRetries",
        "DeviceType": "deviceType",
        "ErrorDescription": "errorDescription",
        "ErrorState": "errorState",
        "Hostname": "hostname",
        "Ip": "ip",
        "IsMaster": "isMaster",
        "IsPrimary": "isPrimary",
        "IxnBuildNumber": "ixnBuildNumber",
        "IxosBuildNumber": "ixosBuildNumber",
        "LicenseErrors": "licenseErrors",
        "MasterDevice": "masterDevice",
        "OsType": "osType",
        "PeerDeviceBridgeEnabled": "peerDeviceBridgeEnabled",
        "PeerDeviceDescription": "peerDeviceDescription",
        "PeerDeviceHostname": "peerDeviceHostname",
        "PeerDeviceMac": "peerDeviceMac",
        "PeerDeviceMgmtIp": "peerDeviceMgmtIp",
        "PeerDeviceRouterEnabled": "peerDeviceRouterEnabled",
        "PrimaryDevice": "primaryDevice",
        "ProtocolBuildNumber": "protocolBuildNumber",
        "SequenceId": "sequenceId",
        "State": "state",
        "StateV2": "stateV2",
    }
    _SDM_ENUM_MAP = {
        "chainTopology": ["daisy", "none", "star"],
        "errorState": [
            "ConnectError",
            "DuplicateChassis",
            "IncompatibleIxOS",
            "MultipleNics",
            "NoCardsFound",
            "NoError",
            "NoLicenseFound",
            "NonAppliance",
            "NonLinuxChassis",
        ],
        "osType": ["linux", "unknown", "windows"],
        "state": ["down", "down", "polling", "polling", "polling", "ready"],
        "stateV2": [
            "connectError",
            "down",
            "notConnected",
            "polling",
            "pollingWait",
            "ready",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Locations, self).__init__(parent, list_op)

    @property
    def Ports(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.ports.ports.Ports): An instance of the Ports class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.ports.ports import (
            Ports,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ports", None) is not None:
                return self._properties.get("Ports")
        return Ports(self)

    @property
    def ResourceGroups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.resourcegroups.resourcegroups.ResourceGroups): An instance of the ResourceGroups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.resourcegroups.resourcegroups import (
            ResourceGroups,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ResourceGroups", None) is not None:
                return self._properties.get("ResourceGroups")
        return ResourceGroups(self)

    @property
    def CableLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the length of the cable between two adjacent devices. Must be set only after the device hostname has been set and committed on the current device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CableLength"])

    @CableLength.setter
    def CableLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CableLength"], value)

    @property
    def ChainTopology(self):
        # type: () -> str
        """
        Returns
        -------
        - str(daisy | none | star): The chain topology type. This must be defined on the primary device. It must be defined only after the device host name has been specified and applied on the current device. For legacy device chains, the daisy chainTopology should be indicated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChainTopology"])

    @ChainTopology.setter
    def ChainTopology(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChainTopology"], value)

    @property
    def ConnectRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of time the client attempted to re-connect with the device. (read only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectRetries"])

    @property
    def DeviceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeviceType"])

    @property
    def ErrorDescription(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Connection error description.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorDescription"])

    @property
    def ErrorState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ConnectError | DuplicateChassis | IncompatibleIxOS | MultipleNics | NoCardsFound | NoError | NoLicenseFound | NonAppliance | NonLinuxChassis): Device error state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorState"])

    @property
    def Hostname(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The hostname or IP address associated with the device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Hostname"])

    @Hostname.setter
    def Hostname(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Hostname"], value)

    @property
    def Ip(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address associated with the device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ip"])

    @property
    def IsMaster(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Specifies whether this device is a primary of a secondary in a chain. There can be only one primary device in a chain. NOTE: The primary is automatically assigned based on cable connections.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsMaster"])

    @property
    def IsPrimary(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Specifies whether this device is a primary of a secondary in a chain.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPrimary"])

    @property
    def IxnBuildNumber(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IxNetwork build number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IxnBuildNumber"])

    @property
    def IxosBuildNumber(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IxOS version running on the device in use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IxosBuildNumber"])

    @property
    def LicenseErrors(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Shows the licensing errors that occurred due to licensing problems.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LicenseErrors"])

    @property
    def MasterDevice(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specify the hostname of the primary device on a secondary device. Must be left blank on primary. Must be set only after the device hostname has been set and committed on the current device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterDevice"])

    @MasterDevice.setter
    def MasterDevice(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterDevice"], value)

    @property
    def OsType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(linux | unknown | windows): Device OS type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OsType"])

    @property
    def PeerDeviceBridgeEnabled(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Bridge enabled status of discovered peer device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerDeviceBridgeEnabled"])

    @property
    def PeerDeviceDescription(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Description of discovered peer device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerDeviceDescription"])

    @property
    def PeerDeviceHostname(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Hostname of discovered peer device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerDeviceHostname"])

    @property
    def PeerDeviceMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: MAC address of discovered peer device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerDeviceMac"])

    @property
    def PeerDeviceMgmtIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Management IP address of discovered peer device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerDeviceMgmtIp"])

    @property
    def PeerDeviceRouterEnabled(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Router enabled status of discovered peer device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerDeviceRouterEnabled"])

    @property
    def PrimaryDevice(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the hostname of the primary chassis on a secondary chassis. Must be left blank on primary. Must be set only after the chassis hostname has been set and committed on the current chassis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrimaryDevice"])

    @PrimaryDevice.setter
    def PrimaryDevice(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrimaryDevice"], value)

    @property
    def ProtocolBuildNumber(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Protocols version of the device in use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolBuildNumber"])

    @property
    def SequenceId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the order at which the device in a chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the device hostname has been set and committed on the current device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceId"])

    @SequenceId.setter
    def SequenceId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceId"], value)

    @property
    def State(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(down | down | polling | polling | polling | ready): The following states can be read from the port: polling, ready, and down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["State"])

    @property
    def StateV2(self):
        # type: () -> str
        """
        Returns
        -------
        - str(connectError | down | notConnected | polling | pollingWait | ready): The following states can be read from the port: polling, notConnected, pollingWait, ready, down, and connectError.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateV2"])

    def update(
        self,
        CableLength=None,
        ChainTopology=None,
        Hostname=None,
        MasterDevice=None,
        PrimaryDevice=None,
        SequenceId=None,
    ):
        # type: (int, str, str, str, str, int) -> Locations
        """Updates locations resource on the server.

        Args
        ----
        - CableLength (number): Specifies the length of the cable between two adjacent devices. Must be set only after the device hostname has been set and committed on the current device.
        - ChainTopology (str(daisy | none | star)): The chain topology type. This must be defined on the primary device. It must be defined only after the device host name has been specified and applied on the current device. For legacy device chains, the daisy chainTopology should be indicated.
        - Hostname (str): The hostname or IP address associated with the device.
        - MasterDevice (str): Specify the hostname of the primary device on a secondary device. Must be left blank on primary. Must be set only after the device hostname has been set and committed on the current device.
        - PrimaryDevice (str): Specify the hostname of the primary chassis on a secondary chassis. Must be left blank on primary. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - SequenceId (number): Indicates the order at which the device in a chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the device hostname has been set and committed on the current device.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        CableLength=None,
        ChainTopology=None,
        Hostname=None,
        MasterDevice=None,
        PrimaryDevice=None,
        SequenceId=None,
    ):
        # type: (int, str, str, str, str, int) -> Locations
        """Adds a new locations resource on the server and adds it to the container.

        Args
        ----
        - CableLength (number): Specifies the length of the cable between two adjacent devices. Must be set only after the device hostname has been set and committed on the current device.
        - ChainTopology (str(daisy | none | star)): The chain topology type. This must be defined on the primary device. It must be defined only after the device host name has been specified and applied on the current device. For legacy device chains, the daisy chainTopology should be indicated.
        - Hostname (str): The hostname or IP address associated with the device.
        - MasterDevice (str): Specify the hostname of the primary device on a secondary device. Must be left blank on primary. Must be set only after the device hostname has been set and committed on the current device.
        - PrimaryDevice (str): Specify the hostname of the primary chassis on a secondary chassis. Must be left blank on primary. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - SequenceId (number): Indicates the order at which the device in a chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the device hostname has been set and committed on the current device.

        Returns
        -------
        - self: This instance with all currently retrieved locations resources using find and the newly added locations resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained locations resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        CableLength=None,
        ChainTopology=None,
        ConnectRetries=None,
        DeviceType=None,
        ErrorDescription=None,
        ErrorState=None,
        Hostname=None,
        Ip=None,
        IsMaster=None,
        IsPrimary=None,
        IxnBuildNumber=None,
        IxosBuildNumber=None,
        LicenseErrors=None,
        MasterDevice=None,
        OsType=None,
        PeerDeviceBridgeEnabled=None,
        PeerDeviceDescription=None,
        PeerDeviceHostname=None,
        PeerDeviceMac=None,
        PeerDeviceMgmtIp=None,
        PeerDeviceRouterEnabled=None,
        PrimaryDevice=None,
        ProtocolBuildNumber=None,
        SequenceId=None,
        State=None,
        StateV2=None,
    ):
        # type: (int, str, int, str, str, str, str, str, bool, bool, str, str, List[str], str, str, str, str, str, str, str, str, str, str, int, str, str) -> Locations
        """Finds and retrieves locations resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve locations resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all locations resources from the server.

        Args
        ----
        - CableLength (number): Specifies the length of the cable between two adjacent devices. Must be set only after the device hostname has been set and committed on the current device.
        - ChainTopology (str(daisy | none | star)): The chain topology type. This must be defined on the primary device. It must be defined only after the device host name has been specified and applied on the current device. For legacy device chains, the daisy chainTopology should be indicated.
        - ConnectRetries (number): The number of time the client attempted to re-connect with the device. (read only)
        - DeviceType (str): The type of device.
        - ErrorDescription (str): Connection error description.
        - ErrorState (str(ConnectError | DuplicateChassis | IncompatibleIxOS | MultipleNics | NoCardsFound | NoError | NoLicenseFound | NonAppliance | NonLinuxChassis)): Device error state.
        - Hostname (str): The hostname or IP address associated with the device.
        - Ip (str): The IP address associated with the device.
        - IsMaster (bool): Specifies whether this device is a primary of a secondary in a chain. There can be only one primary device in a chain. NOTE: The primary is automatically assigned based on cable connections.
        - IsPrimary (bool): Specifies whether this device is a primary of a secondary in a chain.
        - IxnBuildNumber (str): IxNetwork build number.
        - IxosBuildNumber (str): The IxOS version running on the device in use.
        - LicenseErrors (list(str)): Shows the licensing errors that occurred due to licensing problems.
        - MasterDevice (str): Specify the hostname of the primary device on a secondary device. Must be left blank on primary. Must be set only after the device hostname has been set and committed on the current device.
        - OsType (str(linux | unknown | windows)): Device OS type.
        - PeerDeviceBridgeEnabled (str): Bridge enabled status of discovered peer device.
        - PeerDeviceDescription (str): Description of discovered peer device.
        - PeerDeviceHostname (str): Hostname of discovered peer device.
        - PeerDeviceMac (str): MAC address of discovered peer device.
        - PeerDeviceMgmtIp (str): Management IP address of discovered peer device.
        - PeerDeviceRouterEnabled (str): Router enabled status of discovered peer device.
        - PrimaryDevice (str): Specify the hostname of the primary chassis on a secondary chassis. Must be left blank on primary. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - ProtocolBuildNumber (str): The Protocols version of the device in use.
        - SequenceId (number): Indicates the order at which the device in a chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the device hostname has been set and committed on the current device.
        - State (str(down | down | polling | polling | polling | ready)): The following states can be read from the port: polling, ready, and down.
        - StateV2 (str(connectError | down | notConnected | polling | pollingWait | ready)): The following states can be read from the port: polling, notConnected, pollingWait, ready, down, and connectError.

        Returns
        -------
        - self: This instance with matching locations resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of locations data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the locations resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
