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


class Link(Base):
    """
    The Link class encapsulates a list of link resources that are managed by the user.
    A list of resources can be retrieved from the server using the Link.find() method.
    The list can be managed by using the Link.add() and Link.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "link"
    _SDM_ATT_MAP = {
        "DisableInformationPduTx": "disableInformationPduTx",
        "DisableNonInformationPduTx": "disableNonInformationPduTx",
        "EnableCriticalEvent": "enableCriticalEvent",
        "EnableDyingGasp": "enableDyingGasp",
        "EnableLinkFault": "enableLinkFault",
        "EnableLoopbackResponse": "enableLoopbackResponse",
        "EnableVariableResponse": "enableVariableResponse",
        "Enabled": "enabled",
        "EthernetTypeUsedForDataTraffic": "ethernetTypeUsedForDataTraffic",
        "EventInterval": "eventInterval",
        "InformationPduCountPerSecond": "informationPduCountPerSecond",
        "IsDiscLearnedInfoRefreshed": "isDiscLearnedInfoRefreshed",
        "IsEventNotificationLearnedInfoRefreshed": "isEventNotificationLearnedInfoRefreshed",
        "IsLoopbackLearnedInfoRefreshed": "isLoopbackLearnedInfoRefreshed",
        "IsVariableRequestLearnedInfoRefreshed": "isVariableRequestLearnedInfoRefreshed",
        "LinkEventTxMode": "linkEventTxMode",
        "LocalLostLinkTimer": "localLostLinkTimer",
        "LoopbackCmd": "loopbackCmd",
        "LoopbackTimeout": "loopbackTimeout",
        "MacAddress": "macAddress",
        "MaxOamPduSize": "maxOamPduSize",
        "OperationMode": "operationMode",
        "Oui": "oui",
        "OverrideLocalEvaluating": "overrideLocalEvaluating",
        "OverrideLocalSatisfied": "overrideLocalSatisfied",
        "OverrideLocalStable": "overrideLocalStable",
        "OverrideRemoteEvaluating": "overrideRemoteEvaluating",
        "OverrideRemoteStable": "overrideRemoteStable",
        "OverrideRevision": "overrideRevision",
        "OverrideSequenceNumber": "overrideSequenceNumber",
        "Revision": "revision",
        "SequenceNumber": "sequenceNumber",
        "SupportsInterpretingLinkEvents": "supportsInterpretingLinkEvents",
        "SupportsRemoteLoopback": "supportsRemoteLoopback",
        "SupportsUnidirectionalMode": "supportsUnidirectionalMode",
        "SupportsVariableRetrieval": "supportsVariableRetrieval",
        "UpdateRequired": "updateRequired",
        "VariableResponseTimeout": "variableResponseTimeout",
        "VendorSpecificInformation": "vendorSpecificInformation",
        "Version": "version",
    }
    _SDM_ENUM_MAP = {
        "linkEventTxMode": ["single", "periodic"],
        "loopbackCmd": ["disableLoopback", "enableLoopback"],
        "operationMode": ["active", "passive"],
    }

    def __init__(self, parent, list_op=False):
        super(Link, self).__init__(parent, list_op)

    @property
    def DiscoveredLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.discoveredlearnedinfo_c0e259e03145b18e9d30c510acecc721.DiscoveredLearnedInfo): An instance of the DiscoveredLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.discoveredlearnedinfo_c0e259e03145b18e9d30c510acecc721 import (
            DiscoveredLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DiscoveredLearnedInfo", None) is not None:
                return self._properties.get("DiscoveredLearnedInfo")
        return DiscoveredLearnedInfo(self)

    @property
    def ErroredFramePeriodTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframeperiodtlv_7e1618c295e055418cf5b367b43f7292.ErroredFramePeriodTlv): An instance of the ErroredFramePeriodTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframeperiodtlv_7e1618c295e055418cf5b367b43f7292 import (
            ErroredFramePeriodTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ErroredFramePeriodTlv", None) is not None:
                return self._properties.get("ErroredFramePeriodTlv")
        return ErroredFramePeriodTlv(self)._select()

    @property
    def ErroredFrameSecondsSummaryTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframesecondssummarytlv_4572df5d86785124bce4966bd170e271.ErroredFrameSecondsSummaryTlv): An instance of the ErroredFrameSecondsSummaryTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframesecondssummarytlv_4572df5d86785124bce4966bd170e271 import (
            ErroredFrameSecondsSummaryTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ErroredFrameSecondsSummaryTlv", None) is not None:
                return self._properties.get("ErroredFrameSecondsSummaryTlv")
        return ErroredFrameSecondsSummaryTlv(self)._select()

    @property
    def ErroredFrameTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframetlv_2de47697193c848397254c28f553122b.ErroredFrameTlv): An instance of the ErroredFrameTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframetlv_2de47697193c848397254c28f553122b import (
            ErroredFrameTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ErroredFrameTlv", None) is not None:
                return self._properties.get("ErroredFrameTlv")
        return ErroredFrameTlv(self)._select()

    @property
    def ErroredSymbolPeriodTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredsymbolperiodtlv_1f85b8c597f306d2953ee0bd546e6ce7.ErroredSymbolPeriodTlv): An instance of the ErroredSymbolPeriodTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredsymbolperiodtlv_1f85b8c597f306d2953ee0bd546e6ce7 import (
            ErroredSymbolPeriodTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ErroredSymbolPeriodTlv", None) is not None:
                return self._properties.get("ErroredSymbolPeriodTlv")
        return ErroredSymbolPeriodTlv(self)._select()

    @property
    def EventNotificationLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eventnotificationlearnedinfo_e681bdab1ec425c98268821ac8241416.EventNotificationLearnedInfo): An instance of the EventNotificationLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eventnotificationlearnedinfo_e681bdab1ec425c98268821ac8241416 import (
            EventNotificationLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EventNotificationLearnedInfo", None) is not None:
                return self._properties.get("EventNotificationLearnedInfo")
        return EventNotificationLearnedInfo(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_fb4befd0e6a80f240fc4262878630bef.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_fb4befd0e6a80f240fc4262878630bef import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def OrganizationSpecificEventTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificeventtlv_97402ba8afcd510e9807d552c63ac5d6.OrganizationSpecificEventTlv): An instance of the OrganizationSpecificEventTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificeventtlv_97402ba8afcd510e9807d552c63ac5d6 import (
            OrganizationSpecificEventTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OrganizationSpecificEventTlv", None) is not None:
                return self._properties.get("OrganizationSpecificEventTlv")
        return OrganizationSpecificEventTlv(self)._select()

    @property
    def OrganizationSpecificInfoTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificinfotlv_540bb6e0e1ea48ec1f0e9e2272797864.OrganizationSpecificInfoTlv): An instance of the OrganizationSpecificInfoTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificinfotlv_540bb6e0e1ea48ec1f0e9e2272797864 import (
            OrganizationSpecificInfoTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OrganizationSpecificInfoTlv", None) is not None:
                return self._properties.get("OrganizationSpecificInfoTlv")
        return OrganizationSpecificInfoTlv(self)

    @property
    def OrganizationSpecificOamPduData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificoampdudata_af0b25bf714f4cdf2df542ec69948aa9.OrganizationSpecificOamPduData): An instance of the OrganizationSpecificOamPduData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificoampdudata_af0b25bf714f4cdf2df542ec69948aa9 import (
            OrganizationSpecificOamPduData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OrganizationSpecificOamPduData", None) is not None:
                return self._properties.get("OrganizationSpecificOamPduData")
        return OrganizationSpecificOamPduData(self)

    @property
    def VarDescriptor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vardescriptor_183285cb9f666d376d6aa33dcf457f3e.VarDescriptor): An instance of the VarDescriptor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vardescriptor_183285cb9f666d376d6aa33dcf457f3e import (
            VarDescriptor,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VarDescriptor", None) is not None:
                return self._properties.get("VarDescriptor")
        return VarDescriptor(self)

    @property
    def VariableRequestLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variablerequestlearnedinfo_0657cfbaba3ed550a2451249c7c53a6a.VariableRequestLearnedInfo): An instance of the VariableRequestLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variablerequestlearnedinfo_0657cfbaba3ed550a2451249c7c53a6a import (
            VariableRequestLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VariableRequestLearnedInfo", None) is not None:
                return self._properties.get("VariableRequestLearnedInfo")
        return VariableRequestLearnedInfo(self)

    @property
    def VariableResponseDatabase(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variableresponsedatabase_a754eac9129994b0d20fa50e381d4b44.VariableResponseDatabase): An instance of the VariableResponseDatabase class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variableresponsedatabase_a754eac9129994b0d20fa50e381d4b44 import (
            VariableResponseDatabase,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VariableResponseDatabase", None) is not None:
                return self._properties.get("VariableResponseDatabase")
        return VariableResponseDatabase(self)

    @property
    def DisableInformationPduTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableInformationPduTx"])

    @DisableInformationPduTx.setter
    def DisableInformationPduTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableInformationPduTx"], value)

    @property
    def DisableNonInformationPduTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableNonInformationPduTx"])

    @DisableNonInformationPduTx.setter
    def DisableNonInformationPduTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableNonInformationPduTx"], value)

    @property
    def EnableCriticalEvent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCriticalEvent"])

    @EnableCriticalEvent.setter
    def EnableCriticalEvent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCriticalEvent"], value)

    @property
    def EnableDyingGasp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDyingGasp"])

    @EnableDyingGasp.setter
    def EnableDyingGasp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDyingGasp"], value)

    @property
    def EnableLinkFault(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLinkFault"])

    @EnableLinkFault.setter
    def EnableLinkFault(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLinkFault"], value)

    @property
    def EnableLoopbackResponse(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLoopbackResponse"])

    @EnableLoopbackResponse.setter
    def EnableLoopbackResponse(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLoopbackResponse"], value)

    @property
    def EnableVariableResponse(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVariableResponse"])

    @EnableVariableResponse.setter
    def EnableVariableResponse(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVariableResponse"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def EthernetTypeUsedForDataTraffic(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetTypeUsedForDataTraffic"])

    @EthernetTypeUsedForDataTraffic.setter
    def EthernetTypeUsedForDataTraffic(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetTypeUsedForDataTraffic"], value)

    @property
    def EventInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EventInterval"])

    @EventInterval.setter
    def EventInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EventInterval"], value)

    @property
    def InformationPduCountPerSecond(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["InformationPduCountPerSecond"])

    @InformationPduCountPerSecond.setter
    def InformationPduCountPerSecond(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InformationPduCountPerSecond"], value)

    @property
    def IsDiscLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsDiscLearnedInfoRefreshed"])

    @property
    def IsEventNotificationLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsEventNotificationLearnedInfoRefreshed"]
        )

    @property
    def IsLoopbackLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLoopbackLearnedInfoRefreshed"])

    @property
    def IsVariableRequestLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsVariableRequestLearnedInfoRefreshed"]
        )

    @property
    def LinkEventTxMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(single | periodic):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkEventTxMode"])

    @LinkEventTxMode.setter
    def LinkEventTxMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkEventTxMode"], value)

    @property
    def LocalLostLinkTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalLostLinkTimer"])

    @LocalLostLinkTimer.setter
    def LocalLostLinkTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalLostLinkTimer"], value)

    @property
    def LoopbackCmd(self):
        # type: () -> str
        """
        Returns
        -------
        - str(disableLoopback | enableLoopback):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackCmd"])

    @LoopbackCmd.setter
    def LoopbackCmd(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackCmd"], value)

    @property
    def LoopbackTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackTimeout"])

    @LoopbackTimeout.setter
    def LoopbackTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackTimeout"], value)

    @property
    def MacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacAddress"])

    @MacAddress.setter
    def MacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacAddress"], value)

    @property
    def MaxOamPduSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxOamPduSize"])

    @MaxOamPduSize.setter
    def MaxOamPduSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxOamPduSize"], value)

    @property
    def OperationMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(active | passive):
        """
        return self._get_attribute(self._SDM_ATT_MAP["OperationMode"])

    @OperationMode.setter
    def OperationMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OperationMode"], value)

    @property
    def Oui(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Oui"])

    @Oui.setter
    def Oui(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Oui"], value)

    @property
    def OverrideLocalEvaluating(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideLocalEvaluating"])

    @OverrideLocalEvaluating.setter
    def OverrideLocalEvaluating(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideLocalEvaluating"], value)

    @property
    def OverrideLocalSatisfied(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideLocalSatisfied"])

    @OverrideLocalSatisfied.setter
    def OverrideLocalSatisfied(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideLocalSatisfied"], value)

    @property
    def OverrideLocalStable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideLocalStable"])

    @OverrideLocalStable.setter
    def OverrideLocalStable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideLocalStable"], value)

    @property
    def OverrideRemoteEvaluating(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideRemoteEvaluating"])

    @OverrideRemoteEvaluating.setter
    def OverrideRemoteEvaluating(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideRemoteEvaluating"], value)

    @property
    def OverrideRemoteStable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideRemoteStable"])

    @OverrideRemoteStable.setter
    def OverrideRemoteStable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideRemoteStable"], value)

    @property
    def OverrideRevision(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideRevision"])

    @OverrideRevision.setter
    def OverrideRevision(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideRevision"], value)

    @property
    def OverrideSequenceNumber(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideSequenceNumber"])

    @OverrideSequenceNumber.setter
    def OverrideSequenceNumber(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideSequenceNumber"], value)

    @property
    def Revision(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Revision"])

    @Revision.setter
    def Revision(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Revision"], value)

    @property
    def SequenceNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceNumber"])

    @SequenceNumber.setter
    def SequenceNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceNumber"], value)

    @property
    def SupportsInterpretingLinkEvents(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportsInterpretingLinkEvents"])

    @SupportsInterpretingLinkEvents.setter
    def SupportsInterpretingLinkEvents(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportsInterpretingLinkEvents"], value)

    @property
    def SupportsRemoteLoopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportsRemoteLoopback"])

    @SupportsRemoteLoopback.setter
    def SupportsRemoteLoopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportsRemoteLoopback"], value)

    @property
    def SupportsUnidirectionalMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportsUnidirectionalMode"])

    @SupportsUnidirectionalMode.setter
    def SupportsUnidirectionalMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportsUnidirectionalMode"], value)

    @property
    def SupportsVariableRetrieval(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportsVariableRetrieval"])

    @SupportsVariableRetrieval.setter
    def SupportsVariableRetrieval(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportsVariableRetrieval"], value)

    @property
    def UpdateRequired(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpdateRequired"])

    @property
    def VariableResponseTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["VariableResponseTimeout"])

    @VariableResponseTimeout.setter
    def VariableResponseTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VariableResponseTimeout"], value)

    @property
    def VendorSpecificInformation(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorSpecificInformation"])

    @VendorSpecificInformation.setter
    def VendorSpecificInformation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorSpecificInformation"], value)

    @property
    def Version(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Version"])

    @Version.setter
    def Version(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Version"], value)

    def update(
        self,
        DisableInformationPduTx=None,
        DisableNonInformationPduTx=None,
        EnableCriticalEvent=None,
        EnableDyingGasp=None,
        EnableLinkFault=None,
        EnableLoopbackResponse=None,
        EnableVariableResponse=None,
        Enabled=None,
        EthernetTypeUsedForDataTraffic=None,
        EventInterval=None,
        InformationPduCountPerSecond=None,
        LinkEventTxMode=None,
        LocalLostLinkTimer=None,
        LoopbackCmd=None,
        LoopbackTimeout=None,
        MacAddress=None,
        MaxOamPduSize=None,
        OperationMode=None,
        Oui=None,
        OverrideLocalEvaluating=None,
        OverrideLocalSatisfied=None,
        OverrideLocalStable=None,
        OverrideRemoteEvaluating=None,
        OverrideRemoteStable=None,
        OverrideRevision=None,
        OverrideSequenceNumber=None,
        Revision=None,
        SequenceNumber=None,
        SupportsInterpretingLinkEvents=None,
        SupportsRemoteLoopback=None,
        SupportsUnidirectionalMode=None,
        SupportsVariableRetrieval=None,
        VariableResponseTimeout=None,
        VendorSpecificInformation=None,
        Version=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, int, str, int, str, int, str, str, bool, bool, bool, bool, bool, bool, bool, int, int, bool, bool, bool, bool, int, str, int) -> Link
        """Updates link resource on the server.

        Args
        ----
        - DisableInformationPduTx (bool):
        - DisableNonInformationPduTx (bool):
        - EnableCriticalEvent (bool):
        - EnableDyingGasp (bool):
        - EnableLinkFault (bool):
        - EnableLoopbackResponse (bool):
        - EnableVariableResponse (bool):
        - Enabled (bool):
        - EthernetTypeUsedForDataTraffic (number):
        - EventInterval (number):
        - InformationPduCountPerSecond (number):
        - LinkEventTxMode (str(single | periodic)):
        - LocalLostLinkTimer (number):
        - LoopbackCmd (str(disableLoopback | enableLoopback)):
        - LoopbackTimeout (number):
        - MacAddress (str):
        - MaxOamPduSize (number):
        - OperationMode (str(active | passive)):
        - Oui (str):
        - OverrideLocalEvaluating (bool):
        - OverrideLocalSatisfied (bool):
        - OverrideLocalStable (bool):
        - OverrideRemoteEvaluating (bool):
        - OverrideRemoteStable (bool):
        - OverrideRevision (bool):
        - OverrideSequenceNumber (bool):
        - Revision (number):
        - SequenceNumber (number):
        - SupportsInterpretingLinkEvents (bool):
        - SupportsRemoteLoopback (bool):
        - SupportsUnidirectionalMode (bool):
        - SupportsVariableRetrieval (bool):
        - VariableResponseTimeout (number):
        - VendorSpecificInformation (str):
        - Version (number):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DisableInformationPduTx=None,
        DisableNonInformationPduTx=None,
        EnableCriticalEvent=None,
        EnableDyingGasp=None,
        EnableLinkFault=None,
        EnableLoopbackResponse=None,
        EnableVariableResponse=None,
        Enabled=None,
        EthernetTypeUsedForDataTraffic=None,
        EventInterval=None,
        InformationPduCountPerSecond=None,
        LinkEventTxMode=None,
        LocalLostLinkTimer=None,
        LoopbackCmd=None,
        LoopbackTimeout=None,
        MacAddress=None,
        MaxOamPduSize=None,
        OperationMode=None,
        Oui=None,
        OverrideLocalEvaluating=None,
        OverrideLocalSatisfied=None,
        OverrideLocalStable=None,
        OverrideRemoteEvaluating=None,
        OverrideRemoteStable=None,
        OverrideRevision=None,
        OverrideSequenceNumber=None,
        Revision=None,
        SequenceNumber=None,
        SupportsInterpretingLinkEvents=None,
        SupportsRemoteLoopback=None,
        SupportsUnidirectionalMode=None,
        SupportsVariableRetrieval=None,
        VariableResponseTimeout=None,
        VendorSpecificInformation=None,
        Version=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, int, str, int, str, int, str, str, bool, bool, bool, bool, bool, bool, bool, int, int, bool, bool, bool, bool, int, str, int) -> Link
        """Adds a new link resource on the server and adds it to the container.

        Args
        ----
        - DisableInformationPduTx (bool):
        - DisableNonInformationPduTx (bool):
        - EnableCriticalEvent (bool):
        - EnableDyingGasp (bool):
        - EnableLinkFault (bool):
        - EnableLoopbackResponse (bool):
        - EnableVariableResponse (bool):
        - Enabled (bool):
        - EthernetTypeUsedForDataTraffic (number):
        - EventInterval (number):
        - InformationPduCountPerSecond (number):
        - LinkEventTxMode (str(single | periodic)):
        - LocalLostLinkTimer (number):
        - LoopbackCmd (str(disableLoopback | enableLoopback)):
        - LoopbackTimeout (number):
        - MacAddress (str):
        - MaxOamPduSize (number):
        - OperationMode (str(active | passive)):
        - Oui (str):
        - OverrideLocalEvaluating (bool):
        - OverrideLocalSatisfied (bool):
        - OverrideLocalStable (bool):
        - OverrideRemoteEvaluating (bool):
        - OverrideRemoteStable (bool):
        - OverrideRevision (bool):
        - OverrideSequenceNumber (bool):
        - Revision (number):
        - SequenceNumber (number):
        - SupportsInterpretingLinkEvents (bool):
        - SupportsRemoteLoopback (bool):
        - SupportsUnidirectionalMode (bool):
        - SupportsVariableRetrieval (bool):
        - VariableResponseTimeout (number):
        - VendorSpecificInformation (str):
        - Version (number):

        Returns
        -------
        - self: This instance with all currently retrieved link resources using find and the newly added link resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained link resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        DisableInformationPduTx=None,
        DisableNonInformationPduTx=None,
        EnableCriticalEvent=None,
        EnableDyingGasp=None,
        EnableLinkFault=None,
        EnableLoopbackResponse=None,
        EnableVariableResponse=None,
        Enabled=None,
        EthernetTypeUsedForDataTraffic=None,
        EventInterval=None,
        InformationPduCountPerSecond=None,
        IsDiscLearnedInfoRefreshed=None,
        IsEventNotificationLearnedInfoRefreshed=None,
        IsLoopbackLearnedInfoRefreshed=None,
        IsVariableRequestLearnedInfoRefreshed=None,
        LinkEventTxMode=None,
        LocalLostLinkTimer=None,
        LoopbackCmd=None,
        LoopbackTimeout=None,
        MacAddress=None,
        MaxOamPduSize=None,
        OperationMode=None,
        Oui=None,
        OverrideLocalEvaluating=None,
        OverrideLocalSatisfied=None,
        OverrideLocalStable=None,
        OverrideRemoteEvaluating=None,
        OverrideRemoteStable=None,
        OverrideRevision=None,
        OverrideSequenceNumber=None,
        Revision=None,
        SequenceNumber=None,
        SupportsInterpretingLinkEvents=None,
        SupportsRemoteLoopback=None,
        SupportsUnidirectionalMode=None,
        SupportsVariableRetrieval=None,
        UpdateRequired=None,
        VariableResponseTimeout=None,
        VendorSpecificInformation=None,
        Version=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, bool, bool, bool, bool, str, int, str, int, str, int, str, str, bool, bool, bool, bool, bool, bool, bool, int, int, bool, bool, bool, bool, bool, int, str, int) -> Link
        """Finds and retrieves link resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve link resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all link resources from the server.

        Args
        ----
        - DisableInformationPduTx (bool):
        - DisableNonInformationPduTx (bool):
        - EnableCriticalEvent (bool):
        - EnableDyingGasp (bool):
        - EnableLinkFault (bool):
        - EnableLoopbackResponse (bool):
        - EnableVariableResponse (bool):
        - Enabled (bool):
        - EthernetTypeUsedForDataTraffic (number):
        - EventInterval (number):
        - InformationPduCountPerSecond (number):
        - IsDiscLearnedInfoRefreshed (bool):
        - IsEventNotificationLearnedInfoRefreshed (bool):
        - IsLoopbackLearnedInfoRefreshed (bool):
        - IsVariableRequestLearnedInfoRefreshed (bool):
        - LinkEventTxMode (str(single | periodic)):
        - LocalLostLinkTimer (number):
        - LoopbackCmd (str(disableLoopback | enableLoopback)):
        - LoopbackTimeout (number):
        - MacAddress (str):
        - MaxOamPduSize (number):
        - OperationMode (str(active | passive)):
        - Oui (str):
        - OverrideLocalEvaluating (bool):
        - OverrideLocalSatisfied (bool):
        - OverrideLocalStable (bool):
        - OverrideRemoteEvaluating (bool):
        - OverrideRemoteStable (bool):
        - OverrideRevision (bool):
        - OverrideSequenceNumber (bool):
        - Revision (number):
        - SequenceNumber (number):
        - SupportsInterpretingLinkEvents (bool):
        - SupportsRemoteLoopback (bool):
        - SupportsUnidirectionalMode (bool):
        - SupportsVariableRetrieval (bool):
        - UpdateRequired (bool):
        - VariableResponseTimeout (number):
        - VendorSpecificInformation (str):
        - Version (number):

        Returns
        -------
        - self: This instance with matching link resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of link data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the link resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshDiscLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshDiscLearnedInfo operation on the server.

        refreshDiscLearnedInfo(async_operation=bool)bool
        ------------------------------------------------
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
        return self._execute(
            "refreshDiscLearnedInfo", payload=payload, response_object=None
        )

    def RefreshEventNotificationLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshEventNotificationLearnedInfo operation on the server.

        refreshEventNotificationLearnedInfo(async_operation=bool)bool
        -------------------------------------------------------------
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
        return self._execute(
            "refreshEventNotificationLearnedInfo", payload=payload, response_object=None
        )

    def RestartDiscovery(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the restartDiscovery operation on the server.

        restartDiscovery(async_operation=bool)bool
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
        return self._execute("restartDiscovery", payload=payload, response_object=None)

    def SendLoopback(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendLoopback operation on the server.

        sendLoopback(async_operation=bool)bool
        --------------------------------------
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
        return self._execute("sendLoopback", payload=payload, response_object=None)

    def SendOrgSpecificPdu(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendOrgSpecificPdu operation on the server.

        sendOrgSpecificPdu(async_operation=bool)bool
        --------------------------------------------
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
        return self._execute(
            "sendOrgSpecificPdu", payload=payload, response_object=None
        )

    def SendUpdatedParameters(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendUpdatedParameters operation on the server.

        sendUpdatedParameters(async_operation=bool)bool
        -----------------------------------------------
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
        return self._execute(
            "sendUpdatedParameters", payload=payload, response_object=None
        )

    def SendVariableRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendVariableRequest operation on the server.

        sendVariableRequest(async_operation=bool)bool
        ---------------------------------------------
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
        return self._execute(
            "sendVariableRequest", payload=payload, response_object=None
        )

    def StartEventPduTransmission(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the startEventPduTransmission operation on the server.

        startEventPduTransmission(async_operation=bool)bool
        ---------------------------------------------------
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
        return self._execute(
            "startEventPduTransmission", payload=payload, response_object=None
        )

    def StopEventPduTransmission(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the stopEventPduTransmission operation on the server.

        stopEventPduTransmission(async_operation=bool)bool
        --------------------------------------------------
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
        return self._execute(
            "stopEventPduTransmission", payload=payload, response_object=None
        )
