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


class FcoeFipGen(Base):
    """This object configures the options for FCoE FIP parameters.
    The FcoeFipGen class encapsulates a list of fcoeFipGen resources that are managed by the system.
    A list of resources can be retrieved from the server using the FcoeFipGen.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "fcoeFipGen"
    _SDM_ATT_MAP = {
        "AllowFip": "allowFip",
        "FipAddressingMode": "fipAddressingMode",
        "FipAdvertisementPeriod": "fipAdvertisementPeriod",
        "FipEnabled": "fipEnabled",
        "FipMaxFcoeSize": "fipMaxFcoeSize",
        "FipOverrideAdvertisementPeriod": "fipOverrideAdvertisementPeriod",
        "FipOverrideVnportKeepAlivePeriod": "fipOverrideVnportKeepAlivePeriod",
        "FipProposeMacInFpma": "fipProposeMacInFpma",
        "FipRestartOnSessionDown": "fipRestartOnSessionDown",
        "FipSendKeepAlives": "fipSendKeepAlives",
        "FipVendorIdIncrement": "fipVendorIdIncrement",
        "FipVendorIdStart": "fipVendorIdStart",
        "FipVersion": "fipVersion",
        "FipVlanDiscovery": "fipVlanDiscovery",
        "FipVlanDiscoveryUntagged": "fipVlanDiscoveryUntagged",
        "FipVnportKeepAlivePeriod": "fipVnportKeepAlivePeriod",
        "IsPlogiAvailable": "isPlogiAvailable",
        "NameServerRegistration": "nameServerRegistration",
        "PlogiEnabled": "plogiEnabled",
        "PlogiMeshMode": "plogiMeshMode",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FcoeFipGen, self).__init__(parent, list_op)

    @property
    def AllowFip(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, allows FCoE Initialization Protocol (FIP).
        """
        return self._get_attribute(self._SDM_ATT_MAP["AllowFip"])

    @AllowFip.setter
    def AllowFip(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AllowFip"], value)

    @property
    def FipAddressingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The addressing mode specified by FLOGI/FDISC requests.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipAddressingMode"])

    @FipAddressingMode.setter
    def FipAddressingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipAddressingMode"], value)

    @property
    def FipAdvertisementPeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If selected, IxNetwork will use the Discovery Advertisement period that you specify (between 1 and 90 seconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipAdvertisementPeriod"])

    @FipAdvertisementPeriod.setter
    def FipAdvertisementPeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipAdvertisementPeriod"], value)

    @property
    def FipEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, enables FCoE Initialization Protocol (FIP).
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipEnabled"])

    @FipEnabled.setter
    def FipEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipEnabled"], value)

    @property
    def FipMaxFcoeSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum FCoE frame size in bytes. The default is 2158, the minimum is 64, and the maximum is 9216.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipMaxFcoeSize"])

    @FipMaxFcoeSize.setter
    def FipMaxFcoeSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipMaxFcoeSize"], value)

    @property
    def FipOverrideAdvertisementPeriod(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IxNetwork will override the Discovery Advertisement period.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipOverrideAdvertisementPeriod"])

    @FipOverrideAdvertisementPeriod.setter
    def FipOverrideAdvertisementPeriod(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipOverrideAdvertisementPeriod"], value)

    @property
    def FipOverrideVnportKeepAlivePeriod(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When enabled, IxNetwork will override the VN_Port Keep-Alive period.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FipOverrideVnportKeepAlivePeriod"]
        )

    @FipOverrideVnportKeepAlivePeriod.setter
    def FipOverrideVnportKeepAlivePeriod(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FipOverrideVnportKeepAlivePeriod"], value
        )

    @property
    def FipProposeMacInFpma(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Ixia emulated ENodes will propose a non-zero, valid MAC address inFPMA FLOGI request.If cleared, Ixia emulated ENodes will encode an all-zero MAC address in FPMAFLOGI request.This option is unavailable when only FC ports are used in the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipProposeMacInFpma"])

    @FipProposeMacInFpma.setter
    def FipProposeMacInFpma(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipProposeMacInFpma"], value)

    @property
    def FipRestartOnSessionDown(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the port will restart FIP negotiations if the session goes down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipRestartOnSessionDown"])

    @FipRestartOnSessionDown.setter
    def FipRestartOnSessionDown(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipRestartOnSessionDown"], value)

    @property
    def FipSendKeepAlives(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the port will send ENode/VN_Port FIP Keep-Alive messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipSendKeepAlives"])

    @FipSendKeepAlives.setter
    def FipSendKeepAlives(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipSendKeepAlives"], value)

    @property
    def FipVendorIdIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which the Vendor Identifier is incremented for each new range. The default value is 00:00:00:00:00:00:00:01.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipVendorIdIncrement"])

    @FipVendorIdIncrement.setter
    def FipVendorIdIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipVendorIdIncrement"], value)

    @property
    def FipVendorIdStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 8-byte hexadecimal Vendor Identifier. The default value is AA:BB:CC:DD:EE:FF:11:22.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipVendorIdStart"])

    @FipVendorIdStart.setter
    def FipVendorIdStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipVendorIdStart"], value)

    @property
    def FipVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The FIP version to use. Options are:AutoVersion 0Version 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipVersion"])

    @FipVersion.setter
    def FipVersion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipVersion"], value)

    @property
    def FipVlanDiscovery(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1 Ethernet frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipVlanDiscovery"])

    @FipVlanDiscovery.setter
    def FipVlanDiscovery(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipVlanDiscovery"], value)

    @property
    def FipVlanDiscoveryUntagged(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1Ethernet frames. If the request is sent over a VLAN that is configured with802.1q Ethernet frames, IxNetwork removes the tags before sending the request.In addition, this option specifies that the ENode expects to receive responses inuntagged frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipVlanDiscoveryUntagged"])

    @FipVlanDiscoveryUntagged.setter
    def FipVlanDiscoveryUntagged(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipVlanDiscoveryUntagged"], value)

    @property
    def FipVnportKeepAlivePeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When enabled, IxNetwork will use the VN_Port Keep-Alive period that youspecify (between 1 and 3600 seconds).The VN_Port Keep-Alive period is the interval (in seconds) between periodicVN_Port FIP Keep-Alive messages.The default value is 90, the minimum is 1, and the maximum is 3600.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipVnportKeepAlivePeriod"])

    @FipVnportKeepAlivePeriod.setter
    def FipVnportKeepAlivePeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipVnportKeepAlivePeriod"], value)

    @property
    def IsPlogiAvailable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Determines if PLOGI is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPlogiAvailable"])

    @IsPlogiAvailable.setter
    def IsPlogiAvailable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsPlogiAvailable"], value)

    @property
    def NameServerRegistration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When set, the port will attempt to register to a Name Server after fabric login. The Name Server typically resides on the FCF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NameServerRegistration"])

    @NameServerRegistration.setter
    def NameServerRegistration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NameServerRegistration"], value)

    @property
    def PlogiEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the port will initiate a PLOGI from each initiator-side VN_Port and/or N_Port as soon as the target-side VN_Port and/or N_Port receives an LS_ACCfrom the DUT.This option applies to the FIP and FC protocols.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiEnabled"])

    @PlogiEnabled.setter
    def PlogiEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiEnabled"], value)

    @property
    def PlogiMeshMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The mode used for establishing sessions between originate-side and target-side VN_Ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiMeshMode"])

    @PlogiMeshMode.setter
    def PlogiMeshMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiMeshMode"], value)

    def update(
        self,
        AllowFip=None,
        FipAddressingMode=None,
        FipAdvertisementPeriod=None,
        FipEnabled=None,
        FipMaxFcoeSize=None,
        FipOverrideAdvertisementPeriod=None,
        FipOverrideVnportKeepAlivePeriod=None,
        FipProposeMacInFpma=None,
        FipRestartOnSessionDown=None,
        FipSendKeepAlives=None,
        FipVendorIdIncrement=None,
        FipVendorIdStart=None,
        FipVersion=None,
        FipVlanDiscovery=None,
        FipVlanDiscoveryUntagged=None,
        FipVnportKeepAlivePeriod=None,
        IsPlogiAvailable=None,
        NameServerRegistration=None,
        PlogiEnabled=None,
        PlogiMeshMode=None,
    ):
        # type: (bool, str, int, bool, int, bool, bool, bool, bool, bool, str, str, str, bool, bool, int, bool, bool, bool, str) -> FcoeFipGen
        """Updates fcoeFipGen resource on the server.

        Args
        ----
        - AllowFip (bool): If selected, allows FCoE Initialization Protocol (FIP).
        - FipAddressingMode (str): The addressing mode specified by FLOGI/FDISC requests.
        - FipAdvertisementPeriod (number): If selected, IxNetwork will use the Discovery Advertisement period that you specify (between 1 and 90 seconds).
        - FipEnabled (bool): If selected, enables FCoE Initialization Protocol (FIP).
        - FipMaxFcoeSize (number): The maximum FCoE frame size in bytes. The default is 2158, the minimum is 64, and the maximum is 9216.
        - FipOverrideAdvertisementPeriod (bool): If selected, IxNetwork will override the Discovery Advertisement period.
        - FipOverrideVnportKeepAlivePeriod (bool): When enabled, IxNetwork will override the VN_Port Keep-Alive period.
        - FipProposeMacInFpma (bool): If selected, Ixia emulated ENodes will propose a non-zero, valid MAC address inFPMA FLOGI request.If cleared, Ixia emulated ENodes will encode an all-zero MAC address in FPMAFLOGI request.This option is unavailable when only FC ports are used in the test configuration.
        - FipRestartOnSessionDown (bool): If selected, the port will restart FIP negotiations if the session goes down.
        - FipSendKeepAlives (bool): If selected, the port will send ENode/VN_Port FIP Keep-Alive messages.
        - FipVendorIdIncrement (str): The value by which the Vendor Identifier is incremented for each new range. The default value is 00:00:00:00:00:00:00:01.
        - FipVendorIdStart (str): The 8-byte hexadecimal Vendor Identifier. The default value is AA:BB:CC:DD:EE:FF:11:22.
        - FipVersion (str): The FIP version to use. Options are:AutoVersion 0Version 1.
        - FipVlanDiscovery (bool): If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1 Ethernet frames.
        - FipVlanDiscoveryUntagged (bool): If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1Ethernet frames. If the request is sent over a VLAN that is configured with802.1q Ethernet frames, IxNetwork removes the tags before sending the request.In addition, this option specifies that the ENode expects to receive responses inuntagged frames.
        - FipVnportKeepAlivePeriod (number): When enabled, IxNetwork will use the VN_Port Keep-Alive period that youspecify (between 1 and 3600 seconds).The VN_Port Keep-Alive period is the interval (in seconds) between periodicVN_Port FIP Keep-Alive messages.The default value is 90, the minimum is 1, and the maximum is 3600.
        - IsPlogiAvailable (bool): Determines if PLOGI is enabled.
        - NameServerRegistration (bool): When set, the port will attempt to register to a Name Server after fabric login. The Name Server typically resides on the FCF.
        - PlogiEnabled (bool): If selected, the port will initiate a PLOGI from each initiator-side VN_Port and/or N_Port as soon as the target-side VN_Port and/or N_Port receives an LS_ACCfrom the DUT.This option applies to the FIP and FC protocols.
        - PlogiMeshMode (str): The mode used for establishing sessions between originate-side and target-side VN_Ports.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AllowFip=None,
        FipAddressingMode=None,
        FipAdvertisementPeriod=None,
        FipEnabled=None,
        FipMaxFcoeSize=None,
        FipOverrideAdvertisementPeriod=None,
        FipOverrideVnportKeepAlivePeriod=None,
        FipProposeMacInFpma=None,
        FipRestartOnSessionDown=None,
        FipSendKeepAlives=None,
        FipVendorIdIncrement=None,
        FipVendorIdStart=None,
        FipVersion=None,
        FipVlanDiscovery=None,
        FipVlanDiscoveryUntagged=None,
        FipVnportKeepAlivePeriod=None,
        IsPlogiAvailable=None,
        NameServerRegistration=None,
        PlogiEnabled=None,
        PlogiMeshMode=None,
    ):
        # type: (bool, str, int, bool, int, bool, bool, bool, bool, bool, str, str, str, bool, bool, int, bool, bool, bool, str) -> FcoeFipGen
        """Adds a new fcoeFipGen resource on the json, only valid with batch add utility

        Args
        ----
        - AllowFip (bool): If selected, allows FCoE Initialization Protocol (FIP).
        - FipAddressingMode (str): The addressing mode specified by FLOGI/FDISC requests.
        - FipAdvertisementPeriod (number): If selected, IxNetwork will use the Discovery Advertisement period that you specify (between 1 and 90 seconds).
        - FipEnabled (bool): If selected, enables FCoE Initialization Protocol (FIP).
        - FipMaxFcoeSize (number): The maximum FCoE frame size in bytes. The default is 2158, the minimum is 64, and the maximum is 9216.
        - FipOverrideAdvertisementPeriod (bool): If selected, IxNetwork will override the Discovery Advertisement period.
        - FipOverrideVnportKeepAlivePeriod (bool): When enabled, IxNetwork will override the VN_Port Keep-Alive period.
        - FipProposeMacInFpma (bool): If selected, Ixia emulated ENodes will propose a non-zero, valid MAC address inFPMA FLOGI request.If cleared, Ixia emulated ENodes will encode an all-zero MAC address in FPMAFLOGI request.This option is unavailable when only FC ports are used in the test configuration.
        - FipRestartOnSessionDown (bool): If selected, the port will restart FIP negotiations if the session goes down.
        - FipSendKeepAlives (bool): If selected, the port will send ENode/VN_Port FIP Keep-Alive messages.
        - FipVendorIdIncrement (str): The value by which the Vendor Identifier is incremented for each new range. The default value is 00:00:00:00:00:00:00:01.
        - FipVendorIdStart (str): The 8-byte hexadecimal Vendor Identifier. The default value is AA:BB:CC:DD:EE:FF:11:22.
        - FipVersion (str): The FIP version to use. Options are:AutoVersion 0Version 1.
        - FipVlanDiscovery (bool): If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1 Ethernet frames.
        - FipVlanDiscoveryUntagged (bool): If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1Ethernet frames. If the request is sent over a VLAN that is configured with802.1q Ethernet frames, IxNetwork removes the tags before sending the request.In addition, this option specifies that the ENode expects to receive responses inuntagged frames.
        - FipVnportKeepAlivePeriod (number): When enabled, IxNetwork will use the VN_Port Keep-Alive period that youspecify (between 1 and 3600 seconds).The VN_Port Keep-Alive period is the interval (in seconds) between periodicVN_Port FIP Keep-Alive messages.The default value is 90, the minimum is 1, and the maximum is 3600.
        - IsPlogiAvailable (bool): Determines if PLOGI is enabled.
        - NameServerRegistration (bool): When set, the port will attempt to register to a Name Server after fabric login. The Name Server typically resides on the FCF.
        - PlogiEnabled (bool): If selected, the port will initiate a PLOGI from each initiator-side VN_Port and/or N_Port as soon as the target-side VN_Port and/or N_Port receives an LS_ACCfrom the DUT.This option applies to the FIP and FC protocols.
        - PlogiMeshMode (str): The mode used for establishing sessions between originate-side and target-side VN_Ports.

        Returns
        -------
        - self: This instance with all currently retrieved fcoeFipGen resources using find and the newly added fcoeFipGen resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AllowFip=None,
        FipAddressingMode=None,
        FipAdvertisementPeriod=None,
        FipEnabled=None,
        FipMaxFcoeSize=None,
        FipOverrideAdvertisementPeriod=None,
        FipOverrideVnportKeepAlivePeriod=None,
        FipProposeMacInFpma=None,
        FipRestartOnSessionDown=None,
        FipSendKeepAlives=None,
        FipVendorIdIncrement=None,
        FipVendorIdStart=None,
        FipVersion=None,
        FipVlanDiscovery=None,
        FipVlanDiscoveryUntagged=None,
        FipVnportKeepAlivePeriod=None,
        IsPlogiAvailable=None,
        NameServerRegistration=None,
        PlogiEnabled=None,
        PlogiMeshMode=None,
    ):
        # type: (bool, str, int, bool, int, bool, bool, bool, bool, bool, str, str, str, bool, bool, int, bool, bool, bool, str) -> FcoeFipGen
        """Finds and retrieves fcoeFipGen resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeFipGen resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeFipGen resources from the server.

        Args
        ----
        - AllowFip (bool): If selected, allows FCoE Initialization Protocol (FIP).
        - FipAddressingMode (str): The addressing mode specified by FLOGI/FDISC requests.
        - FipAdvertisementPeriod (number): If selected, IxNetwork will use the Discovery Advertisement period that you specify (between 1 and 90 seconds).
        - FipEnabled (bool): If selected, enables FCoE Initialization Protocol (FIP).
        - FipMaxFcoeSize (number): The maximum FCoE frame size in bytes. The default is 2158, the minimum is 64, and the maximum is 9216.
        - FipOverrideAdvertisementPeriod (bool): If selected, IxNetwork will override the Discovery Advertisement period.
        - FipOverrideVnportKeepAlivePeriod (bool): When enabled, IxNetwork will override the VN_Port Keep-Alive period.
        - FipProposeMacInFpma (bool): If selected, Ixia emulated ENodes will propose a non-zero, valid MAC address inFPMA FLOGI request.If cleared, Ixia emulated ENodes will encode an all-zero MAC address in FPMAFLOGI request.This option is unavailable when only FC ports are used in the test configuration.
        - FipRestartOnSessionDown (bool): If selected, the port will restart FIP negotiations if the session goes down.
        - FipSendKeepAlives (bool): If selected, the port will send ENode/VN_Port FIP Keep-Alive messages.
        - FipVendorIdIncrement (str): The value by which the Vendor Identifier is incremented for each new range. The default value is 00:00:00:00:00:00:00:01.
        - FipVendorIdStart (str): The 8-byte hexadecimal Vendor Identifier. The default value is AA:BB:CC:DD:EE:FF:11:22.
        - FipVersion (str): The FIP version to use. Options are:AutoVersion 0Version 1.
        - FipVlanDiscovery (bool): If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1 Ethernet frames.
        - FipVlanDiscoveryUntagged (bool): If selected, the ENode sends FIP VLAN Discovery requests using standard 802.1Ethernet frames. If the request is sent over a VLAN that is configured with802.1q Ethernet frames, IxNetwork removes the tags before sending the request.In addition, this option specifies that the ENode expects to receive responses inuntagged frames.
        - FipVnportKeepAlivePeriod (number): When enabled, IxNetwork will use the VN_Port Keep-Alive period that youspecify (between 1 and 3600 seconds).The VN_Port Keep-Alive period is the interval (in seconds) between periodicVN_Port FIP Keep-Alive messages.The default value is 90, the minimum is 1, and the maximum is 3600.
        - IsPlogiAvailable (bool): Determines if PLOGI is enabled.
        - NameServerRegistration (bool): When set, the port will attempt to register to a Name Server after fabric login. The Name Server typically resides on the FCF.
        - PlogiEnabled (bool): If selected, the port will initiate a PLOGI from each initiator-side VN_Port and/or N_Port as soon as the target-side VN_Port and/or N_Port receives an LS_ACCfrom the DUT.This option applies to the FIP and FC protocols.
        - PlogiMeshMode (str): The mode used for establishing sessions between originate-side and target-side VN_Ports.

        Returns
        -------
        - self: This instance with matching fcoeFipGen resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeFipGen data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeFipGen resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
