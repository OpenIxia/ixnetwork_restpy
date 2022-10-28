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


class Mp(Base):
    """This object contains the Maintenance Point (MP) configuration.
    The Mp class encapsulates a list of mp resources that are managed by the user.
    A list of resources can be retrieved from the server using the Mp.find() method.
    The list can be managed by using the Mp.add() and Mp.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "mp"
    _SDM_ATT_MAP = {
        "AddCcmCustomTlvs": "addCcmCustomTlvs",
        "AddDataTlv": "addDataTlv",
        "AddInterfaceStatusTlv": "addInterfaceStatusTlv",
        "AddLbmCustomTlvs": "addLbmCustomTlvs",
        "AddLbrCustomTlvs": "addLbrCustomTlvs",
        "AddLmmCustomTlvs": "addLmmCustomTlvs",
        "AddLmrCustomTlvs": "addLmrCustomTlvs",
        "AddLtmCustomTlvs": "addLtmCustomTlvs",
        "AddLtrCustomTlvs": "addLtrCustomTlvs",
        "AddOrganizationSpecificTlv": "addOrganizationSpecificTlv",
        "AddPortStatusTlv": "addPortStatusTlv",
        "AddSenderIdTlv": "addSenderIdTlv",
        "AisEnableUnicastMac": "aisEnableUnicastMac",
        "AisInterval": "aisInterval",
        "AisMode": "aisMode",
        "AisPriority": "aisPriority",
        "AisUnicastMac": "aisUnicastMac",
        "AutoDmAllDestination": "autoDmAllDestination",
        "AutoDmDestination": "autoDmDestination",
        "AutoDmIteration": "autoDmIteration",
        "AutoDmTimeout": "autoDmTimeout",
        "AutoDmTimer": "autoDmTimer",
        "AutoLbAllDestination": "autoLbAllDestination",
        "AutoLbDestination": "autoLbDestination",
        "AutoLbIteration": "autoLbIteration",
        "AutoLbTimeout": "autoLbTimeout",
        "AutoLbTimer": "autoLbTimer",
        "AutoLmIteration": "autoLmIteration",
        "AutoLmTimeout": "autoLmTimeout",
        "AutoLmTimer": "autoLmTimer",
        "AutoLtAllDestination": "autoLtAllDestination",
        "AutoLtDestination": "autoLtDestination",
        "AutoLtIteration": "autoLtIteration",
        "AutoLtTimeout": "autoLtTimeout",
        "AutoLtTimer": "autoLtTimer",
        "CciInterval": "cciInterval",
        "CcmLmmTxFcf": "ccmLmmTxFcf",
        "CcmLmmTxFcfStep": "ccmLmmTxFcfStep",
        "CcmPriority": "ccmPriority",
        "CcmRxFcb": "ccmRxFcb",
        "CcmRxFcbStep": "ccmRxFcbStep",
        "ChassisId": "chassisId",
        "ChassisIdLength": "chassisIdLength",
        "ChassisIdSubType": "chassisIdSubType",
        "DataTlvLength": "dataTlvLength",
        "DataTlvValue": "dataTlvValue",
        "DmMethod": "dmMethod",
        "DmPriority": "dmPriority",
        "DmmPriority": "dmmPriority",
        "EnableAisRx": "enableAisRx",
        "EnableAutoDm": "enableAutoDm",
        "EnableAutoLb": "enableAutoLb",
        "EnableAutoLm": "enableAutoLm",
        "EnableAutoLt": "enableAutoLt",
        "EnableLckRx": "enableLckRx",
        "EnableLmCounterUpdate": "enableLmCounterUpdate",
        "EnableTstRx": "enableTstRx",
        "Enabled": "enabled",
        "InterRemoteMepRxIncrementStep": "interRemoteMepRxIncrementStep",
        "InterRemoteMepTxIncrementStep": "interRemoteMepTxIncrementStep",
        "LbmPriority": "lbmPriority",
        "LckEnableUnicastMac": "lckEnableUnicastMac",
        "LckInterval": "lckInterval",
        "LckMode": "lckMode",
        "LckPriority": "lckPriority",
        "LckSupportAisGeneration": "lckSupportAisGeneration",
        "LckUnicastMac": "lckUnicastMac",
        "LmAllRemoteMeps": "lmAllRemoteMeps",
        "LmDestinationMacAddress": "lmDestinationMacAddress",
        "LmMethod": "lmMethod",
        "LmmPriority": "lmmPriority",
        "LmrPriority": "lmrPriority",
        "LmrRxFcf": "lmrRxFcf",
        "LmrRxFcfStep": "lmrRxFcfStep",
        "LtmPriority": "ltmPriority",
        "MacAddress": "macAddress",
        "ManagementAddress": "managementAddress",
        "ManagementAddressDomain": "managementAddressDomain",
        "ManagementAddressDomainLength": "managementAddressDomainLength",
        "ManagementAddressLength": "managementAddressLength",
        "MdLevel": "mdLevel",
        "MegId": "megId",
        "MegIdFormat": "megIdFormat",
        "MepId": "mepId",
        "MipId": "mipId",
        "MpType": "mpType",
        "OrganizationSpecificTlvLength": "organizationSpecificTlvLength",
        "OrganizationSpecificTlvValue": "organizationSpecificTlvValue",
        "OverrideVlanPriority": "overrideVlanPriority",
        "Rdi": "rdi",
        "ShortMaName": "shortMaName",
        "ShortMaNameFormat": "shortMaNameFormat",
        "TstEnableUnicastMac": "tstEnableUnicastMac",
        "TstIncrPacketLength": "tstIncrPacketLength",
        "TstIncrPacketLengthStep": "tstIncrPacketLengthStep",
        "TstInitialPatternValue": "tstInitialPatternValue",
        "TstInterval": "tstInterval",
        "TstMode": "tstMode",
        "TstOverwriteSequenceNumber": "tstOverwriteSequenceNumber",
        "TstPacketLength": "tstPacketLength",
        "TstPatternType": "tstPatternType",
        "TstPriority": "tstPriority",
        "TstSequenceNumber": "tstSequenceNumber",
        "TstTestType": "tstTestType",
        "TstUnicastMac": "tstUnicastMac",
        "Ttl": "ttl",
        "Vlan": "vlan",
    }
    _SDM_ENUM_MAP = {
        "aisInterval": ["oneSec", "oneMin"],
        "aisMode": ["auto", "start", "stop"],
        "cciInterval": [
            "3.33msec",
            "10msec",
            "100msec",
            "1sec",
            "10sec",
            "1min",
            "10min",
        ],
        "chassisIdSubType": [
            "chassisComponent",
            "interfaceAlias",
            "portComponent",
            "macAddress",
            "networkAddress",
            "interfaceName",
            "locallyAssigned",
        ],
        "dmMethod": ["twoWay", "oneWay"],
        "lckInterval": ["oneSec", "oneMin"],
        "lckMode": ["auto", "start", "stop"],
        "lmMethod": ["singleEnded", "dualEnded"],
        "megIdFormat": [
            "iccBasedFormat",
            "primaryVid",
            "characterString",
            "2octetInteger",
            "rfc2685VpnId",
        ],
        "mpType": ["mip", "mep"],
        "rdi": ["auto", "on", "off"],
        "shortMaNameFormat": [
            "primaryVid",
            "characterString",
            "2octetInteger",
            "rfc2685VpnId",
        ],
        "tstMode": ["start", "stop"],
        "tstPatternType": [
            "nullSignalWithoutCrc32",
            "nullSignalWithCrc32",
            "prbs2311WithoutCrc32",
            "prbs2311WithCrc32",
        ],
        "tstTestType": ["inService", "outOfService"],
    }

    def __init__(self, parent, list_op=False):
        super(Mp, self).__init__(parent, list_op)

    @property
    def AddCcmCustomTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom CCM TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddCcmCustomTlvs"])

    @AddCcmCustomTlvs.setter
    def AddCcmCustomTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddCcmCustomTlvs"], value)

    @property
    def AddDataTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a data TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddDataTlv"])

    @AddDataTlv.setter
    def AddDataTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddDataTlv"], value)

    @property
    def AddInterfaceStatusTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds an interface status TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddInterfaceStatusTlv"])

    @AddInterfaceStatusTlv.setter
    def AddInterfaceStatusTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddInterfaceStatusTlv"], value)

    @property
    def AddLbmCustomTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom loopback message TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddLbmCustomTlvs"])

    @AddLbmCustomTlvs.setter
    def AddLbmCustomTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddLbmCustomTlvs"], value)

    @property
    def AddLbrCustomTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom loopback response message TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddLbrCustomTlvs"])

    @AddLbrCustomTlvs.setter
    def AddLbrCustomTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddLbrCustomTlvs"], value)

    @property
    def AddLmmCustomTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddLmmCustomTlvs"])

    @AddLmmCustomTlvs.setter
    def AddLmmCustomTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddLmmCustomTlvs"], value)

    @property
    def AddLmrCustomTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddLmrCustomTlvs"])

    @AddLmrCustomTlvs.setter
    def AddLmrCustomTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddLmrCustomTlvs"], value)

    @property
    def AddLtmCustomTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom link trace message TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddLtmCustomTlvs"])

    @AddLtmCustomTlvs.setter
    def AddLtmCustomTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddLtmCustomTlvs"], value)

    @property
    def AddLtrCustomTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom link trace message TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddLtrCustomTlvs"])

    @AddLtrCustomTlvs.setter
    def AddLtrCustomTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddLtrCustomTlvs"], value)

    @property
    def AddOrganizationSpecificTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom organization specific message TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddOrganizationSpecificTlv"])

    @AddOrganizationSpecificTlv.setter
    def AddOrganizationSpecificTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddOrganizationSpecificTlv"], value)

    @property
    def AddPortStatusTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom port statust message TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddPortStatusTlv"])

    @AddPortStatusTlv.setter
    def AddPortStatusTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddPortStatusTlv"], value)

    @property
    def AddSenderIdTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, adds a custom sender ID message TLV to bridge messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddSenderIdTlv"])

    @AddSenderIdTlv.setter
    def AddSenderIdTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddSenderIdTlv"], value)

    @property
    def AisEnableUnicastMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisEnableUnicastMac"])

    @AisEnableUnicastMac.setter
    def AisEnableUnicastMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisEnableUnicastMac"], value)

    @property
    def AisInterval(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oneSec | oneMin): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisInterval"])

    @AisInterval.setter
    def AisInterval(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisInterval"], value)

    @property
    def AisMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(auto | start | stop): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisMode"])

    @AisMode.setter
    def AisMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisMode"], value)

    @property
    def AisPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisPriority"])

    @AisPriority.setter
    def AisPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisPriority"], value)

    @property
    def AisUnicastMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisUnicastMac"])

    @AisUnicastMac.setter
    def AisUnicastMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisUnicastMac"], value)

    @property
    def AutoDmAllDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of DM Messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoDmAllDestination"])

    @AutoDmAllDestination.setter
    def AutoDmAllDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoDmAllDestination"], value)

    @property
    def AutoDmDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The sent MAC address for the DM, if autoDmAllDestination is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoDmDestination"])

    @AutoDmDestination.setter
    def AutoDmDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoDmDestination"], value)

    @property
    def AutoDmIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoDmIteration"])

    @AutoDmIteration.setter
    def AutoDmIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoDmIteration"], value)

    @property
    def AutoDmTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoDmTimeout"])

    @AutoDmTimeout.setter
    def AutoDmTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoDmTimeout"], value)

    @property
    def AutoDmTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoDmTimer"])

    @AutoDmTimer.setter
    def AutoDmTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoDmTimer"], value)

    @property
    def AutoLbAllDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of Loopback Messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLbAllDestination"])

    @AutoLbAllDestination.setter
    def AutoLbAllDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLbAllDestination"], value)

    @property
    def AutoLbDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the loopback destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLbDestination"])

    @AutoLbDestination.setter
    def AutoLbDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLbDestination"], value)

    @property
    def AutoLbIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLbIteration"])

    @AutoLbIteration.setter
    def AutoLbIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLbIteration"], value)

    @property
    def AutoLbTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLbTimeout"])

    @AutoLbTimeout.setter
    def AutoLbTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLbTimeout"], value)

    @property
    def AutoLbTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time period in seconds between LBMs. Default is 60. Min: 1 Max: 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLbTimer"])

    @AutoLbTimer.setter
    def AutoLbTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLbTimer"], value)

    @property
    def AutoLmIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLmIteration"])

    @AutoLmIteration.setter
    def AutoLmIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLmIteration"], value)

    @property
    def AutoLmTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLmTimeout"])

    @AutoLmTimeout.setter
    def AutoLmTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLmTimeout"], value)

    @property
    def AutoLmTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLmTimer"])

    @AutoLmTimer.setter
    def AutoLmTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLmTimer"], value)

    @property
    def AutoLtAllDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the automatic sending to Link Trace Messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLtAllDestination"])

    @AutoLtAllDestination.setter
    def AutoLtAllDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLtAllDestination"], value)

    @property
    def AutoLtDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the link trance destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLtDestination"])

    @AutoLtDestination.setter
    def AutoLtDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLtDestination"], value)

    @property
    def AutoLtIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLtIteration"])

    @AutoLtIteration.setter
    def AutoLtIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLtIteration"], value)

    @property
    def AutoLtTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLtTimeout"])

    @AutoLtTimeout.setter
    def AutoLtTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLtTimeout"], value)

    @property
    def AutoLtTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoLtTimer"])

    @AutoLtTimer.setter
    def AutoLtTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoLtTimer"], value)

    @property
    def CciInterval(self):
        # type: () -> str
        """
        Returns
        -------
        - str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min): Sets the Continuity Check Interval (CCI).
        """
        return self._get_attribute(self._SDM_ATT_MAP["CciInterval"])

    @CciInterval.setter
    def CciInterval(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CciInterval"], value)

    @property
    def CcmLmmTxFcf(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmLmmTxFcf"])

    @CcmLmmTxFcf.setter
    def CcmLmmTxFcf(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmLmmTxFcf"], value)

    @property
    def CcmLmmTxFcfStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmLmmTxFcfStep"])

    @CcmLmmTxFcfStep.setter
    def CcmLmmTxFcfStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmLmmTxFcfStep"], value)

    @property
    def CcmPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmPriority"])

    @CcmPriority.setter
    def CcmPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmPriority"], value)

    @property
    def CcmRxFcb(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmRxFcb"])

    @CcmRxFcb.setter
    def CcmRxFcb(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmRxFcb"], value)

    @property
    def CcmRxFcbStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmRxFcbStep"])

    @CcmRxFcbStep.setter
    def CcmRxFcbStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmRxFcbStep"], value)

    @property
    def ChassisId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChassisId"])

    @ChassisId.setter
    def ChassisId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChassisId"], value)

    @property
    def ChassisIdLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChassisIdLength"])

    @ChassisIdLength.setter
    def ChassisIdLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChassisIdLength"], value)

    @property
    def ChassisIdSubType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChassisIdSubType"])

    @ChassisIdSubType.setter
    def ChassisIdSubType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChassisIdSubType"], value)

    @property
    def DataTlvLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataTlvLength"])

    @DataTlvLength.setter
    def DataTlvLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataTlvLength"], value)

    @property
    def DataTlvValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataTlvValue"])

    @DataTlvValue.setter
    def DataTlvValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataTlvValue"], value)

    @property
    def DmMethod(self):
        # type: () -> str
        """
        Returns
        -------
        - str(twoWay | oneWay): The type of Delay Measurment support.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmMethod"])

    @DmMethod.setter
    def DmMethod(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmMethod"], value)

    @property
    def DmPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Methodfor each MIP). The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmPriority"])

    @DmPriority.setter
    def DmPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmPriority"], value)

    @property
    def DmmPriority(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmmPriority"])

    @DmmPriority.setter
    def DmmPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmmPriority"], value)

    @property
    def EnableAisRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAisRx"])

    @EnableAisRx.setter
    def EnableAisRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAisRx"], value)

    @property
    def EnableAutoDm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of DM Messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoDm"])

    @EnableAutoDm.setter
    def EnableAutoDm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoDm"], value)

    @property
    def EnableAutoLb(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of Loopback messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoLb"])

    @EnableAutoLb.setter
    def EnableAutoLb(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoLb"], value)

    @property
    def EnableAutoLm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoLm"])

    @EnableAutoLm.setter
    def EnableAutoLm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoLm"], value)

    @property
    def EnableAutoLt(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of Link Trace messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoLt"])

    @EnableAutoLt.setter
    def EnableAutoLt(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoLt"], value)

    @property
    def EnableLckRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLckRx"])

    @EnableLckRx.setter
    def EnableLckRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLckRx"], value)

    @property
    def EnableLmCounterUpdate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLmCounterUpdate"])

    @EnableLmCounterUpdate.setter
    def EnableLmCounterUpdate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLmCounterUpdate"], value)

    @property
    def EnableTstRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTstRx"])

    @EnableTstRx.setter
    def EnableTstRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTstRx"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the MP is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def InterRemoteMepRxIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterRemoteMepRxIncrementStep"])

    @InterRemoteMepRxIncrementStep.setter
    def InterRemoteMepRxIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterRemoteMepRxIncrementStep"], value)

    @property
    def InterRemoteMepTxIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterRemoteMepTxIncrementStep"])

    @InterRemoteMepTxIncrementStep.setter
    def InterRemoteMepTxIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterRemoteMepTxIncrementStep"], value)

    @property
    def LbmPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute(self._SDM_ATT_MAP["LbmPriority"])

    @LbmPriority.setter
    def LbmPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LbmPriority"], value)

    @property
    def LckEnableUnicastMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckEnableUnicastMac"])

    @LckEnableUnicastMac.setter
    def LckEnableUnicastMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckEnableUnicastMac"], value)

    @property
    def LckInterval(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oneSec | oneMin): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckInterval"])

    @LckInterval.setter
    def LckInterval(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckInterval"], value)

    @property
    def LckMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(auto | start | stop): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckMode"])

    @LckMode.setter
    def LckMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckMode"], value)

    @property
    def LckPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckPriority"])

    @LckPriority.setter
    def LckPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckPriority"], value)

    @property
    def LckSupportAisGeneration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckSupportAisGeneration"])

    @LckSupportAisGeneration.setter
    def LckSupportAisGeneration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckSupportAisGeneration"], value)

    @property
    def LckUnicastMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckUnicastMac"])

    @LckUnicastMac.setter
    def LckUnicastMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckUnicastMac"], value)

    @property
    def LmAllRemoteMeps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmAllRemoteMeps"])

    @LmAllRemoteMeps.setter
    def LmAllRemoteMeps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmAllRemoteMeps"], value)

    @property
    def LmDestinationMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmDestinationMacAddress"])

    @LmDestinationMacAddress.setter
    def LmDestinationMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmDestinationMacAddress"], value)

    @property
    def LmMethod(self):
        # type: () -> str
        """
        Returns
        -------
        - str(singleEnded | dualEnded): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmMethod"])

    @LmMethod.setter
    def LmMethod(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmMethod"], value)

    @property
    def LmmPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmmPriority"])

    @LmmPriority.setter
    def LmmPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmmPriority"], value)

    @property
    def LmrPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmrPriority"])

    @LmrPriority.setter
    def LmrPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmrPriority"], value)

    @property
    def LmrRxFcf(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmrRxFcf"])

    @LmrRxFcf.setter
    def LmrRxFcf(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmrRxFcf"], value)

    @property
    def LmrRxFcfStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmrRxFcfStep"])

    @LmrRxFcfStep.setter
    def LmrRxFcfStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmrRxFcfStep"], value)

    @property
    def LtmPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute(self._SDM_ATT_MAP["LtmPriority"])

    @LtmPriority.setter
    def LtmPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LtmPriority"], value)

    @property
    def MacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MAC address of the MP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacAddress"])

    @MacAddress.setter
    def MacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacAddress"], value)

    @property
    def ManagementAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the MP management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ManagementAddress"])

    @ManagementAddress.setter
    def ManagementAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ManagementAddress"], value)

    @property
    def ManagementAddressDomain(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the MP management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ManagementAddressDomain"])

    @ManagementAddressDomain.setter
    def ManagementAddressDomain(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ManagementAddressDomain"], value)

    @property
    def ManagementAddressDomainLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ManagementAddressDomainLength"])

    @ManagementAddressDomainLength.setter
    def ManagementAddressDomainLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ManagementAddressDomainLength"], value)

    @property
    def ManagementAddressLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ManagementAddressLength"])

    @ManagementAddressLength.setter
    def ManagementAddressLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ManagementAddressLength"], value)

    @property
    def MdLevel(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/mdLevel): The MD level of the MP. The MD level must be previously configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel"])

    @MdLevel.setter
    def MdLevel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel"], value)

    @property
    def MegId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MEG identifier of the MP. This is for use with ITU-T Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MegId"])

    @MegId.setter
    def MegId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MegId"], value)

    @property
    def MegIdFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str(iccBasedFormat | primaryVid | characterString | 2octetInteger | rfc2685VpnId): The MEG identifier format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MegIdFormat"])

    @MegIdFormat.setter
    def MegIdFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MegIdFormat"], value)

    @property
    def MepId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The MEP identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepId"])

    @MepId.setter
    def MepId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MepId"], value)

    @property
    def MipId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The MIP identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MipId"])

    @MipId.setter
    def MipId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MipId"], value)

    @property
    def MpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mip | mep): Sets the MP type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MpType"])

    @MpType.setter
    def MpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MpType"], value)

    @property
    def OrganizationSpecificTlvLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        """
        return self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificTlvLength"])

    @OrganizationSpecificTlvLength.setter
    def OrganizationSpecificTlvLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OrganizationSpecificTlvLength"], value)

    @property
    def OrganizationSpecificTlvValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificTlvValue"])

    @OrganizationSpecificTlvValue.setter
    def OrganizationSpecificTlvValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OrganizationSpecificTlvValue"], value)

    @property
    def OverrideVlanPriority(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideVlanPriority"])

    @OverrideVlanPriority.setter
    def OverrideVlanPriority(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideVlanPriority"], value)

    @property
    def Rdi(self):
        # type: () -> str
        """
        Returns
        -------
        - str(auto | on | off): The Remote Defect Identification.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rdi"])

    @Rdi.setter
    def Rdi(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rdi"], value)

    @property
    def ShortMaName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the Short MA name. The format is determined in shortMaNameFormat. This is used with IEEE 802.1ag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShortMaName"])

    @ShortMaName.setter
    def ShortMaName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShortMaName"], value)

    @property
    def ShortMaNameFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str(primaryVid | characterString | 2octetInteger | rfc2685VpnId): Sets the Short MA Name format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShortMaNameFormat"])

    @ShortMaNameFormat.setter
    def ShortMaNameFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShortMaNameFormat"], value)

    @property
    def TstEnableUnicastMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstEnableUnicastMac"])

    @TstEnableUnicastMac.setter
    def TstEnableUnicastMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstEnableUnicastMac"], value)

    @property
    def TstIncrPacketLength(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstIncrPacketLength"])

    @TstIncrPacketLength.setter
    def TstIncrPacketLength(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstIncrPacketLength"], value)

    @property
    def TstIncrPacketLengthStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstIncrPacketLengthStep"])

    @TstIncrPacketLengthStep.setter
    def TstIncrPacketLengthStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstIncrPacketLengthStep"], value)

    @property
    def TstInitialPatternValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstInitialPatternValue"])

    @TstInitialPatternValue.setter
    def TstInitialPatternValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstInitialPatternValue"], value)

    @property
    def TstInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstInterval"])

    @TstInterval.setter
    def TstInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstInterval"], value)

    @property
    def TstMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(start | stop): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstMode"])

    @TstMode.setter
    def TstMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstMode"], value)

    @property
    def TstOverwriteSequenceNumber(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstOverwriteSequenceNumber"])

    @TstOverwriteSequenceNumber.setter
    def TstOverwriteSequenceNumber(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstOverwriteSequenceNumber"], value)

    @property
    def TstPacketLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstPacketLength"])

    @TstPacketLength.setter
    def TstPacketLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstPacketLength"], value)

    @property
    def TstPatternType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstPatternType"])

    @TstPatternType.setter
    def TstPatternType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstPatternType"], value)

    @property
    def TstPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstPriority"])

    @TstPriority.setter
    def TstPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstPriority"], value)

    @property
    def TstSequenceNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstSequenceNumber"])

    @TstSequenceNumber.setter
    def TstSequenceNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstSequenceNumber"], value)

    @property
    def TstTestType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(inService | outOfService): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstTestType"])

    @TstTestType.setter
    def TstTestType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstTestType"], value)

    @property
    def TstUnicastMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstUnicastMac"])

    @TstUnicastMac.setter
    def TstUnicastMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstUnicastMac"], value)

    @property
    def Ttl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the MP Time-to-live value. Default is 64. Min: 1 Max: 255
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ttl"])

    @Ttl.setter
    def Ttl(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ttl"], value)

    @property
    def Vlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/vlans): Assigns a VLAN to the MP. The VLAN must be previously configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Vlan"])

    @Vlan.setter
    def Vlan(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Vlan"], value)

    def update(
        self,
        AddCcmCustomTlvs=None,
        AddDataTlv=None,
        AddInterfaceStatusTlv=None,
        AddLbmCustomTlvs=None,
        AddLbrCustomTlvs=None,
        AddLmmCustomTlvs=None,
        AddLmrCustomTlvs=None,
        AddLtmCustomTlvs=None,
        AddLtrCustomTlvs=None,
        AddOrganizationSpecificTlv=None,
        AddPortStatusTlv=None,
        AddSenderIdTlv=None,
        AisEnableUnicastMac=None,
        AisInterval=None,
        AisMode=None,
        AisPriority=None,
        AisUnicastMac=None,
        AutoDmAllDestination=None,
        AutoDmDestination=None,
        AutoDmIteration=None,
        AutoDmTimeout=None,
        AutoDmTimer=None,
        AutoLbAllDestination=None,
        AutoLbDestination=None,
        AutoLbIteration=None,
        AutoLbTimeout=None,
        AutoLbTimer=None,
        AutoLmIteration=None,
        AutoLmTimeout=None,
        AutoLmTimer=None,
        AutoLtAllDestination=None,
        AutoLtDestination=None,
        AutoLtIteration=None,
        AutoLtTimeout=None,
        AutoLtTimer=None,
        CciInterval=None,
        CcmLmmTxFcf=None,
        CcmLmmTxFcfStep=None,
        CcmPriority=None,
        CcmRxFcb=None,
        CcmRxFcbStep=None,
        ChassisId=None,
        ChassisIdLength=None,
        ChassisIdSubType=None,
        DataTlvLength=None,
        DataTlvValue=None,
        DmMethod=None,
        DmPriority=None,
        DmmPriority=None,
        EnableAisRx=None,
        EnableAutoDm=None,
        EnableAutoLb=None,
        EnableAutoLm=None,
        EnableAutoLt=None,
        EnableLckRx=None,
        EnableLmCounterUpdate=None,
        EnableTstRx=None,
        Enabled=None,
        InterRemoteMepRxIncrementStep=None,
        InterRemoteMepTxIncrementStep=None,
        LbmPriority=None,
        LckEnableUnicastMac=None,
        LckInterval=None,
        LckMode=None,
        LckPriority=None,
        LckSupportAisGeneration=None,
        LckUnicastMac=None,
        LmAllRemoteMeps=None,
        LmDestinationMacAddress=None,
        LmMethod=None,
        LmmPriority=None,
        LmrPriority=None,
        LmrRxFcf=None,
        LmrRxFcfStep=None,
        LtmPriority=None,
        MacAddress=None,
        ManagementAddress=None,
        ManagementAddressDomain=None,
        ManagementAddressDomainLength=None,
        ManagementAddressLength=None,
        MdLevel=None,
        MegId=None,
        MegIdFormat=None,
        MepId=None,
        MipId=None,
        MpType=None,
        OrganizationSpecificTlvLength=None,
        OrganizationSpecificTlvValue=None,
        OverrideVlanPriority=None,
        Rdi=None,
        ShortMaName=None,
        ShortMaNameFormat=None,
        TstEnableUnicastMac=None,
        TstIncrPacketLength=None,
        TstIncrPacketLengthStep=None,
        TstInitialPatternValue=None,
        TstInterval=None,
        TstMode=None,
        TstOverwriteSequenceNumber=None,
        TstPacketLength=None,
        TstPatternType=None,
        TstPriority=None,
        TstSequenceNumber=None,
        TstTestType=None,
        TstUnicastMac=None,
        Ttl=None,
        Vlan=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, bool, str, int, int, int, bool, str, int, int, int, int, int, int, bool, str, int, int, int, str, int, int, int, int, int, str, int, str, int, str, str, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, bool, str, str, int, bool, str, bool, str, str, int, int, int, int, int, str, str, str, int, int, str, str, str, int, int, str, int, str, bool, str, str, str, bool, bool, int, int, int, str, bool, int, str, int, int, str, str, int, str) -> Mp
        """Updates mp resource on the server.

        Args
        ----
        - AddCcmCustomTlvs (bool): If true, adds a custom CCM TLV to bridge messages.
        - AddDataTlv (bool): If true, adds a data TLV to bridge messages.
        - AddInterfaceStatusTlv (bool): If true, adds an interface status TLV to bridge messages.
        - AddLbmCustomTlvs (bool): If true, adds a custom loopback message TLV to bridge messages.
        - AddLbrCustomTlvs (bool): If true, adds a custom loopback response message TLV to bridge messages.
        - AddLmmCustomTlvs (bool): NOT DEFINED
        - AddLmrCustomTlvs (bool): NOT DEFINED
        - AddLtmCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddLtrCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddOrganizationSpecificTlv (bool): If true, adds a custom organization specific message TLV to bridge messages.
        - AddPortStatusTlv (bool): If true, adds a custom port statust message TLV to bridge messages.
        - AddSenderIdTlv (bool): If true, adds a custom sender ID message TLV to bridge messages.
        - AisEnableUnicastMac (bool): NOT DEFINED
        - AisInterval (str(oneSec | oneMin)): NOT DEFINED
        - AisMode (str(auto | start | stop)): NOT DEFINED
        - AisPriority (number): NOT DEFINED
        - AisUnicastMac (str): NOT DEFINED
        - AutoDmAllDestination (bool): If true, enables the automatic sending of DM Messages.
        - AutoDmDestination (str): The sent MAC address for the DM, if autoDmAllDestination is set to true.
        - AutoDmIteration (number): The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoDmTimeout (number): The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        - AutoDmTimer (number): The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        - AutoLbAllDestination (bool): If true, enables the automatic sending of Loopback Messages.
        - AutoLbDestination (str): Sets the loopback destination MAC address.
        - AutoLbIteration (number): The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLbTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLbTimer (number): The time period in seconds between LBMs. Default is 60. Min: 1 Max: 65535
        - AutoLmIteration (number): NOT DEFINED
        - AutoLmTimeout (number): NOT DEFINED
        - AutoLmTimer (number): NOT DEFINED
        - AutoLtAllDestination (bool): If true, enables the automatic sending to Link Trace Messages.
        - AutoLtDestination (str): Sets the link trance destination MAC address.
        - AutoLtIteration (number): The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLtTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLtTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - CciInterval (str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min)): Sets the Continuity Check Interval (CCI).
        - CcmLmmTxFcf (number): NOT DEFINED
        - CcmLmmTxFcfStep (number): NOT DEFINED
        - CcmPriority (number): Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        - CcmRxFcb (number): NOT DEFINED
        - CcmRxFcbStep (number): NOT DEFINED
        - ChassisId (str): Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        - ChassisIdLength (number): Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        - ChassisIdSubType (str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned)): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        - DataTlvLength (number): Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        - DataTlvValue (str): This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        - DmMethod (str(twoWay | oneWay)): The type of Delay Measurment support.
        - DmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Methodfor each MIP). The default is 0.
        - DmmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        - EnableAisRx (bool): NOT DEFINED
        - EnableAutoDm (bool): If true, enables the automatic sending of DM Messages.
        - EnableAutoLb (bool): If true, enables the automatic sending of Loopback messages.
        - EnableAutoLm (bool): NOT DEFINED
        - EnableAutoLt (bool): If true, enables the automatic sending of Link Trace messages.
        - EnableLckRx (bool): NOT DEFINED
        - EnableLmCounterUpdate (bool): NOT DEFINED
        - EnableTstRx (bool): NOT DEFINED
        - Enabled (bool): If true, the MP is enabled.
        - InterRemoteMepRxIncrementStep (number): NOT DEFINED
        - InterRemoteMepTxIncrementStep (number): NOT DEFINED
        - LbmPriority (number): Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        - LckEnableUnicastMac (bool): NOT DEFINED
        - LckInterval (str(oneSec | oneMin)): NOT DEFINED
        - LckMode (str(auto | start | stop)): NOT DEFINED
        - LckPriority (number): NOT DEFINED
        - LckSupportAisGeneration (bool): NOT DEFINED
        - LckUnicastMac (str): NOT DEFINED
        - LmAllRemoteMeps (bool): NOT DEFINED
        - LmDestinationMacAddress (str): NOT DEFINED
        - LmMethod (str(singleEnded | dualEnded)): NOT DEFINED
        - LmmPriority (number): NOT DEFINED
        - LmrPriority (number): NOT DEFINED
        - LmrRxFcf (number): NOT DEFINED
        - LmrRxFcfStep (number): NOT DEFINED
        - LtmPriority (number): Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        - MacAddress (str): The MAC address of the MP.
        - ManagementAddress (str): Sets the MP management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        - ManagementAddressDomain (str): Sets the MP management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        - ManagementAddressDomainLength (number): Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        - ManagementAddressLength (number): Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        - MdLevel (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/mdLevel)): The MD level of the MP. The MD level must be previously configured.
        - MegId (str): The MEG identifier of the MP. This is for use with ITU-T Y.1731.
        - MegIdFormat (str(iccBasedFormat | primaryVid | characterString | 2octetInteger | rfc2685VpnId)): The MEG identifier format.
        - MepId (number): The MEP identifier.
        - MipId (number): The MIP identifier.
        - MpType (str(mip | mep)): Sets the MP type.
        - OrganizationSpecificTlvLength (number): Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        - OrganizationSpecificTlvValue (str): Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        - OverrideVlanPriority (bool): If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        - Rdi (str(auto | on | off)): The Remote Defect Identification.
        - ShortMaName (str): Sets the Short MA name. The format is determined in shortMaNameFormat. This is used with IEEE 802.1ag.
        - ShortMaNameFormat (str(primaryVid | characterString | 2octetInteger | rfc2685VpnId)): Sets the Short MA Name format.
        - TstEnableUnicastMac (bool): NOT DEFINED
        - TstIncrPacketLength (bool): NOT DEFINED
        - TstIncrPacketLengthStep (number): NOT DEFINED
        - TstInitialPatternValue (number): NOT DEFINED
        - TstInterval (number): NOT DEFINED
        - TstMode (str(start | stop)): NOT DEFINED
        - TstOverwriteSequenceNumber (bool): NOT DEFINED
        - TstPacketLength (number): NOT DEFINED
        - TstPatternType (str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32)): NOT DEFINED
        - TstPriority (number): NOT DEFINED
        - TstSequenceNumber (number): NOT DEFINED
        - TstTestType (str(inService | outOfService)): NOT DEFINED
        - TstUnicastMac (str): NOT DEFINED
        - Ttl (number): Sets the MP Time-to-live value. Default is 64. Min: 1 Max: 255
        - Vlan (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/vlans)): Assigns a VLAN to the MP. The VLAN must be previously configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AddCcmCustomTlvs=None,
        AddDataTlv=None,
        AddInterfaceStatusTlv=None,
        AddLbmCustomTlvs=None,
        AddLbrCustomTlvs=None,
        AddLmmCustomTlvs=None,
        AddLmrCustomTlvs=None,
        AddLtmCustomTlvs=None,
        AddLtrCustomTlvs=None,
        AddOrganizationSpecificTlv=None,
        AddPortStatusTlv=None,
        AddSenderIdTlv=None,
        AisEnableUnicastMac=None,
        AisInterval=None,
        AisMode=None,
        AisPriority=None,
        AisUnicastMac=None,
        AutoDmAllDestination=None,
        AutoDmDestination=None,
        AutoDmIteration=None,
        AutoDmTimeout=None,
        AutoDmTimer=None,
        AutoLbAllDestination=None,
        AutoLbDestination=None,
        AutoLbIteration=None,
        AutoLbTimeout=None,
        AutoLbTimer=None,
        AutoLmIteration=None,
        AutoLmTimeout=None,
        AutoLmTimer=None,
        AutoLtAllDestination=None,
        AutoLtDestination=None,
        AutoLtIteration=None,
        AutoLtTimeout=None,
        AutoLtTimer=None,
        CciInterval=None,
        CcmLmmTxFcf=None,
        CcmLmmTxFcfStep=None,
        CcmPriority=None,
        CcmRxFcb=None,
        CcmRxFcbStep=None,
        ChassisId=None,
        ChassisIdLength=None,
        ChassisIdSubType=None,
        DataTlvLength=None,
        DataTlvValue=None,
        DmMethod=None,
        DmPriority=None,
        DmmPriority=None,
        EnableAisRx=None,
        EnableAutoDm=None,
        EnableAutoLb=None,
        EnableAutoLm=None,
        EnableAutoLt=None,
        EnableLckRx=None,
        EnableLmCounterUpdate=None,
        EnableTstRx=None,
        Enabled=None,
        InterRemoteMepRxIncrementStep=None,
        InterRemoteMepTxIncrementStep=None,
        LbmPriority=None,
        LckEnableUnicastMac=None,
        LckInterval=None,
        LckMode=None,
        LckPriority=None,
        LckSupportAisGeneration=None,
        LckUnicastMac=None,
        LmAllRemoteMeps=None,
        LmDestinationMacAddress=None,
        LmMethod=None,
        LmmPriority=None,
        LmrPriority=None,
        LmrRxFcf=None,
        LmrRxFcfStep=None,
        LtmPriority=None,
        MacAddress=None,
        ManagementAddress=None,
        ManagementAddressDomain=None,
        ManagementAddressDomainLength=None,
        ManagementAddressLength=None,
        MdLevel=None,
        MegId=None,
        MegIdFormat=None,
        MepId=None,
        MipId=None,
        MpType=None,
        OrganizationSpecificTlvLength=None,
        OrganizationSpecificTlvValue=None,
        OverrideVlanPriority=None,
        Rdi=None,
        ShortMaName=None,
        ShortMaNameFormat=None,
        TstEnableUnicastMac=None,
        TstIncrPacketLength=None,
        TstIncrPacketLengthStep=None,
        TstInitialPatternValue=None,
        TstInterval=None,
        TstMode=None,
        TstOverwriteSequenceNumber=None,
        TstPacketLength=None,
        TstPatternType=None,
        TstPriority=None,
        TstSequenceNumber=None,
        TstTestType=None,
        TstUnicastMac=None,
        Ttl=None,
        Vlan=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, bool, str, int, int, int, bool, str, int, int, int, int, int, int, bool, str, int, int, int, str, int, int, int, int, int, str, int, str, int, str, str, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, bool, str, str, int, bool, str, bool, str, str, int, int, int, int, int, str, str, str, int, int, str, str, str, int, int, str, int, str, bool, str, str, str, bool, bool, int, int, int, str, bool, int, str, int, int, str, str, int, str) -> Mp
        """Adds a new mp resource on the server and adds it to the container.

        Args
        ----
        - AddCcmCustomTlvs (bool): If true, adds a custom CCM TLV to bridge messages.
        - AddDataTlv (bool): If true, adds a data TLV to bridge messages.
        - AddInterfaceStatusTlv (bool): If true, adds an interface status TLV to bridge messages.
        - AddLbmCustomTlvs (bool): If true, adds a custom loopback message TLV to bridge messages.
        - AddLbrCustomTlvs (bool): If true, adds a custom loopback response message TLV to bridge messages.
        - AddLmmCustomTlvs (bool): NOT DEFINED
        - AddLmrCustomTlvs (bool): NOT DEFINED
        - AddLtmCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddLtrCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddOrganizationSpecificTlv (bool): If true, adds a custom organization specific message TLV to bridge messages.
        - AddPortStatusTlv (bool): If true, adds a custom port statust message TLV to bridge messages.
        - AddSenderIdTlv (bool): If true, adds a custom sender ID message TLV to bridge messages.
        - AisEnableUnicastMac (bool): NOT DEFINED
        - AisInterval (str(oneSec | oneMin)): NOT DEFINED
        - AisMode (str(auto | start | stop)): NOT DEFINED
        - AisPriority (number): NOT DEFINED
        - AisUnicastMac (str): NOT DEFINED
        - AutoDmAllDestination (bool): If true, enables the automatic sending of DM Messages.
        - AutoDmDestination (str): The sent MAC address for the DM, if autoDmAllDestination is set to true.
        - AutoDmIteration (number): The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoDmTimeout (number): The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        - AutoDmTimer (number): The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        - AutoLbAllDestination (bool): If true, enables the automatic sending of Loopback Messages.
        - AutoLbDestination (str): Sets the loopback destination MAC address.
        - AutoLbIteration (number): The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLbTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLbTimer (number): The time period in seconds between LBMs. Default is 60. Min: 1 Max: 65535
        - AutoLmIteration (number): NOT DEFINED
        - AutoLmTimeout (number): NOT DEFINED
        - AutoLmTimer (number): NOT DEFINED
        - AutoLtAllDestination (bool): If true, enables the automatic sending to Link Trace Messages.
        - AutoLtDestination (str): Sets the link trance destination MAC address.
        - AutoLtIteration (number): The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLtTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLtTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - CciInterval (str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min)): Sets the Continuity Check Interval (CCI).
        - CcmLmmTxFcf (number): NOT DEFINED
        - CcmLmmTxFcfStep (number): NOT DEFINED
        - CcmPriority (number): Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        - CcmRxFcb (number): NOT DEFINED
        - CcmRxFcbStep (number): NOT DEFINED
        - ChassisId (str): Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        - ChassisIdLength (number): Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        - ChassisIdSubType (str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned)): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        - DataTlvLength (number): Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        - DataTlvValue (str): This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        - DmMethod (str(twoWay | oneWay)): The type of Delay Measurment support.
        - DmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Methodfor each MIP). The default is 0.
        - DmmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        - EnableAisRx (bool): NOT DEFINED
        - EnableAutoDm (bool): If true, enables the automatic sending of DM Messages.
        - EnableAutoLb (bool): If true, enables the automatic sending of Loopback messages.
        - EnableAutoLm (bool): NOT DEFINED
        - EnableAutoLt (bool): If true, enables the automatic sending of Link Trace messages.
        - EnableLckRx (bool): NOT DEFINED
        - EnableLmCounterUpdate (bool): NOT DEFINED
        - EnableTstRx (bool): NOT DEFINED
        - Enabled (bool): If true, the MP is enabled.
        - InterRemoteMepRxIncrementStep (number): NOT DEFINED
        - InterRemoteMepTxIncrementStep (number): NOT DEFINED
        - LbmPriority (number): Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        - LckEnableUnicastMac (bool): NOT DEFINED
        - LckInterval (str(oneSec | oneMin)): NOT DEFINED
        - LckMode (str(auto | start | stop)): NOT DEFINED
        - LckPriority (number): NOT DEFINED
        - LckSupportAisGeneration (bool): NOT DEFINED
        - LckUnicastMac (str): NOT DEFINED
        - LmAllRemoteMeps (bool): NOT DEFINED
        - LmDestinationMacAddress (str): NOT DEFINED
        - LmMethod (str(singleEnded | dualEnded)): NOT DEFINED
        - LmmPriority (number): NOT DEFINED
        - LmrPriority (number): NOT DEFINED
        - LmrRxFcf (number): NOT DEFINED
        - LmrRxFcfStep (number): NOT DEFINED
        - LtmPriority (number): Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        - MacAddress (str): The MAC address of the MP.
        - ManagementAddress (str): Sets the MP management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        - ManagementAddressDomain (str): Sets the MP management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        - ManagementAddressDomainLength (number): Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        - ManagementAddressLength (number): Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        - MdLevel (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/mdLevel)): The MD level of the MP. The MD level must be previously configured.
        - MegId (str): The MEG identifier of the MP. This is for use with ITU-T Y.1731.
        - MegIdFormat (str(iccBasedFormat | primaryVid | characterString | 2octetInteger | rfc2685VpnId)): The MEG identifier format.
        - MepId (number): The MEP identifier.
        - MipId (number): The MIP identifier.
        - MpType (str(mip | mep)): Sets the MP type.
        - OrganizationSpecificTlvLength (number): Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        - OrganizationSpecificTlvValue (str): Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        - OverrideVlanPriority (bool): If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        - Rdi (str(auto | on | off)): The Remote Defect Identification.
        - ShortMaName (str): Sets the Short MA name. The format is determined in shortMaNameFormat. This is used with IEEE 802.1ag.
        - ShortMaNameFormat (str(primaryVid | characterString | 2octetInteger | rfc2685VpnId)): Sets the Short MA Name format.
        - TstEnableUnicastMac (bool): NOT DEFINED
        - TstIncrPacketLength (bool): NOT DEFINED
        - TstIncrPacketLengthStep (number): NOT DEFINED
        - TstInitialPatternValue (number): NOT DEFINED
        - TstInterval (number): NOT DEFINED
        - TstMode (str(start | stop)): NOT DEFINED
        - TstOverwriteSequenceNumber (bool): NOT DEFINED
        - TstPacketLength (number): NOT DEFINED
        - TstPatternType (str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32)): NOT DEFINED
        - TstPriority (number): NOT DEFINED
        - TstSequenceNumber (number): NOT DEFINED
        - TstTestType (str(inService | outOfService)): NOT DEFINED
        - TstUnicastMac (str): NOT DEFINED
        - Ttl (number): Sets the MP Time-to-live value. Default is 64. Min: 1 Max: 255
        - Vlan (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/vlans)): Assigns a VLAN to the MP. The VLAN must be previously configured.

        Returns
        -------
        - self: This instance with all currently retrieved mp resources using find and the newly added mp resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mp resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AddCcmCustomTlvs=None,
        AddDataTlv=None,
        AddInterfaceStatusTlv=None,
        AddLbmCustomTlvs=None,
        AddLbrCustomTlvs=None,
        AddLmmCustomTlvs=None,
        AddLmrCustomTlvs=None,
        AddLtmCustomTlvs=None,
        AddLtrCustomTlvs=None,
        AddOrganizationSpecificTlv=None,
        AddPortStatusTlv=None,
        AddSenderIdTlv=None,
        AisEnableUnicastMac=None,
        AisInterval=None,
        AisMode=None,
        AisPriority=None,
        AisUnicastMac=None,
        AutoDmAllDestination=None,
        AutoDmDestination=None,
        AutoDmIteration=None,
        AutoDmTimeout=None,
        AutoDmTimer=None,
        AutoLbAllDestination=None,
        AutoLbDestination=None,
        AutoLbIteration=None,
        AutoLbTimeout=None,
        AutoLbTimer=None,
        AutoLmIteration=None,
        AutoLmTimeout=None,
        AutoLmTimer=None,
        AutoLtAllDestination=None,
        AutoLtDestination=None,
        AutoLtIteration=None,
        AutoLtTimeout=None,
        AutoLtTimer=None,
        CciInterval=None,
        CcmLmmTxFcf=None,
        CcmLmmTxFcfStep=None,
        CcmPriority=None,
        CcmRxFcb=None,
        CcmRxFcbStep=None,
        ChassisId=None,
        ChassisIdLength=None,
        ChassisIdSubType=None,
        DataTlvLength=None,
        DataTlvValue=None,
        DmMethod=None,
        DmPriority=None,
        DmmPriority=None,
        EnableAisRx=None,
        EnableAutoDm=None,
        EnableAutoLb=None,
        EnableAutoLm=None,
        EnableAutoLt=None,
        EnableLckRx=None,
        EnableLmCounterUpdate=None,
        EnableTstRx=None,
        Enabled=None,
        InterRemoteMepRxIncrementStep=None,
        InterRemoteMepTxIncrementStep=None,
        LbmPriority=None,
        LckEnableUnicastMac=None,
        LckInterval=None,
        LckMode=None,
        LckPriority=None,
        LckSupportAisGeneration=None,
        LckUnicastMac=None,
        LmAllRemoteMeps=None,
        LmDestinationMacAddress=None,
        LmMethod=None,
        LmmPriority=None,
        LmrPriority=None,
        LmrRxFcf=None,
        LmrRxFcfStep=None,
        LtmPriority=None,
        MacAddress=None,
        ManagementAddress=None,
        ManagementAddressDomain=None,
        ManagementAddressDomainLength=None,
        ManagementAddressLength=None,
        MdLevel=None,
        MegId=None,
        MegIdFormat=None,
        MepId=None,
        MipId=None,
        MpType=None,
        OrganizationSpecificTlvLength=None,
        OrganizationSpecificTlvValue=None,
        OverrideVlanPriority=None,
        Rdi=None,
        ShortMaName=None,
        ShortMaNameFormat=None,
        TstEnableUnicastMac=None,
        TstIncrPacketLength=None,
        TstIncrPacketLengthStep=None,
        TstInitialPatternValue=None,
        TstInterval=None,
        TstMode=None,
        TstOverwriteSequenceNumber=None,
        TstPacketLength=None,
        TstPatternType=None,
        TstPriority=None,
        TstSequenceNumber=None,
        TstTestType=None,
        TstUnicastMac=None,
        Ttl=None,
        Vlan=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, bool, str, int, int, int, bool, str, int, int, int, int, int, int, bool, str, int, int, int, str, int, int, int, int, int, str, int, str, int, str, str, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, bool, str, str, int, bool, str, bool, str, str, int, int, int, int, int, str, str, str, int, int, str, str, str, int, int, str, int, str, bool, str, str, str, bool, bool, int, int, int, str, bool, int, str, int, int, str, str, int, str) -> Mp
        """Finds and retrieves mp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mp resources from the server.

        Args
        ----
        - AddCcmCustomTlvs (bool): If true, adds a custom CCM TLV to bridge messages.
        - AddDataTlv (bool): If true, adds a data TLV to bridge messages.
        - AddInterfaceStatusTlv (bool): If true, adds an interface status TLV to bridge messages.
        - AddLbmCustomTlvs (bool): If true, adds a custom loopback message TLV to bridge messages.
        - AddLbrCustomTlvs (bool): If true, adds a custom loopback response message TLV to bridge messages.
        - AddLmmCustomTlvs (bool): NOT DEFINED
        - AddLmrCustomTlvs (bool): NOT DEFINED
        - AddLtmCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddLtrCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddOrganizationSpecificTlv (bool): If true, adds a custom organization specific message TLV to bridge messages.
        - AddPortStatusTlv (bool): If true, adds a custom port statust message TLV to bridge messages.
        - AddSenderIdTlv (bool): If true, adds a custom sender ID message TLV to bridge messages.
        - AisEnableUnicastMac (bool): NOT DEFINED
        - AisInterval (str(oneSec | oneMin)): NOT DEFINED
        - AisMode (str(auto | start | stop)): NOT DEFINED
        - AisPriority (number): NOT DEFINED
        - AisUnicastMac (str): NOT DEFINED
        - AutoDmAllDestination (bool): If true, enables the automatic sending of DM Messages.
        - AutoDmDestination (str): The sent MAC address for the DM, if autoDmAllDestination is set to true.
        - AutoDmIteration (number): The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoDmTimeout (number): The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        - AutoDmTimer (number): The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        - AutoLbAllDestination (bool): If true, enables the automatic sending of Loopback Messages.
        - AutoLbDestination (str): Sets the loopback destination MAC address.
        - AutoLbIteration (number): The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLbTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLbTimer (number): The time period in seconds between LBMs. Default is 60. Min: 1 Max: 65535
        - AutoLmIteration (number): NOT DEFINED
        - AutoLmTimeout (number): NOT DEFINED
        - AutoLmTimer (number): NOT DEFINED
        - AutoLtAllDestination (bool): If true, enables the automatic sending to Link Trace Messages.
        - AutoLtDestination (str): Sets the link trance destination MAC address.
        - AutoLtIteration (number): The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLtTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLtTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - CciInterval (str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min)): Sets the Continuity Check Interval (CCI).
        - CcmLmmTxFcf (number): NOT DEFINED
        - CcmLmmTxFcfStep (number): NOT DEFINED
        - CcmPriority (number): Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        - CcmRxFcb (number): NOT DEFINED
        - CcmRxFcbStep (number): NOT DEFINED
        - ChassisId (str): Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        - ChassisIdLength (number): Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        - ChassisIdSubType (str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned)): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        - DataTlvLength (number): Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        - DataTlvValue (str): This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        - DmMethod (str(twoWay | oneWay)): The type of Delay Measurment support.
        - DmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Methodfor each MIP). The default is 0.
        - DmmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        - EnableAisRx (bool): NOT DEFINED
        - EnableAutoDm (bool): If true, enables the automatic sending of DM Messages.
        - EnableAutoLb (bool): If true, enables the automatic sending of Loopback messages.
        - EnableAutoLm (bool): NOT DEFINED
        - EnableAutoLt (bool): If true, enables the automatic sending of Link Trace messages.
        - EnableLckRx (bool): NOT DEFINED
        - EnableLmCounterUpdate (bool): NOT DEFINED
        - EnableTstRx (bool): NOT DEFINED
        - Enabled (bool): If true, the MP is enabled.
        - InterRemoteMepRxIncrementStep (number): NOT DEFINED
        - InterRemoteMepTxIncrementStep (number): NOT DEFINED
        - LbmPriority (number): Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        - LckEnableUnicastMac (bool): NOT DEFINED
        - LckInterval (str(oneSec | oneMin)): NOT DEFINED
        - LckMode (str(auto | start | stop)): NOT DEFINED
        - LckPriority (number): NOT DEFINED
        - LckSupportAisGeneration (bool): NOT DEFINED
        - LckUnicastMac (str): NOT DEFINED
        - LmAllRemoteMeps (bool): NOT DEFINED
        - LmDestinationMacAddress (str): NOT DEFINED
        - LmMethod (str(singleEnded | dualEnded)): NOT DEFINED
        - LmmPriority (number): NOT DEFINED
        - LmrPriority (number): NOT DEFINED
        - LmrRxFcf (number): NOT DEFINED
        - LmrRxFcfStep (number): NOT DEFINED
        - LtmPriority (number): Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        - MacAddress (str): The MAC address of the MP.
        - ManagementAddress (str): Sets the MP management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        - ManagementAddressDomain (str): Sets the MP management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        - ManagementAddressDomainLength (number): Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        - ManagementAddressLength (number): Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        - MdLevel (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/mdLevel)): The MD level of the MP. The MD level must be previously configured.
        - MegId (str): The MEG identifier of the MP. This is for use with ITU-T Y.1731.
        - MegIdFormat (str(iccBasedFormat | primaryVid | characterString | 2octetInteger | rfc2685VpnId)): The MEG identifier format.
        - MepId (number): The MEP identifier.
        - MipId (number): The MIP identifier.
        - MpType (str(mip | mep)): Sets the MP type.
        - OrganizationSpecificTlvLength (number): Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        - OrganizationSpecificTlvValue (str): Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        - OverrideVlanPriority (bool): If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        - Rdi (str(auto | on | off)): The Remote Defect Identification.
        - ShortMaName (str): Sets the Short MA name. The format is determined in shortMaNameFormat. This is used with IEEE 802.1ag.
        - ShortMaNameFormat (str(primaryVid | characterString | 2octetInteger | rfc2685VpnId)): Sets the Short MA Name format.
        - TstEnableUnicastMac (bool): NOT DEFINED
        - TstIncrPacketLength (bool): NOT DEFINED
        - TstIncrPacketLengthStep (number): NOT DEFINED
        - TstInitialPatternValue (number): NOT DEFINED
        - TstInterval (number): NOT DEFINED
        - TstMode (str(start | stop)): NOT DEFINED
        - TstOverwriteSequenceNumber (bool): NOT DEFINED
        - TstPacketLength (number): NOT DEFINED
        - TstPatternType (str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32)): NOT DEFINED
        - TstPriority (number): NOT DEFINED
        - TstSequenceNumber (number): NOT DEFINED
        - TstTestType (str(inService | outOfService)): NOT DEFINED
        - TstUnicastMac (str): NOT DEFINED
        - Ttl (number): Sets the MP Time-to-live value. Default is 64. Min: 1 Max: 255
        - Vlan (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/cfm/bridge/vlans)): Assigns a VLAN to the MP. The VLAN must be previously configured.

        Returns
        -------
        - self: This instance with matching mp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
