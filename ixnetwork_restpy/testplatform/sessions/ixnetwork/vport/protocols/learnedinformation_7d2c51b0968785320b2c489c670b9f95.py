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


class LearnedInformation(Base):
    """This object displays the information learned from each router.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "learnedInformation"
    _SDM_ATT_MAP = {
        "AlarmTrigger": "alarmTrigger",
        "AlarmType": "alarmType",
        "ApsTriggerType": "apsTriggerType",
        "CccvPauseTriggerOption": "cccvPauseTriggerOption",
        "CccvResumeTriggerOption": "cccvResumeTriggerOption",
        "ChangeSessionParameters": "changeSessionParameters",
        "ClearMisconnectivityDefect": "clearMisconnectivityDefect",
        "CounterType": "counterType",
        "DmInterval": "dmInterval",
        "DmIterations": "dmIterations",
        "DmMode": "dmMode",
        "DmPadLen": "dmPadLen",
        "DmRequestPaddedReply": "dmRequestPaddedReply",
        "DmTimeFormat": "dmTimeFormat",
        "DmTrafficClass": "dmTrafficClass",
        "DmType": "dmType",
        "EnableAlarm": "enableAlarm",
        "EnableAlarmAis": "enableAlarmAis",
        "EnableAlarmFastClear": "enableAlarmFastClear",
        "EnableAlarmLck": "enableAlarmLck",
        "EnableAlarmSetLdi": "enableAlarmSetLdi",
        "EnableApsTrigger": "enableApsTrigger",
        "EnableCccvPause": "enableCccvPause",
        "EnableCccvResume": "enableCccvResume",
        "EnableDmTrigger": "enableDmTrigger",
        "EnableLmTrigger": "enableLmTrigger",
        "EnableLspPing": "enableLspPing",
        "EnableLspPingFecStackValidation": "enableLspPingFecStackValidation",
        "EnableLspPingValidateReversePath": "enableLspPingValidateReversePath",
        "EnableLspTraceRoute": "enableLspTraceRoute",
        "EnableLspTraceRouteFecStackValidation": "enableLspTraceRouteFecStackValidation",
        "EnablePwStatusClear": "enablePwStatusClear",
        "EnablePwStatusFault": "enablePwStatusFault",
        "IsDmLearnedInformationRefreshed": "isDmLearnedInformationRefreshed",
        "IsGeneralLearnedInformationRefreshed": "isGeneralLearnedInformationRefreshed",
        "IsLmLearnedInformationRefreshed": "isLmLearnedInformationRefreshed",
        "IsPingLearnedInformationRefreshed": "isPingLearnedInformationRefreshed",
        "IsTraceRouteLearnedInformationRefreshed": "isTraceRouteLearnedInformationRefreshed",
        "LastDmResponseTimeout": "lastDmResponseTimeout",
        "LastLmResponseTimeout": "lastLmResponseTimeout",
        "LmInitialRxValue": "lmInitialRxValue",
        "LmInitialTxValue": "lmInitialTxValue",
        "LmInterval": "lmInterval",
        "LmIterations": "lmIterations",
        "LmMode": "lmMode",
        "LmRxStep": "lmRxStep",
        "LmTrafficClass": "lmTrafficClass",
        "LmTxStep": "lmTxStep",
        "LmType": "lmType",
        "LspPingEncapsulationType": "lspPingEncapsulationType",
        "LspPingResponseTimeout": "lspPingResponseTimeout",
        "LspPingTtlValue": "lspPingTtlValue",
        "LspTraceRouteEncapsulationType": "lspTraceRouteEncapsulationType",
        "LspTraceRouteResponseTimeout": "lspTraceRouteResponseTimeout",
        "LspTraceRouteTtlLimit": "lspTraceRouteTtlLimit",
        "MinRxInterval": "minRxInterval",
        "MinTxInterval": "minTxInterval",
        "MisconnectivityDefect": "misconnectivityDefect",
        "MisconnectivityDefectOption": "misconnectivityDefectOption",
        "OnDemandCvDownstreamAddressType": "onDemandCvDownstreamAddressType",
        "OnDemandCvDownstreamIpAddress": "onDemandCvDownstreamIpAddress",
        "OnDemandCvDsIflag": "onDemandCvDsIflag",
        "OnDemandCvDsNflag": "onDemandCvDsNflag",
        "OnDemandCvEgressIfNumber": "onDemandCvEgressIfNumber",
        "OnDemandCvIncludeDestinationIdentifierTlv": "onDemandCvIncludeDestinationIdentifierTlv",
        "OnDemandCvIncludeDetailedDownstreamMappingTlv": "onDemandCvIncludeDetailedDownstreamMappingTlv",
        "OnDemandCvIncludeDownstreamMappingTlv": "onDemandCvIncludeDownstreamMappingTlv",
        "OnDemandCvIncludePadTlv": "onDemandCvIncludePadTlv",
        "OnDemandCvIncludeReplyTosByteTlv": "onDemandCvIncludeReplyTosByteTlv",
        "OnDemandCvIncludeSourceIdentifierTlv": "onDemandCvIncludeSourceIdentifierTlv",
        "OnDemandCvIngressIfNumber": "onDemandCvIngressIfNumber",
        "OnDemandCvNumberedDownstreamInterfaceAddress": "onDemandCvNumberedDownstreamInterfaceAddress",
        "OnDemandCvPadTlvFirstOctet": "onDemandCvPadTlvFirstOctet",
        "OnDemandCvPadTlvLength": "onDemandCvPadTlvLength",
        "OnDemandCvTosByte": "onDemandCvTosByte",
        "OnDemandCvUnnumberedDownstreamInterfaceAddress": "onDemandCvUnnumberedDownstreamInterfaceAddress",
        "Periodicity": "periodicity",
        "PwStatusClearLabelTtl": "pwStatusClearLabelTtl",
        "PwStatusClearTransmitInterval": "pwStatusClearTransmitInterval",
        "PwStatusCode": "pwStatusCode",
        "PwStatusFaultLabelTtl": "pwStatusFaultLabelTtl",
        "PwStatusFaultTransmitInterval": "pwStatusFaultTransmitInterval",
    }
    _SDM_ENUM_MAP = {
        "alarmTrigger": ["clear", "start"],
        "alarmType": ["ietf", "y1731"],
        "apsTriggerType": [
            "clear",
            "forcedSwitch",
            "manualSwitchToProtect",
            "manualSwitchToWorking",
            "lockout",
            "exercise",
            "freeze",
        ],
        "cccvPauseTriggerOption": ["tx", "rx", "txRx"],
        "cccvResumeTriggerOption": ["tx", "rx", "txRx"],
        "counterType": ["32Bit", "64Bit"],
        "dmMode": ["noResponseExpected", "responseExpected"],
        "dmTimeFormat": ["ieee", "ntp"],
        "dmType": ["ietf", "y1731"],
        "lmMode": ["responseExpected", "noResponseExpected"],
        "lmType": ["ietf", "y1731"],
        "lspPingEncapsulationType": ["GAch", "UDP over IP over GAch"],
        "lspTraceRouteEncapsulationType": ["GAch", "UDP over IP over GAch"],
        "minRxInterval": ["10", "100", "1000", "10000", "3.33", "60000", "600000"],
        "minTxInterval": ["10", "100", "1000", "10000", "3.33", "60000", "600000"],
        "misconnectivityDefectOption": [
            "unexpectedMepId",
            "unexpectedYourDiscriminator",
        ],
        "onDemandCvDownstreamAddressType": ["ipv4Numbered", "ipv4Unnumbered", "nonIp"],
        "onDemandCvPadTlvFirstOctet": ["drop", "copy"],
    }

    def __init__(self, parent, list_op=False):
        super(LearnedInformation, self).__init__(parent, list_op)

    @property
    def DmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dmlearnedinfo_4f43a9179cbbb274bfab560ae9dfbd66.DmLearnedInfo): An instance of the DmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dmlearnedinfo_4f43a9179cbbb274bfab560ae9dfbd66 import (
            DmLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DmLearnedInfo", None) is not None:
                return self._properties.get("DmLearnedInfo")
        return DmLearnedInfo(self)

    @property
    def GeneralLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_69b009fa3b0223c18c475044c80e0a8a.GeneralLearnedInfo): An instance of the GeneralLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_69b009fa3b0223c18c475044c80e0a8a import (
            GeneralLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GeneralLearnedInfo", None) is not None:
                return self._properties.get("GeneralLearnedInfo")
        return GeneralLearnedInfo(self)

    @property
    def LmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmlearnedinfo_82bda5fc632e654980ce384194a117b8.LmLearnedInfo): An instance of the LmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmlearnedinfo_82bda5fc632e654980ce384194a117b8 import (
            LmLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LmLearnedInfo", None) is not None:
                return self._properties.get("LmLearnedInfo")
        return LmLearnedInfo(self)

    @property
    def PingLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pinglearnedinfo_7cfde3bc969579781fc43365d9e4e20c.PingLearnedInfo): An instance of the PingLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pinglearnedinfo_7cfde3bc969579781fc43365d9e4e20c import (
            PingLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PingLearnedInfo", None) is not None:
                return self._properties.get("PingLearnedInfo")
        return PingLearnedInfo(self)

    @property
    def TraceRouteLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.traceroutelearnedinfo_d3fe51085725a1f70fdb83bc1f0780d7.TraceRouteLearnedInfo): An instance of the TraceRouteLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.traceroutelearnedinfo_d3fe51085725a1f70fdb83bc1f0780d7 import (
            TraceRouteLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TraceRouteLearnedInfo", None) is not None:
                return self._properties.get("TraceRouteLearnedInfo")
        return TraceRouteLearnedInfo(self)

    @property
    def AlarmTrigger(self):
        # type: () -> str
        """
        Returns
        -------
        - str(clear | start): This signifies the alarm trigger. Possible values include Clear and Start.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlarmTrigger"])

    @AlarmTrigger.setter
    def AlarmTrigger(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlarmTrigger"], value)

    @property
    def AlarmType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ietf | y1731): This signifies the alarm type. Possible values include IETF and Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlarmType"])

    @AlarmType.setter
    def AlarmType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlarmType"], value)

    @property
    def ApsTriggerType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(clear | forcedSwitch | manualSwitchToProtect | manualSwitchToWorking | lockout | exercise | freeze): This signifies the Trigger type. Possible values include Clear, Exercise, Forced Switch, Freeze, Lockout, Manual Switch To Protect and Manual Switch To Working.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsTriggerType"])

    @ApsTriggerType.setter
    def ApsTriggerType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApsTriggerType"], value)

    @property
    def CccvPauseTriggerOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tx | rx | txRx): This signifies the cccv pause trigger option. Possible values include TX, RX and TXRX.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CccvPauseTriggerOption"])

    @CccvPauseTriggerOption.setter
    def CccvPauseTriggerOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CccvPauseTriggerOption"], value)

    @property
    def CccvResumeTriggerOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tx | rx | txRx): This signifies the cccv resume trigger option. Possible values include Tx, Rx and TxRx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CccvResumeTriggerOption"])

    @CccvResumeTriggerOption.setter
    def CccvResumeTriggerOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CccvResumeTriggerOption"], value)

    @property
    def ChangeSessionParameters(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This specifies the minimum receive interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChangeSessionParameters"])

    @ChangeSessionParameters.setter
    def ChangeSessionParameters(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChangeSessionParameters"], value)

    @property
    def ClearMisconnectivityDefect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If set true all the misconnectivity defects that have been triggered earlier with any type gets cleared.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClearMisconnectivityDefect"])

    @ClearMisconnectivityDefect.setter
    def ClearMisconnectivityDefect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClearMisconnectivityDefect"], value)

    @property
    def CounterType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(32Bit | 64Bit): This signifies the LM Counter Type. Possible values include 32 Bit (default) and 64 Bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CounterType"])

    @CounterType.setter
    def CounterType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CounterType"], value)

    @property
    def DmInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the DM interval in milliseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmInterval"])

    @DmInterval.setter
    def DmInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmInterval"], value)

    @property
    def DmIterations(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the total number of DM queries to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmIterations"])

    @DmIterations.setter
    def DmIterations(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmIterations"], value)

    @property
    def DmMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noResponseExpected | responseExpected): This signifies the DM mode. The possible values include Response Expected and No Response Expected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmMode"])

    @DmMode.setter
    def DmMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmMode"], value)

    @property
    def DmPadLen(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the DM pad length.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmPadLen"])

    @DmPadLen.setter
    def DmPadLen(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmPadLen"], value)

    @property
    def DmRequestPaddedReply(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the DM request as a padded reply.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmRequestPaddedReply"])

    @DmRequestPaddedReply.setter
    def DmRequestPaddedReply(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmRequestPaddedReply"], value)

    @property
    def DmTimeFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ieee | ntp): This signifies the DM time format. The possible values include IEEE and NTP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmTimeFormat"])

    @DmTimeFormat.setter
    def DmTimeFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmTimeFormat"], value)

    @property
    def DmTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the DM traffic class value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmTrafficClass"])

    @DmTrafficClass.setter
    def DmTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmTrafficClass"], value)

    @property
    def DmType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ietf | y1731): This signifies the DM Type. Possible values include IETF and Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmType"])

    @DmType.setter
    def DmType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmType"], value)

    @property
    def EnableAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the Alarm and the fields under it.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAlarm"])

    @EnableAlarm.setter
    def EnableAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAlarm"], value)

    @property
    def EnableAlarmAis(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: This signifies the enablement of the Alarm AIS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAlarmAis"])

    @EnableAlarmAis.setter
    def EnableAlarmAis(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAlarmAis"], value)

    @property
    def EnableAlarmFastClear(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Clears the Alarm State in 10 seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAlarmFastClear"])

    @EnableAlarmFastClear.setter
    def EnableAlarmFastClear(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAlarmFastClear"], value)

    @property
    def EnableAlarmLck(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the Alarm lck.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAlarmLck"])

    @EnableAlarmLck.setter
    def EnableAlarmLck(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAlarmLck"], value)

    @property
    def EnableAlarmSetLdi(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the Alarm Set LDI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAlarmSetLdi"])

    @EnableAlarmSetLdi.setter
    def EnableAlarmSetLdi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAlarmSetLdi"], value)

    @property
    def EnableApsTrigger(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of APS trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableApsTrigger"])

    @EnableApsTrigger.setter
    def EnableApsTrigger(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableApsTrigger"], value)

    @property
    def EnableCccvPause(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enabling of CCCV Pause.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCccvPause"])

    @EnableCccvPause.setter
    def EnableCccvPause(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCccvPause"], value)

    @property
    def EnableCccvResume(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of CCCV Resume.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCccvResume"])

    @EnableCccvResume.setter
    def EnableCccvResume(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCccvResume"], value)

    @property
    def EnableDmTrigger(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the DM trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDmTrigger"])

    @EnableDmTrigger.setter
    def EnableDmTrigger(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDmTrigger"], value)

    @property
    def EnableLmTrigger(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the LM trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLmTrigger"])

    @EnableLmTrigger.setter
    def EnableLmTrigger(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLmTrigger"], value)

    @property
    def EnableLspPing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the LSP Ping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLspPing"])

    @EnableLspPing.setter
    def EnableLspPing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLspPing"], value)

    @property
    def EnableLspPingFecStackValidation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the FEC Stack Validation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLspPingFecStackValidation"])

    @EnableLspPingFecStackValidation.setter
    def EnableLspPingFecStackValidation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLspPingFecStackValidation"], value)

    @property
    def EnableLspPingValidateReversePath(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true validate reverse path bit is set in lsp ping message.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableLspPingValidateReversePath"]
        )

    @EnableLspPingValidateReversePath.setter
    def EnableLspPingValidateReversePath(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableLspPingValidateReversePath"], value
        )

    @property
    def EnableLspTraceRoute(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the lsp traceroute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLspTraceRoute"])

    @EnableLspTraceRoute.setter
    def EnableLspTraceRoute(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLspTraceRoute"], value)

    @property
    def EnableLspTraceRouteFecStackValidation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the FEC Stack Validation.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableLspTraceRouteFecStackValidation"]
        )

    @EnableLspTraceRouteFecStackValidation.setter
    def EnableLspTraceRouteFecStackValidation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableLspTraceRouteFecStackValidation"], value
        )

    @property
    def EnablePwStatusClear(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the PW Status Clear and the fields under it.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePwStatusClear"])

    @EnablePwStatusClear.setter
    def EnablePwStatusClear(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePwStatusClear"], value)

    @property
    def EnablePwStatusFault(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the PW Status Fault.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePwStatusFault"])

    @EnablePwStatusFault.setter
    def EnablePwStatusFault(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePwStatusFault"], value)

    @property
    def IsDmLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the refresheing of the DM learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsDmLearnedInformationRefreshed"])

    @property
    def IsGeneralLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the refereshing of the general learned information.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsGeneralLearnedInformationRefreshed"]
        )

    @property
    def IsLmLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the refresheing of the LM learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLmLearnedInformationRefreshed"])

    @property
    def IsPingLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the refresheing of the Ping learned information.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsPingLearnedInformationRefreshed"]
        )

    @property
    def IsTraceRouteLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the refresheing of the Trace Route learned information.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsTraceRouteLearnedInformationRefreshed"]
        )

    @property
    def LastDmResponseTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the last DM Response Timeout.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastDmResponseTimeout"])

    @LastDmResponseTimeout.setter
    def LastDmResponseTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LastDmResponseTimeout"], value)

    @property
    def LastLmResponseTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the last LM response timeout.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastLmResponseTimeout"])

    @LastLmResponseTimeout.setter
    def LastLmResponseTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LastLmResponseTimeout"], value)

    @property
    def LmInitialRxValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Initial Rx value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmInitialRxValue"])

    @LmInitialRxValue.setter
    def LmInitialRxValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmInitialRxValue"], value)

    @property
    def LmInitialTxValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Initial Tx value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmInitialTxValue"])

    @LmInitialTxValue.setter
    def LmInitialTxValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmInitialTxValue"], value)

    @property
    def LmInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM interval in milliseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmInterval"])

    @LmInterval.setter
    def LmInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmInterval"], value)

    @property
    def LmIterations(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of LM queries to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmIterations"])

    @LmIterations.setter
    def LmIterations(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmIterations"], value)

    @property
    def LmMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(responseExpected | noResponseExpected): This signifies the LM mode. Possible values include Response Expected and No Response Expected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmMode"])

    @LmMode.setter
    def LmMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmMode"], value)

    @property
    def LmRxStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Rx step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmRxStep"])

    @LmRxStep.setter
    def LmRxStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmRxStep"], value)

    @property
    def LmTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Traffic Class.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmTrafficClass"])

    @LmTrafficClass.setter
    def LmTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmTrafficClass"], value)

    @property
    def LmTxStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Tx Step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmTxStep"])

    @LmTxStep.setter
    def LmTxStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmTxStep"], value)

    @property
    def LmType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ietf | y1731): This signifies the LM type. The possible values include IETF and Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmType"])

    @LmType.setter
    def LmType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmType"], value)

    @property
    def LspPingEncapsulationType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(GAch | UDP over IP over GAch): This signifies the encapsulation type with which the lsp ping request message will be sent out. The possible values include UDP-IP-GAch and GAch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspPingEncapsulationType"])

    @LspPingEncapsulationType.setter
    def LspPingEncapsulationType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspPingEncapsulationType"], value)

    @property
    def LspPingResponseTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the response timeout in milliseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspPingResponseTimeout"])

    @LspPingResponseTimeout.setter
    def LspPingResponseTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspPingResponseTimeout"], value)

    @property
    def LspPingTtlValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LSP Ping Ttl value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspPingTtlValue"])

    @LspPingTtlValue.setter
    def LspPingTtlValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspPingTtlValue"], value)

    @property
    def LspTraceRouteEncapsulationType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(GAch | UDP over IP over GAch): This signifies the encapsulation type with which the Trace route request message will be sen out. The possible values include UDP-IP-GAch and GAch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspTraceRouteEncapsulationType"])

    @LspTraceRouteEncapsulationType.setter
    def LspTraceRouteEncapsulationType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspTraceRouteEncapsulationType"], value)

    @property
    def LspTraceRouteResponseTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the response timeout in milliseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspTraceRouteResponseTimeout"])

    @LspTraceRouteResponseTimeout.setter
    def LspTraceRouteResponseTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspTraceRouteResponseTimeout"], value)

    @property
    def LspTraceRouteTtlLimit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the max TTL till which the Echo Request will be sent out as part of trace route process.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspTraceRouteTtlLimit"])

    @LspTraceRouteTtlLimit.setter
    def LspTraceRouteTtlLimit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspTraceRouteTtlLimit"], value)

    @property
    def MinRxInterval(self):
        # type: () -> str
        """
        Returns
        -------
        - str(10 | 100 | 1000 | 10000 | 3.33 | 60000 | 600000): This signifies the minimum receive interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRxInterval"])

    @MinRxInterval.setter
    def MinRxInterval(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRxInterval"], value)

    @property
    def MinTxInterval(self):
        # type: () -> str
        """
        Returns
        -------
        - str(10 | 100 | 1000 | 10000 | 3.33 | 60000 | 600000): This signifies the learned information minimum transmit interval, in milliseconds. This specifies the minimum transmit interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinTxInterval"])

    @MinTxInterval.setter
    def MinTxInterval(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinTxInterval"], value)

    @property
    def MisconnectivityDefect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: To enable misconnectivity defect on the fly by changing LSP/PW MEP/MEG Id parameter or Your Discriminator on the source side.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MisconnectivityDefect"])

    @MisconnectivityDefect.setter
    def MisconnectivityDefect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MisconnectivityDefect"], value)

    @property
    def MisconnectivityDefectOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unexpectedMepId | unexpectedYourDiscriminator): To enable misconnectivity defect on the fly by changing LSP/PW MEP/MEG Id parameter or Your Discriminator on the source side.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MisconnectivityDefectOption"])

    @MisconnectivityDefectOption.setter
    def MisconnectivityDefectOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MisconnectivityDefectOption"], value)

    @property
    def OnDemandCvDownstreamAddressType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4Numbered | ipv4Unnumbered | nonIp): This signifies the Address Type of the Downstream or Detailed Downstream Mapping TLV. This can be of three types.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvDownstreamAddressType"])

    @OnDemandCvDownstreamAddressType.setter
    def OnDemandCvDownstreamAddressType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvDownstreamAddressType"], value)

    @property
    def OnDemandCvDownstreamIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the inclusion of the IP address in Downstream or Detailed Downstream Mapping TLV. This takes input in ip address format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvDownstreamIpAddress"])

    @OnDemandCvDownstreamIpAddress.setter
    def OnDemandCvDownstreamIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvDownstreamIpAddress"], value)

    @property
    def OnDemandCvDsIflag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the setting of I bit in the DS Flag of Downstream or Detailed Downstream Mapping TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvDsIflag"])

    @OnDemandCvDsIflag.setter
    def OnDemandCvDsIflag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvDsIflag"], value)

    @property
    def OnDemandCvDsNflag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If set true, N bit is set in the DS Flag of Downstream or Detailed Downstream Mapping TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvDsNflag"])

    @OnDemandCvDsNflag.setter
    def OnDemandCvDsNflag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvDsNflag"], value)

    @property
    def OnDemandCvEgressIfNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Egress If Number, if address type of Downstream or Detailed Downstream Mapping TLV is set to nonIP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvEgressIfNumber"])

    @OnDemandCvEgressIfNumber.setter
    def OnDemandCvEgressIfNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvEgressIfNumber"], value)

    @property
    def OnDemandCvIncludeDestinationIdentifierTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If channel type is set to GAch, this signifies the inclusion of Destination Identifier TLV in the On Demand CV message. Possible values are true or false.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeDestinationIdentifierTlv"]
        )

    @OnDemandCvIncludeDestinationIdentifierTlv.setter
    def OnDemandCvIncludeDestinationIdentifierTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeDestinationIdentifierTlv"], value
        )

    @property
    def OnDemandCvIncludeDetailedDownstreamMappingTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the inclusion of the Detailed Downstream Mapping TLV in on demand cv message. Possible values are true or false.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeDetailedDownstreamMappingTlv"]
        )

    @OnDemandCvIncludeDetailedDownstreamMappingTlv.setter
    def OnDemandCvIncludeDetailedDownstreamMappingTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeDetailedDownstreamMappingTlv"], value
        )

    @property
    def OnDemandCvIncludeDownstreamMappingTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the inclusion of Downstream Mapping TLV in on demand cv messages.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeDownstreamMappingTlv"]
        )

    @OnDemandCvIncludeDownstreamMappingTlv.setter
    def OnDemandCvIncludeDownstreamMappingTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeDownstreamMappingTlv"], value
        )

    @property
    def OnDemandCvIncludePadTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the inclusion of Pad TLV in on demand cv messages (ping or traceroute).
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvIncludePadTlv"])

    @OnDemandCvIncludePadTlv.setter
    def OnDemandCvIncludePadTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvIncludePadTlv"], value)

    @property
    def OnDemandCvIncludeReplyTosByteTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the inclusion of Reply Tos Byte TLV in on demand cv messages, if channel type is configured ip-udp-gach.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeReplyTosByteTlv"]
        )

    @OnDemandCvIncludeReplyTosByteTlv.setter
    def OnDemandCvIncludeReplyTosByteTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeReplyTosByteTlv"], value
        )

    @property
    def OnDemandCvIncludeSourceIdentifierTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If channel type is set to GAch, this signifies the inclusion of Source Identifier TLV in the On Demand CV message. Possible values are true or false.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeSourceIdentifierTlv"]
        )

    @OnDemandCvIncludeSourceIdentifierTlv.setter
    def OnDemandCvIncludeSourceIdentifierTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["OnDemandCvIncludeSourceIdentifierTlv"], value
        )

    @property
    def OnDemandCvIngressIfNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Ingress If Number, if address type of Downstream or Detailed Downstream Mapping TLV is set to nonIP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvIngressIfNumber"])

    @OnDemandCvIngressIfNumber.setter
    def OnDemandCvIngressIfNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvIngressIfNumber"], value)

    @property
    def OnDemandCvNumberedDownstreamInterfaceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If the address type of Downstream Address TLV is set to ipv4Numbered, it signifies the numbered Interface Address. This takes value in ip address format.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["OnDemandCvNumberedDownstreamInterfaceAddress"]
        )

    @OnDemandCvNumberedDownstreamInterfaceAddress.setter
    def OnDemandCvNumberedDownstreamInterfaceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["OnDemandCvNumberedDownstreamInterfaceAddress"], value
        )

    @property
    def OnDemandCvPadTlvFirstOctet(self):
        # type: () -> str
        """
        Returns
        -------
        - str(drop | copy): This signifies the value of first octet of Pad TLV. The possible values are copy or drop.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvPadTlvFirstOctet"])

    @OnDemandCvPadTlvFirstOctet.setter
    def OnDemandCvPadTlvFirstOctet(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvPadTlvFirstOctet"], value)

    @property
    def OnDemandCvPadTlvLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the inclusion of Pad TLV length in On Demand CV message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvPadTlvLength"])

    @OnDemandCvPadTlvLength.setter
    def OnDemandCvPadTlvLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvPadTlvLength"], value)

    @property
    def OnDemandCvTosByte(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If channel type is set ip-udp-Gach, this signifies the value of Tos Byte field within Reply TOS Byte TLV, included in on demand cv messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvTosByte"])

    @OnDemandCvTosByte.setter
    def OnDemandCvTosByte(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvTosByte"], value)

    @property
    def OnDemandCvUnnumberedDownstreamInterfaceAddress(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If the address type of Downstream Address TLV is set to ipv4Unnumbered, this signifies the unnumbered Interface Address. This takes value in integer format. The max value can be 4294967295.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["OnDemandCvUnnumberedDownstreamInterfaceAddress"]
        )

    @OnDemandCvUnnumberedDownstreamInterfaceAddress.setter
    def OnDemandCvUnnumberedDownstreamInterfaceAddress(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["OnDemandCvUnnumberedDownstreamInterfaceAddress"], value
        )

    @property
    def Periodicity(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the periodicity of the alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Periodicity"])

    @Periodicity.setter
    def Periodicity(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Periodicity"], value)

    @property
    def PwStatusClearLabelTtl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW status clear label Ttl.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwStatusClearLabelTtl"])

    @PwStatusClearLabelTtl.setter
    def PwStatusClearLabelTtl(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwStatusClearLabelTtl"], value)

    @property
    def PwStatusClearTransmitInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the transmit interval in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwStatusClearTransmitInterval"])

    @PwStatusClearTransmitInterval.setter
    def PwStatusClearTransmitInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwStatusClearTransmitInterval"], value)

    @property
    def PwStatusCode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the selecting of the relevant option from the drop-down on the right hand side.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwStatusCode"])

    @PwStatusCode.setter
    def PwStatusCode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwStatusCode"], value)

    @property
    def PwStatusFaultLabelTtl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the TTL value to be set in the PW label header while sending out PW Status message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwStatusFaultLabelTtl"])

    @PwStatusFaultLabelTtl.setter
    def PwStatusFaultLabelTtl(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwStatusFaultLabelTtl"], value)

    @property
    def PwStatusFaultTransmitInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Status Fault Transmit Interval in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwStatusFaultTransmitInterval"])

    @PwStatusFaultTransmitInterval.setter
    def PwStatusFaultTransmitInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwStatusFaultTransmitInterval"], value)

    def update(
        self,
        AlarmTrigger=None,
        AlarmType=None,
        ApsTriggerType=None,
        CccvPauseTriggerOption=None,
        CccvResumeTriggerOption=None,
        ChangeSessionParameters=None,
        ClearMisconnectivityDefect=None,
        CounterType=None,
        DmInterval=None,
        DmIterations=None,
        DmMode=None,
        DmPadLen=None,
        DmRequestPaddedReply=None,
        DmTimeFormat=None,
        DmTrafficClass=None,
        DmType=None,
        EnableAlarm=None,
        EnableAlarmAis=None,
        EnableAlarmFastClear=None,
        EnableAlarmLck=None,
        EnableAlarmSetLdi=None,
        EnableApsTrigger=None,
        EnableCccvPause=None,
        EnableCccvResume=None,
        EnableDmTrigger=None,
        EnableLmTrigger=None,
        EnableLspPing=None,
        EnableLspPingFecStackValidation=None,
        EnableLspPingValidateReversePath=None,
        EnableLspTraceRoute=None,
        EnableLspTraceRouteFecStackValidation=None,
        EnablePwStatusClear=None,
        EnablePwStatusFault=None,
        LastDmResponseTimeout=None,
        LastLmResponseTimeout=None,
        LmInitialRxValue=None,
        LmInitialTxValue=None,
        LmInterval=None,
        LmIterations=None,
        LmMode=None,
        LmRxStep=None,
        LmTrafficClass=None,
        LmTxStep=None,
        LmType=None,
        LspPingEncapsulationType=None,
        LspPingResponseTimeout=None,
        LspPingTtlValue=None,
        LspTraceRouteEncapsulationType=None,
        LspTraceRouteResponseTimeout=None,
        LspTraceRouteTtlLimit=None,
        MinRxInterval=None,
        MinTxInterval=None,
        MisconnectivityDefect=None,
        MisconnectivityDefectOption=None,
        OnDemandCvDownstreamAddressType=None,
        OnDemandCvDownstreamIpAddress=None,
        OnDemandCvDsIflag=None,
        OnDemandCvDsNflag=None,
        OnDemandCvEgressIfNumber=None,
        OnDemandCvIncludeDestinationIdentifierTlv=None,
        OnDemandCvIncludeDetailedDownstreamMappingTlv=None,
        OnDemandCvIncludeDownstreamMappingTlv=None,
        OnDemandCvIncludePadTlv=None,
        OnDemandCvIncludeReplyTosByteTlv=None,
        OnDemandCvIncludeSourceIdentifierTlv=None,
        OnDemandCvIngressIfNumber=None,
        OnDemandCvNumberedDownstreamInterfaceAddress=None,
        OnDemandCvPadTlvFirstOctet=None,
        OnDemandCvPadTlvLength=None,
        OnDemandCvTosByte=None,
        OnDemandCvUnnumberedDownstreamInterfaceAddress=None,
        Periodicity=None,
        PwStatusClearLabelTtl=None,
        PwStatusClearTransmitInterval=None,
        PwStatusCode=None,
        PwStatusFaultLabelTtl=None,
        PwStatusFaultTransmitInterval=None,
    ):
        # type: (str, str, str, str, str, bool, bool, str, int, int, str, int, bool, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, int, int, int, str, int, int, int, str, str, int, int, str, int, int, str, str, bool, str, str, str, bool, bool, int, bool, bool, bool, bool, bool, bool, int, str, str, int, int, int, int, int, int, int, int, int) -> LearnedInformation
        """Updates learnedInformation resource on the server.

        Args
        ----
        - AlarmTrigger (str(clear | start)): This signifies the alarm trigger. Possible values include Clear and Start.
        - AlarmType (str(ietf | y1731)): This signifies the alarm type. Possible values include IETF and Y.1731.
        - ApsTriggerType (str(clear | forcedSwitch | manualSwitchToProtect | manualSwitchToWorking | lockout | exercise | freeze)): This signifies the Trigger type. Possible values include Clear, Exercise, Forced Switch, Freeze, Lockout, Manual Switch To Protect and Manual Switch To Working.
        - CccvPauseTriggerOption (str(tx | rx | txRx)): This signifies the cccv pause trigger option. Possible values include TX, RX and TXRX.
        - CccvResumeTriggerOption (str(tx | rx | txRx)): This signifies the cccv resume trigger option. Possible values include Tx, Rx and TxRx.
        - ChangeSessionParameters (bool): This specifies the minimum receive interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        - ClearMisconnectivityDefect (bool): If set true all the misconnectivity defects that have been triggered earlier with any type gets cleared.
        - CounterType (str(32Bit | 64Bit)): This signifies the LM Counter Type. Possible values include 32 Bit (default) and 64 Bit.
        - DmInterval (number): This signifies the DM interval in milliseconds.
        - DmIterations (number): This signifies the total number of DM queries to be sent.
        - DmMode (str(noResponseExpected | responseExpected)): This signifies the DM mode. The possible values include Response Expected and No Response Expected.
        - DmPadLen (number): This signifies the DM pad length.
        - DmRequestPaddedReply (bool): This signifies the DM request as a padded reply.
        - DmTimeFormat (str(ieee | ntp)): This signifies the DM time format. The possible values include IEEE and NTP.
        - DmTrafficClass (number): This signifies the DM traffic class value.
        - DmType (str(ietf | y1731)): This signifies the DM Type. Possible values include IETF and Y.1731.
        - EnableAlarm (bool): This signifies the enablement of the Alarm and the fields under it.
        - EnableAlarmAis (bool): This signifies the enablement of the Alarm AIS.
        - EnableAlarmFastClear (bool): Clears the Alarm State in 10 seconds
        - EnableAlarmLck (bool): This signifies the enablement of the Alarm lck.
        - EnableAlarmSetLdi (bool): This signifies the enablement of the Alarm Set LDI.
        - EnableApsTrigger (bool): This signifies the enablement of APS trigger.
        - EnableCccvPause (bool): This signifies the enabling of CCCV Pause.
        - EnableCccvResume (bool): This signifies the enablement of CCCV Resume.
        - EnableDmTrigger (bool): This signifies the enablement of the DM trigger.
        - EnableLmTrigger (bool): This signifies the enablement of the LM trigger.
        - EnableLspPing (bool): This signifies the enablement of the LSP Ping.
        - EnableLspPingFecStackValidation (bool): This signifies the enablement of the FEC Stack Validation.
        - EnableLspPingValidateReversePath (bool): If true validate reverse path bit is set in lsp ping message.
        - EnableLspTraceRoute (bool): This signifies the enablement of the lsp traceroute.
        - EnableLspTraceRouteFecStackValidation (bool): This signifies the enablement of the FEC Stack Validation.
        - EnablePwStatusClear (bool): This signifies the enablement of the PW Status Clear and the fields under it.
        - EnablePwStatusFault (bool): This signifies the enablement of the PW Status Fault.
        - LastDmResponseTimeout (number): This signifies the last DM Response Timeout.
        - LastLmResponseTimeout (number): This signifies the last LM response timeout.
        - LmInitialRxValue (number): This signifies the LM Initial Rx value.
        - LmInitialTxValue (number): This signifies the LM Initial Tx value.
        - LmInterval (number): This signifies the LM interval in milliseconds.
        - LmIterations (number): This signifies the number of LM queries to be sent.
        - LmMode (str(responseExpected | noResponseExpected)): This signifies the LM mode. Possible values include Response Expected and No Response Expected.
        - LmRxStep (number): This signifies the LM Rx step value.
        - LmTrafficClass (number): This signifies the LM Traffic Class.
        - LmTxStep (number): This signifies the LM Tx Step value.
        - LmType (str(ietf | y1731)): This signifies the LM type. The possible values include IETF and Y.1731.
        - LspPingEncapsulationType (str(GAch | UDP over IP over GAch)): This signifies the encapsulation type with which the lsp ping request message will be sent out. The possible values include UDP-IP-GAch and GAch.
        - LspPingResponseTimeout (number): This signifies the response timeout in milliseconds.
        - LspPingTtlValue (number): This signifies the LSP Ping Ttl value.
        - LspTraceRouteEncapsulationType (str(GAch | UDP over IP over GAch)): This signifies the encapsulation type with which the Trace route request message will be sen out. The possible values include UDP-IP-GAch and GAch.
        - LspTraceRouteResponseTimeout (number): This signifies the response timeout in milliseconds.
        - LspTraceRouteTtlLimit (number): This signifies the max TTL till which the Echo Request will be sent out as part of trace route process.
        - MinRxInterval (str(10 | 100 | 1000 | 10000 | 3.33 | 60000 | 600000)): This signifies the minimum receive interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        - MinTxInterval (str(10 | 100 | 1000 | 10000 | 3.33 | 60000 | 600000)): This signifies the learned information minimum transmit interval, in milliseconds. This specifies the minimum transmit interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        - MisconnectivityDefect (bool): To enable misconnectivity defect on the fly by changing LSP/PW MEP/MEG Id parameter or Your Discriminator on the source side.
        - MisconnectivityDefectOption (str(unexpectedMepId | unexpectedYourDiscriminator)): To enable misconnectivity defect on the fly by changing LSP/PW MEP/MEG Id parameter or Your Discriminator on the source side.
        - OnDemandCvDownstreamAddressType (str(ipv4Numbered | ipv4Unnumbered | nonIp)): This signifies the Address Type of the Downstream or Detailed Downstream Mapping TLV. This can be of three types.
        - OnDemandCvDownstreamIpAddress (str): This signifies the inclusion of the IP address in Downstream or Detailed Downstream Mapping TLV. This takes input in ip address format.
        - OnDemandCvDsIflag (bool): This signifies the setting of I bit in the DS Flag of Downstream or Detailed Downstream Mapping TLV.
        - OnDemandCvDsNflag (bool): If set true, N bit is set in the DS Flag of Downstream or Detailed Downstream Mapping TLV.
        - OnDemandCvEgressIfNumber (number): This signifies the Egress If Number, if address type of Downstream or Detailed Downstream Mapping TLV is set to nonIP.
        - OnDemandCvIncludeDestinationIdentifierTlv (bool): If channel type is set to GAch, this signifies the inclusion of Destination Identifier TLV in the On Demand CV message. Possible values are true or false.
        - OnDemandCvIncludeDetailedDownstreamMappingTlv (bool): This signifies the inclusion of the Detailed Downstream Mapping TLV in on demand cv message. Possible values are true or false.
        - OnDemandCvIncludeDownstreamMappingTlv (bool): This signifies the inclusion of Downstream Mapping TLV in on demand cv messages.
        - OnDemandCvIncludePadTlv (bool): This signifies the inclusion of Pad TLV in on demand cv messages (ping or traceroute).
        - OnDemandCvIncludeReplyTosByteTlv (bool): This signifies the inclusion of Reply Tos Byte TLV in on demand cv messages, if channel type is configured ip-udp-gach.
        - OnDemandCvIncludeSourceIdentifierTlv (bool): If channel type is set to GAch, this signifies the inclusion of Source Identifier TLV in the On Demand CV message. Possible values are true or false.
        - OnDemandCvIngressIfNumber (number): This signifies the Ingress If Number, if address type of Downstream or Detailed Downstream Mapping TLV is set to nonIP.
        - OnDemandCvNumberedDownstreamInterfaceAddress (str): If the address type of Downstream Address TLV is set to ipv4Numbered, it signifies the numbered Interface Address. This takes value in ip address format.
        - OnDemandCvPadTlvFirstOctet (str(drop | copy)): This signifies the value of first octet of Pad TLV. The possible values are copy or drop.
        - OnDemandCvPadTlvLength (number): This signifies the inclusion of Pad TLV length in On Demand CV message.
        - OnDemandCvTosByte (number): If channel type is set ip-udp-Gach, this signifies the value of Tos Byte field within Reply TOS Byte TLV, included in on demand cv messages.
        - OnDemandCvUnnumberedDownstreamInterfaceAddress (number): If the address type of Downstream Address TLV is set to ipv4Unnumbered, this signifies the unnumbered Interface Address. This takes value in integer format. The max value can be 4294967295.
        - Periodicity (number): This signifies the periodicity of the alarm.
        - PwStatusClearLabelTtl (number): This signifies the PW status clear label Ttl.
        - PwStatusClearTransmitInterval (number): This signifies the transmit interval in seconds.
        - PwStatusCode (number): This signifies the selecting of the relevant option from the drop-down on the right hand side.
        - PwStatusFaultLabelTtl (number): This signifies the TTL value to be set in the PW label header while sending out PW Status message.
        - PwStatusFaultTransmitInterval (number): This signifies the PW Status Fault Transmit Interval in seconds.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AlarmTrigger=None,
        AlarmType=None,
        ApsTriggerType=None,
        CccvPauseTriggerOption=None,
        CccvResumeTriggerOption=None,
        ChangeSessionParameters=None,
        ClearMisconnectivityDefect=None,
        CounterType=None,
        DmInterval=None,
        DmIterations=None,
        DmMode=None,
        DmPadLen=None,
        DmRequestPaddedReply=None,
        DmTimeFormat=None,
        DmTrafficClass=None,
        DmType=None,
        EnableAlarm=None,
        EnableAlarmAis=None,
        EnableAlarmFastClear=None,
        EnableAlarmLck=None,
        EnableAlarmSetLdi=None,
        EnableApsTrigger=None,
        EnableCccvPause=None,
        EnableCccvResume=None,
        EnableDmTrigger=None,
        EnableLmTrigger=None,
        EnableLspPing=None,
        EnableLspPingFecStackValidation=None,
        EnableLspPingValidateReversePath=None,
        EnableLspTraceRoute=None,
        EnableLspTraceRouteFecStackValidation=None,
        EnablePwStatusClear=None,
        EnablePwStatusFault=None,
        IsDmLearnedInformationRefreshed=None,
        IsGeneralLearnedInformationRefreshed=None,
        IsLmLearnedInformationRefreshed=None,
        IsPingLearnedInformationRefreshed=None,
        IsTraceRouteLearnedInformationRefreshed=None,
        LastDmResponseTimeout=None,
        LastLmResponseTimeout=None,
        LmInitialRxValue=None,
        LmInitialTxValue=None,
        LmInterval=None,
        LmIterations=None,
        LmMode=None,
        LmRxStep=None,
        LmTrafficClass=None,
        LmTxStep=None,
        LmType=None,
        LspPingEncapsulationType=None,
        LspPingResponseTimeout=None,
        LspPingTtlValue=None,
        LspTraceRouteEncapsulationType=None,
        LspTraceRouteResponseTimeout=None,
        LspTraceRouteTtlLimit=None,
        MinRxInterval=None,
        MinTxInterval=None,
        MisconnectivityDefect=None,
        MisconnectivityDefectOption=None,
        OnDemandCvDownstreamAddressType=None,
        OnDemandCvDownstreamIpAddress=None,
        OnDemandCvDsIflag=None,
        OnDemandCvDsNflag=None,
        OnDemandCvEgressIfNumber=None,
        OnDemandCvIncludeDestinationIdentifierTlv=None,
        OnDemandCvIncludeDetailedDownstreamMappingTlv=None,
        OnDemandCvIncludeDownstreamMappingTlv=None,
        OnDemandCvIncludePadTlv=None,
        OnDemandCvIncludeReplyTosByteTlv=None,
        OnDemandCvIncludeSourceIdentifierTlv=None,
        OnDemandCvIngressIfNumber=None,
        OnDemandCvNumberedDownstreamInterfaceAddress=None,
        OnDemandCvPadTlvFirstOctet=None,
        OnDemandCvPadTlvLength=None,
        OnDemandCvTosByte=None,
        OnDemandCvUnnumberedDownstreamInterfaceAddress=None,
        Periodicity=None,
        PwStatusClearLabelTtl=None,
        PwStatusClearTransmitInterval=None,
        PwStatusCode=None,
        PwStatusFaultLabelTtl=None,
        PwStatusFaultTransmitInterval=None,
    ):
        # type: (str, str, str, str, str, bool, bool, str, int, int, str, int, bool, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, int, int, int, str, int, int, int, str, str, int, int, str, int, int, str, str, bool, str, str, str, bool, bool, int, bool, bool, bool, bool, bool, bool, int, str, str, int, int, int, int, int, int, int, int, int) -> LearnedInformation
        """Finds and retrieves learnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInformation resources from the server.

        Args
        ----
        - AlarmTrigger (str(clear | start)): This signifies the alarm trigger. Possible values include Clear and Start.
        - AlarmType (str(ietf | y1731)): This signifies the alarm type. Possible values include IETF and Y.1731.
        - ApsTriggerType (str(clear | forcedSwitch | manualSwitchToProtect | manualSwitchToWorking | lockout | exercise | freeze)): This signifies the Trigger type. Possible values include Clear, Exercise, Forced Switch, Freeze, Lockout, Manual Switch To Protect and Manual Switch To Working.
        - CccvPauseTriggerOption (str(tx | rx | txRx)): This signifies the cccv pause trigger option. Possible values include TX, RX and TXRX.
        - CccvResumeTriggerOption (str(tx | rx | txRx)): This signifies the cccv resume trigger option. Possible values include Tx, Rx and TxRx.
        - ChangeSessionParameters (bool): This specifies the minimum receive interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        - ClearMisconnectivityDefect (bool): If set true all the misconnectivity defects that have been triggered earlier with any type gets cleared.
        - CounterType (str(32Bit | 64Bit)): This signifies the LM Counter Type. Possible values include 32 Bit (default) and 64 Bit.
        - DmInterval (number): This signifies the DM interval in milliseconds.
        - DmIterations (number): This signifies the total number of DM queries to be sent.
        - DmMode (str(noResponseExpected | responseExpected)): This signifies the DM mode. The possible values include Response Expected and No Response Expected.
        - DmPadLen (number): This signifies the DM pad length.
        - DmRequestPaddedReply (bool): This signifies the DM request as a padded reply.
        - DmTimeFormat (str(ieee | ntp)): This signifies the DM time format. The possible values include IEEE and NTP.
        - DmTrafficClass (number): This signifies the DM traffic class value.
        - DmType (str(ietf | y1731)): This signifies the DM Type. Possible values include IETF and Y.1731.
        - EnableAlarm (bool): This signifies the enablement of the Alarm and the fields under it.
        - EnableAlarmAis (bool): This signifies the enablement of the Alarm AIS.
        - EnableAlarmFastClear (bool): Clears the Alarm State in 10 seconds
        - EnableAlarmLck (bool): This signifies the enablement of the Alarm lck.
        - EnableAlarmSetLdi (bool): This signifies the enablement of the Alarm Set LDI.
        - EnableApsTrigger (bool): This signifies the enablement of APS trigger.
        - EnableCccvPause (bool): This signifies the enabling of CCCV Pause.
        - EnableCccvResume (bool): This signifies the enablement of CCCV Resume.
        - EnableDmTrigger (bool): This signifies the enablement of the DM trigger.
        - EnableLmTrigger (bool): This signifies the enablement of the LM trigger.
        - EnableLspPing (bool): This signifies the enablement of the LSP Ping.
        - EnableLspPingFecStackValidation (bool): This signifies the enablement of the FEC Stack Validation.
        - EnableLspPingValidateReversePath (bool): If true validate reverse path bit is set in lsp ping message.
        - EnableLspTraceRoute (bool): This signifies the enablement of the lsp traceroute.
        - EnableLspTraceRouteFecStackValidation (bool): This signifies the enablement of the FEC Stack Validation.
        - EnablePwStatusClear (bool): This signifies the enablement of the PW Status Clear and the fields under it.
        - EnablePwStatusFault (bool): This signifies the enablement of the PW Status Fault.
        - IsDmLearnedInformationRefreshed (bool): This signifies the refresheing of the DM learned information.
        - IsGeneralLearnedInformationRefreshed (bool): This signifies the refereshing of the general learned information.
        - IsLmLearnedInformationRefreshed (bool): This signifies the refresheing of the LM learned information.
        - IsPingLearnedInformationRefreshed (bool): This signifies the refresheing of the Ping learned information.
        - IsTraceRouteLearnedInformationRefreshed (bool): This signifies the refresheing of the Trace Route learned information.
        - LastDmResponseTimeout (number): This signifies the last DM Response Timeout.
        - LastLmResponseTimeout (number): This signifies the last LM response timeout.
        - LmInitialRxValue (number): This signifies the LM Initial Rx value.
        - LmInitialTxValue (number): This signifies the LM Initial Tx value.
        - LmInterval (number): This signifies the LM interval in milliseconds.
        - LmIterations (number): This signifies the number of LM queries to be sent.
        - LmMode (str(responseExpected | noResponseExpected)): This signifies the LM mode. Possible values include Response Expected and No Response Expected.
        - LmRxStep (number): This signifies the LM Rx step value.
        - LmTrafficClass (number): This signifies the LM Traffic Class.
        - LmTxStep (number): This signifies the LM Tx Step value.
        - LmType (str(ietf | y1731)): This signifies the LM type. The possible values include IETF and Y.1731.
        - LspPingEncapsulationType (str(GAch | UDP over IP over GAch)): This signifies the encapsulation type with which the lsp ping request message will be sent out. The possible values include UDP-IP-GAch and GAch.
        - LspPingResponseTimeout (number): This signifies the response timeout in milliseconds.
        - LspPingTtlValue (number): This signifies the LSP Ping Ttl value.
        - LspTraceRouteEncapsulationType (str(GAch | UDP over IP over GAch)): This signifies the encapsulation type with which the Trace route request message will be sen out. The possible values include UDP-IP-GAch and GAch.
        - LspTraceRouteResponseTimeout (number): This signifies the response timeout in milliseconds.
        - LspTraceRouteTtlLimit (number): This signifies the max TTL till which the Echo Request will be sent out as part of trace route process.
        - MinRxInterval (str(10 | 100 | 1000 | 10000 | 3.33 | 60000 | 600000)): This signifies the minimum receive interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        - MinTxInterval (str(10 | 100 | 1000 | 10000 | 3.33 | 60000 | 600000)): This signifies the learned information minimum transmit interval, in milliseconds. This specifies the minimum transmit interval of cc messages in millisecond, at the source side that the user intends to set on the fly.
        - MisconnectivityDefect (bool): To enable misconnectivity defect on the fly by changing LSP/PW MEP/MEG Id parameter or Your Discriminator on the source side.
        - MisconnectivityDefectOption (str(unexpectedMepId | unexpectedYourDiscriminator)): To enable misconnectivity defect on the fly by changing LSP/PW MEP/MEG Id parameter or Your Discriminator on the source side.
        - OnDemandCvDownstreamAddressType (str(ipv4Numbered | ipv4Unnumbered | nonIp)): This signifies the Address Type of the Downstream or Detailed Downstream Mapping TLV. This can be of three types.
        - OnDemandCvDownstreamIpAddress (str): This signifies the inclusion of the IP address in Downstream or Detailed Downstream Mapping TLV. This takes input in ip address format.
        - OnDemandCvDsIflag (bool): This signifies the setting of I bit in the DS Flag of Downstream or Detailed Downstream Mapping TLV.
        - OnDemandCvDsNflag (bool): If set true, N bit is set in the DS Flag of Downstream or Detailed Downstream Mapping TLV.
        - OnDemandCvEgressIfNumber (number): This signifies the Egress If Number, if address type of Downstream or Detailed Downstream Mapping TLV is set to nonIP.
        - OnDemandCvIncludeDestinationIdentifierTlv (bool): If channel type is set to GAch, this signifies the inclusion of Destination Identifier TLV in the On Demand CV message. Possible values are true or false.
        - OnDemandCvIncludeDetailedDownstreamMappingTlv (bool): This signifies the inclusion of the Detailed Downstream Mapping TLV in on demand cv message. Possible values are true or false.
        - OnDemandCvIncludeDownstreamMappingTlv (bool): This signifies the inclusion of Downstream Mapping TLV in on demand cv messages.
        - OnDemandCvIncludePadTlv (bool): This signifies the inclusion of Pad TLV in on demand cv messages (ping or traceroute).
        - OnDemandCvIncludeReplyTosByteTlv (bool): This signifies the inclusion of Reply Tos Byte TLV in on demand cv messages, if channel type is configured ip-udp-gach.
        - OnDemandCvIncludeSourceIdentifierTlv (bool): If channel type is set to GAch, this signifies the inclusion of Source Identifier TLV in the On Demand CV message. Possible values are true or false.
        - OnDemandCvIngressIfNumber (number): This signifies the Ingress If Number, if address type of Downstream or Detailed Downstream Mapping TLV is set to nonIP.
        - OnDemandCvNumberedDownstreamInterfaceAddress (str): If the address type of Downstream Address TLV is set to ipv4Numbered, it signifies the numbered Interface Address. This takes value in ip address format.
        - OnDemandCvPadTlvFirstOctet (str(drop | copy)): This signifies the value of first octet of Pad TLV. The possible values are copy or drop.
        - OnDemandCvPadTlvLength (number): This signifies the inclusion of Pad TLV length in On Demand CV message.
        - OnDemandCvTosByte (number): If channel type is set ip-udp-Gach, this signifies the value of Tos Byte field within Reply TOS Byte TLV, included in on demand cv messages.
        - OnDemandCvUnnumberedDownstreamInterfaceAddress (number): If the address type of Downstream Address TLV is set to ipv4Unnumbered, this signifies the unnumbered Interface Address. This takes value in integer format. The max value can be 4294967295.
        - Periodicity (number): This signifies the periodicity of the alarm.
        - PwStatusClearLabelTtl (number): This signifies the PW status clear label Ttl.
        - PwStatusClearTransmitInterval (number): This signifies the transmit interval in seconds.
        - PwStatusCode (number): This signifies the selecting of the relevant option from the drop-down on the right hand side.
        - PwStatusFaultLabelTtl (number): This signifies the TTL value to be set in the PW label header while sending out PW Status message.
        - PwStatusFaultTransmitInterval (number): This signifies the PW Status Fault Transmit Interval in seconds.

        Returns
        -------
        - self: This instance with matching learnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearRecordsForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the clearRecordsForTrigger operation on the server.

        This option is used to clear the selected learned information using the command addRecordForTrigger

        clearRecordsForTrigger(async_operation=bool)bool
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "clearRecordsForTrigger", payload=payload, response_object=None
        )

    def RefreshLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInformation operation on the server.

        This signifies the refreshing of the learned information of MPLSTP router.

        refreshLearnedInformation(async_operation=bool)bool
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshLearnedInformation", payload=payload, response_object=None
        )

    def Trigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the trigger operation on the server.

        This signifies the learned info trigger settings.

        trigger(async_operation=bool)bool
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute("trigger", payload=payload, response_object=None)
