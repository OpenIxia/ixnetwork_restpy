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


class OamAggregatedStatistics(Base):
    """Represents stats of OAM Aggregated Statistics
    The OamAggregatedStatistics class encapsulates a required oamAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "oamAggregatedStatistics"
    _SDM_ATT_MAP = {
        "CriticalEventRx": "criticalEventRx",
        "CriticalEventTx": "criticalEventTx",
        "DyingGaspRx": "dyingGaspRx",
        "DyingGaspTx": "dyingGaspTx",
        "ErroredFrameErrorRunningTotalRx": "erroredFrameErrorRunningTotalRx",
        "ErroredFrameErrorRunningTotalTx": "erroredFrameErrorRunningTotalTx",
        "ErroredFrameEventRunningTotalRx": "erroredFrameEventRunningTotalRx",
        "ErroredFrameEventRunningTotalTx": "erroredFrameEventRunningTotalTx",
        "ErroredFramePeriodErrorRunningTotalRx": "erroredFramePeriodErrorRunningTotalRx",
        "ErroredFramePeriodErrorRunningTotalTx": "erroredFramePeriodErrorRunningTotalTx",
        "ErroredFramePeriodEventRunningTotalRx": "erroredFramePeriodEventRunningTotalRx",
        "ErroredFramePeriodEventRunningTotalTx": "erroredFramePeriodEventRunningTotalTx",
        "ErroredFrameSSErrorRunningTotalRx": "erroredFrameSSErrorRunningTotalRx",
        "ErroredFrameSSErrorRunningTotalTx": "erroredFrameSSErrorRunningTotalTx",
        "ErroredFrameSSEventRunningTotalRx": "erroredFrameSSEventRunningTotalRx",
        "ErroredFrameSSEventRunningTotalTx": "erroredFrameSSEventRunningTotalTx",
        "ErroredSymbolPeriodErrorRunningTotalRx": "erroredSymbolPeriodErrorRunningTotalRx",
        "ErroredSymbolPeriodErrorRunningTotalTx": "erroredSymbolPeriodErrorRunningTotalTx",
        "ErroredSymbolPeriodEventRunningTotalRx": "erroredSymbolPeriodEventRunningTotalRx",
        "ErroredSymbolPeriodEventRunningTotalTx": "erroredSymbolPeriodEventRunningTotalTx",
        "EventNotificationPDURx": "eventNotificationPDURx",
        "EventNotificationPDUTx": "eventNotificationPDUTx",
        "InformationPDURx": "informationPDURx",
        "InformationPDUTx": "informationPDUTx",
        "LinkFaultRx": "linkFaultRx",
        "LinkFaultTx": "linkFaultTx",
        "LinksConfigured": "linksConfigured",
        "LinksRunning": "linksRunning",
        "LocalDiscoveryState": "localDiscoveryState",
        "LocalRevision": "localRevision",
        "LoopbackDisableControlPDURx": "loopbackDisableControlPDURx",
        "LoopbackDisableControlPDUTx": "loopbackDisableControlPDUTx",
        "LoopbackEnableControlPDURx": "loopbackEnableControlPDURx",
        "LoopbackEnableControlPDUTx": "loopbackEnableControlPDUTx",
        "OrganizationSpecificPDURx": "organizationSpecificPDURx",
        "OrganizationSpecificPDUTx": "organizationSpecificPDUTx",
        "PortName": "portName",
        "RemoteRevision": "remoteRevision",
        "SessionFlapCount": "sessionFlapCount",
        "UniqueEventNotificationPDURx": "uniqueEventNotificationPDURx",
        "UniqueEventNotificationPDUTx": "uniqueEventNotificationPDUTx",
        "UniqueInformationPDURx": "uniqueInformationPDURx",
        "UniqueInformationPDUTx": "uniqueInformationPDUTx",
        "UnsupportedPDURx": "unsupportedPDURx",
        "VariableRequestPDURx": "variableRequestPDURx",
        "VariableRequestPDUTx": "variableRequestPDUTx",
        "VariableResponsePDURx": "variableResponsePDURx",
        "VariableResponsePDUTx": "variableResponsePDUTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OamAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def CriticalEventRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Critical Event Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["CriticalEventRx"])

    @CriticalEventRx.setter
    def CriticalEventRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CriticalEventRx"], value)

    @property
    def CriticalEventTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Critical Event Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["CriticalEventTx"])

    @CriticalEventTx.setter
    def CriticalEventTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CriticalEventTx"], value)

    @property
    def DyingGaspRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Dying Gasp Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DyingGaspRx"])

    @DyingGaspRx.setter
    def DyingGaspRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DyingGaspRx"], value)

    @property
    def DyingGaspTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Dying Gasp Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DyingGaspTx"])

    @DyingGaspTx.setter
    def DyingGaspTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DyingGaspTx"], value)

    @property
    def ErroredFrameErrorRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Error Running Total Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErroredFrameErrorRunningTotalRx"])

    @ErroredFrameErrorRunningTotalRx.setter
    def ErroredFrameErrorRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErroredFrameErrorRunningTotalRx"], value)

    @property
    def ErroredFrameErrorRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Error Running Total Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErroredFrameErrorRunningTotalTx"])

    @ErroredFrameErrorRunningTotalTx.setter
    def ErroredFrameErrorRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErroredFrameErrorRunningTotalTx"], value)

    @property
    def ErroredFrameEventRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Event Running Total Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErroredFrameEventRunningTotalRx"])

    @ErroredFrameEventRunningTotalRx.setter
    def ErroredFrameEventRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErroredFrameEventRunningTotalRx"], value)

    @property
    def ErroredFrameEventRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Event Running Total Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErroredFrameEventRunningTotalTx"])

    @ErroredFrameEventRunningTotalTx.setter
    def ErroredFrameEventRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErroredFrameEventRunningTotalTx"], value)

    @property
    def ErroredFramePeriodErrorRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Period Error Running Total Rx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodErrorRunningTotalRx"]
        )

    @ErroredFramePeriodErrorRunningTotalRx.setter
    def ErroredFramePeriodErrorRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodErrorRunningTotalRx"], value
        )

    @property
    def ErroredFramePeriodErrorRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Period Error Running Total Tx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodErrorRunningTotalTx"]
        )

    @ErroredFramePeriodErrorRunningTotalTx.setter
    def ErroredFramePeriodErrorRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodErrorRunningTotalTx"], value
        )

    @property
    def ErroredFramePeriodEventRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Period Event Running Total Rx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodEventRunningTotalRx"]
        )

    @ErroredFramePeriodEventRunningTotalRx.setter
    def ErroredFramePeriodEventRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodEventRunningTotalRx"], value
        )

    @property
    def ErroredFramePeriodEventRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame Period Event Running Total Tx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodEventRunningTotalTx"]
        )

    @ErroredFramePeriodEventRunningTotalTx.setter
    def ErroredFramePeriodEventRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFramePeriodEventRunningTotalTx"], value
        )

    @property
    def ErroredFrameSSErrorRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame SS Error Running Total Rx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSErrorRunningTotalRx"]
        )

    @ErroredFrameSSErrorRunningTotalRx.setter
    def ErroredFrameSSErrorRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSErrorRunningTotalRx"], value
        )

    @property
    def ErroredFrameSSErrorRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame SS Error Running Total Tx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSErrorRunningTotalTx"]
        )

    @ErroredFrameSSErrorRunningTotalTx.setter
    def ErroredFrameSSErrorRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSErrorRunningTotalTx"], value
        )

    @property
    def ErroredFrameSSEventRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame SS Event Running Total Rx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSEventRunningTotalRx"]
        )

    @ErroredFrameSSEventRunningTotalRx.setter
    def ErroredFrameSSEventRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSEventRunningTotalRx"], value
        )

    @property
    def ErroredFrameSSEventRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Frame SS Event Running Total Tx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSEventRunningTotalTx"]
        )

    @ErroredFrameSSEventRunningTotalTx.setter
    def ErroredFrameSSEventRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredFrameSSEventRunningTotalTx"], value
        )

    @property
    def ErroredSymbolPeriodErrorRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Symbol Period Error Running Total Rx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodErrorRunningTotalRx"]
        )

    @ErroredSymbolPeriodErrorRunningTotalRx.setter
    def ErroredSymbolPeriodErrorRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodErrorRunningTotalRx"], value
        )

    @property
    def ErroredSymbolPeriodErrorRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Symbol Period Error Running Total Tx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodErrorRunningTotalTx"]
        )

    @ErroredSymbolPeriodErrorRunningTotalTx.setter
    def ErroredSymbolPeriodErrorRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodErrorRunningTotalTx"], value
        )

    @property
    def ErroredSymbolPeriodEventRunningTotalRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Symbol Period Event Running Total Rx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodEventRunningTotalRx"]
        )

    @ErroredSymbolPeriodEventRunningTotalRx.setter
    def ErroredSymbolPeriodEventRunningTotalRx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodEventRunningTotalRx"], value
        )

    @property
    def ErroredSymbolPeriodEventRunningTotalTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Symbol Period Event Running Total Tx
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodEventRunningTotalTx"]
        )

    @ErroredSymbolPeriodEventRunningTotalTx.setter
    def ErroredSymbolPeriodEventRunningTotalTx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErroredSymbolPeriodEventRunningTotalTx"], value
        )

    @property
    def EventNotificationPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Event Notification PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EventNotificationPDURx"])

    @EventNotificationPDURx.setter
    def EventNotificationPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EventNotificationPDURx"], value)

    @property
    def EventNotificationPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Event Notification PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EventNotificationPDUTx"])

    @EventNotificationPDUTx.setter
    def EventNotificationPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EventNotificationPDUTx"], value)

    @property
    def InformationPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Information PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InformationPDURx"])

    @InformationPDURx.setter
    def InformationPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InformationPDURx"], value)

    @property
    def InformationPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Information PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InformationPDUTx"])

    @InformationPDUTx.setter
    def InformationPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InformationPDUTx"], value)

    @property
    def LinkFaultRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Link Fault Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkFaultRx"])

    @LinkFaultRx.setter
    def LinkFaultRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkFaultRx"], value)

    @property
    def LinkFaultTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Link Fault Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkFaultTx"])

    @LinkFaultTx.setter
    def LinkFaultTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkFaultTx"], value)

    @property
    def LinksConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Links Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinksConfigured"])

    @LinksConfigured.setter
    def LinksConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinksConfigured"], value)

    @property
    def LinksRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Links Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinksRunning"])

    @LinksRunning.setter
    def LinksRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinksRunning"], value)

    @property
    def LocalDiscoveryState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Local Discovery State
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalDiscoveryState"])

    @LocalDiscoveryState.setter
    def LocalDiscoveryState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalDiscoveryState"], value)

    @property
    def LocalRevision(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Local Revision
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalRevision"])

    @LocalRevision.setter
    def LocalRevision(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalRevision"], value)

    @property
    def LoopbackDisableControlPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Loopback Disable Control PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackDisableControlPDURx"])

    @LoopbackDisableControlPDURx.setter
    def LoopbackDisableControlPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackDisableControlPDURx"], value)

    @property
    def LoopbackDisableControlPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Loopback Disable Control PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackDisableControlPDUTx"])

    @LoopbackDisableControlPDUTx.setter
    def LoopbackDisableControlPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackDisableControlPDUTx"], value)

    @property
    def LoopbackEnableControlPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Loopback Enable Control PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackEnableControlPDURx"])

    @LoopbackEnableControlPDURx.setter
    def LoopbackEnableControlPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackEnableControlPDURx"], value)

    @property
    def LoopbackEnableControlPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Loopback Enable Control PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackEnableControlPDUTx"])

    @LoopbackEnableControlPDUTx.setter
    def LoopbackEnableControlPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackEnableControlPDUTx"], value)

    @property
    def OrganizationSpecificPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Organization Specific PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificPDURx"])

    @OrganizationSpecificPDURx.setter
    def OrganizationSpecificPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OrganizationSpecificPDURx"], value)

    @property
    def OrganizationSpecificPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Organization Specific PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificPDUTx"])

    @OrganizationSpecificPDUTx.setter
    def OrganizationSpecificPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OrganizationSpecificPDUTx"], value)

    @property
    def PortName(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortName"])

    @PortName.setter
    def PortName(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortName"], value)

    @property
    def RemoteRevision(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Revision
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteRevision"])

    @RemoteRevision.setter
    def RemoteRevision(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteRevision"], value)

    @property
    def SessionFlapCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Session Flap Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionFlapCount"])

    @SessionFlapCount.setter
    def SessionFlapCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionFlapCount"], value)

    @property
    def UniqueEventNotificationPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unique Event Notification PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UniqueEventNotificationPDURx"])

    @UniqueEventNotificationPDURx.setter
    def UniqueEventNotificationPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UniqueEventNotificationPDURx"], value)

    @property
    def UniqueEventNotificationPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unique Event Notification PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UniqueEventNotificationPDUTx"])

    @UniqueEventNotificationPDUTx.setter
    def UniqueEventNotificationPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UniqueEventNotificationPDUTx"], value)

    @property
    def UniqueInformationPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unique Information PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UniqueInformationPDURx"])

    @UniqueInformationPDURx.setter
    def UniqueInformationPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UniqueInformationPDURx"], value)

    @property
    def UniqueInformationPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unique Information PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UniqueInformationPDUTx"])

    @UniqueInformationPDUTx.setter
    def UniqueInformationPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UniqueInformationPDUTx"], value)

    @property
    def UnsupportedPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unsupported PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnsupportedPDURx"])

    @UnsupportedPDURx.setter
    def UnsupportedPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnsupportedPDURx"], value)

    @property
    def VariableRequestPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Variable Request PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VariableRequestPDURx"])

    @VariableRequestPDURx.setter
    def VariableRequestPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VariableRequestPDURx"], value)

    @property
    def VariableRequestPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Variable Request PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VariableRequestPDUTx"])

    @VariableRequestPDUTx.setter
    def VariableRequestPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VariableRequestPDUTx"], value)

    @property
    def VariableResponsePDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Variable Response PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VariableResponsePDURx"])

    @VariableResponsePDURx.setter
    def VariableResponsePDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VariableResponsePDURx"], value)

    @property
    def VariableResponsePDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Variable Response PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VariableResponsePDUTx"])

    @VariableResponsePDUTx.setter
    def VariableResponsePDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VariableResponsePDUTx"], value)

    def update(
        self,
        CriticalEventRx=None,
        CriticalEventTx=None,
        DyingGaspRx=None,
        DyingGaspTx=None,
        ErroredFrameErrorRunningTotalRx=None,
        ErroredFrameErrorRunningTotalTx=None,
        ErroredFrameEventRunningTotalRx=None,
        ErroredFrameEventRunningTotalTx=None,
        ErroredFramePeriodErrorRunningTotalRx=None,
        ErroredFramePeriodErrorRunningTotalTx=None,
        ErroredFramePeriodEventRunningTotalRx=None,
        ErroredFramePeriodEventRunningTotalTx=None,
        ErroredFrameSSErrorRunningTotalRx=None,
        ErroredFrameSSErrorRunningTotalTx=None,
        ErroredFrameSSEventRunningTotalRx=None,
        ErroredFrameSSEventRunningTotalTx=None,
        ErroredSymbolPeriodErrorRunningTotalRx=None,
        ErroredSymbolPeriodErrorRunningTotalTx=None,
        ErroredSymbolPeriodEventRunningTotalRx=None,
        ErroredSymbolPeriodEventRunningTotalTx=None,
        EventNotificationPDURx=None,
        EventNotificationPDUTx=None,
        InformationPDURx=None,
        InformationPDUTx=None,
        LinkFaultRx=None,
        LinkFaultTx=None,
        LinksConfigured=None,
        LinksRunning=None,
        LocalDiscoveryState=None,
        LocalRevision=None,
        LoopbackDisableControlPDURx=None,
        LoopbackDisableControlPDUTx=None,
        LoopbackEnableControlPDURx=None,
        LoopbackEnableControlPDUTx=None,
        OrganizationSpecificPDURx=None,
        OrganizationSpecificPDUTx=None,
        PortName=None,
        RemoteRevision=None,
        SessionFlapCount=None,
        UniqueEventNotificationPDURx=None,
        UniqueEventNotificationPDUTx=None,
        UniqueInformationPDURx=None,
        UniqueInformationPDUTx=None,
        UnsupportedPDURx=None,
        VariableRequestPDURx=None,
        VariableRequestPDUTx=None,
        VariableResponsePDURx=None,
        VariableResponsePDUTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> OamAggregatedStatistics
        """Updates oamAggregatedStatistics resource on the server.

        Args
        ----
        - CriticalEventRx (bool): Critical Event Rx
        - CriticalEventTx (bool): Critical Event Tx
        - DyingGaspRx (bool): Dying Gasp Rx
        - DyingGaspTx (bool): Dying Gasp Tx
        - ErroredFrameErrorRunningTotalRx (bool): Errored Frame Error Running Total Rx
        - ErroredFrameErrorRunningTotalTx (bool): Errored Frame Error Running Total Tx
        - ErroredFrameEventRunningTotalRx (bool): Errored Frame Event Running Total Rx
        - ErroredFrameEventRunningTotalTx (bool): Errored Frame Event Running Total Tx
        - ErroredFramePeriodErrorRunningTotalRx (bool): Errored Frame Period Error Running Total Rx
        - ErroredFramePeriodErrorRunningTotalTx (bool): Errored Frame Period Error Running Total Tx
        - ErroredFramePeriodEventRunningTotalRx (bool): Errored Frame Period Event Running Total Rx
        - ErroredFramePeriodEventRunningTotalTx (bool): Errored Frame Period Event Running Total Tx
        - ErroredFrameSSErrorRunningTotalRx (bool): Errored Frame SS Error Running Total Rx
        - ErroredFrameSSErrorRunningTotalTx (bool): Errored Frame SS Error Running Total Tx
        - ErroredFrameSSEventRunningTotalRx (bool): Errored Frame SS Event Running Total Rx
        - ErroredFrameSSEventRunningTotalTx (bool): Errored Frame SS Event Running Total Tx
        - ErroredSymbolPeriodErrorRunningTotalRx (bool): Errored Symbol Period Error Running Total Rx
        - ErroredSymbolPeriodErrorRunningTotalTx (bool): Errored Symbol Period Error Running Total Tx
        - ErroredSymbolPeriodEventRunningTotalRx (bool): Errored Symbol Period Event Running Total Rx
        - ErroredSymbolPeriodEventRunningTotalTx (bool): Errored Symbol Period Event Running Total Tx
        - EventNotificationPDURx (bool): Event Notification PDU Rx
        - EventNotificationPDUTx (bool): Event Notification PDU Tx
        - InformationPDURx (bool): Information PDU Rx
        - InformationPDUTx (bool): Information PDU Tx
        - LinkFaultRx (bool): Link Fault Rx
        - LinkFaultTx (bool): Link Fault Tx
        - LinksConfigured (bool): Links Configured
        - LinksRunning (bool): Links Running
        - LocalDiscoveryState (bool): Local Discovery State
        - LocalRevision (bool): Local Revision
        - LoopbackDisableControlPDURx (bool): Loopback Disable Control PDU Rx
        - LoopbackDisableControlPDUTx (bool): Loopback Disable Control PDU Tx
        - LoopbackEnableControlPDURx (bool): Loopback Enable Control PDU Rx
        - LoopbackEnableControlPDUTx (bool): Loopback Enable Control PDU Tx
        - OrganizationSpecificPDURx (bool): Organization Specific PDU Rx
        - OrganizationSpecificPDUTx (bool): Organization Specific PDU Tx
        - PortName (bool): Port Name
        - RemoteRevision (bool): Remote Revision
        - SessionFlapCount (bool): Session Flap Count
        - UniqueEventNotificationPDURx (bool): Unique Event Notification PDU Rx
        - UniqueEventNotificationPDUTx (bool): Unique Event Notification PDU Tx
        - UniqueInformationPDURx (bool): Unique Information PDU Rx
        - UniqueInformationPDUTx (bool): Unique Information PDU Tx
        - UnsupportedPDURx (bool): Unsupported PDU Rx
        - VariableRequestPDURx (bool): Variable Request PDU Rx
        - VariableRequestPDUTx (bool): Variable Request PDU Tx
        - VariableResponsePDURx (bool): Variable Response PDU Rx
        - VariableResponsePDUTx (bool): Variable Response PDU Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CriticalEventRx=None,
        CriticalEventTx=None,
        DyingGaspRx=None,
        DyingGaspTx=None,
        ErroredFrameErrorRunningTotalRx=None,
        ErroredFrameErrorRunningTotalTx=None,
        ErroredFrameEventRunningTotalRx=None,
        ErroredFrameEventRunningTotalTx=None,
        ErroredFramePeriodErrorRunningTotalRx=None,
        ErroredFramePeriodErrorRunningTotalTx=None,
        ErroredFramePeriodEventRunningTotalRx=None,
        ErroredFramePeriodEventRunningTotalTx=None,
        ErroredFrameSSErrorRunningTotalRx=None,
        ErroredFrameSSErrorRunningTotalTx=None,
        ErroredFrameSSEventRunningTotalRx=None,
        ErroredFrameSSEventRunningTotalTx=None,
        ErroredSymbolPeriodErrorRunningTotalRx=None,
        ErroredSymbolPeriodErrorRunningTotalTx=None,
        ErroredSymbolPeriodEventRunningTotalRx=None,
        ErroredSymbolPeriodEventRunningTotalTx=None,
        EventNotificationPDURx=None,
        EventNotificationPDUTx=None,
        InformationPDURx=None,
        InformationPDUTx=None,
        LinkFaultRx=None,
        LinkFaultTx=None,
        LinksConfigured=None,
        LinksRunning=None,
        LocalDiscoveryState=None,
        LocalRevision=None,
        LoopbackDisableControlPDURx=None,
        LoopbackDisableControlPDUTx=None,
        LoopbackEnableControlPDURx=None,
        LoopbackEnableControlPDUTx=None,
        OrganizationSpecificPDURx=None,
        OrganizationSpecificPDUTx=None,
        PortName=None,
        RemoteRevision=None,
        SessionFlapCount=None,
        UniqueEventNotificationPDURx=None,
        UniqueEventNotificationPDUTx=None,
        UniqueInformationPDURx=None,
        UniqueInformationPDUTx=None,
        UnsupportedPDURx=None,
        VariableRequestPDURx=None,
        VariableRequestPDUTx=None,
        VariableResponsePDURx=None,
        VariableResponsePDUTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> OamAggregatedStatistics
        """Finds and retrieves oamAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve oamAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all oamAggregatedStatistics resources from the server.

        Args
        ----
        - CriticalEventRx (bool): Critical Event Rx
        - CriticalEventTx (bool): Critical Event Tx
        - DyingGaspRx (bool): Dying Gasp Rx
        - DyingGaspTx (bool): Dying Gasp Tx
        - ErroredFrameErrorRunningTotalRx (bool): Errored Frame Error Running Total Rx
        - ErroredFrameErrorRunningTotalTx (bool): Errored Frame Error Running Total Tx
        - ErroredFrameEventRunningTotalRx (bool): Errored Frame Event Running Total Rx
        - ErroredFrameEventRunningTotalTx (bool): Errored Frame Event Running Total Tx
        - ErroredFramePeriodErrorRunningTotalRx (bool): Errored Frame Period Error Running Total Rx
        - ErroredFramePeriodErrorRunningTotalTx (bool): Errored Frame Period Error Running Total Tx
        - ErroredFramePeriodEventRunningTotalRx (bool): Errored Frame Period Event Running Total Rx
        - ErroredFramePeriodEventRunningTotalTx (bool): Errored Frame Period Event Running Total Tx
        - ErroredFrameSSErrorRunningTotalRx (bool): Errored Frame SS Error Running Total Rx
        - ErroredFrameSSErrorRunningTotalTx (bool): Errored Frame SS Error Running Total Tx
        - ErroredFrameSSEventRunningTotalRx (bool): Errored Frame SS Event Running Total Rx
        - ErroredFrameSSEventRunningTotalTx (bool): Errored Frame SS Event Running Total Tx
        - ErroredSymbolPeriodErrorRunningTotalRx (bool): Errored Symbol Period Error Running Total Rx
        - ErroredSymbolPeriodErrorRunningTotalTx (bool): Errored Symbol Period Error Running Total Tx
        - ErroredSymbolPeriodEventRunningTotalRx (bool): Errored Symbol Period Event Running Total Rx
        - ErroredSymbolPeriodEventRunningTotalTx (bool): Errored Symbol Period Event Running Total Tx
        - EventNotificationPDURx (bool): Event Notification PDU Rx
        - EventNotificationPDUTx (bool): Event Notification PDU Tx
        - InformationPDURx (bool): Information PDU Rx
        - InformationPDUTx (bool): Information PDU Tx
        - LinkFaultRx (bool): Link Fault Rx
        - LinkFaultTx (bool): Link Fault Tx
        - LinksConfigured (bool): Links Configured
        - LinksRunning (bool): Links Running
        - LocalDiscoveryState (bool): Local Discovery State
        - LocalRevision (bool): Local Revision
        - LoopbackDisableControlPDURx (bool): Loopback Disable Control PDU Rx
        - LoopbackDisableControlPDUTx (bool): Loopback Disable Control PDU Tx
        - LoopbackEnableControlPDURx (bool): Loopback Enable Control PDU Rx
        - LoopbackEnableControlPDUTx (bool): Loopback Enable Control PDU Tx
        - OrganizationSpecificPDURx (bool): Organization Specific PDU Rx
        - OrganizationSpecificPDUTx (bool): Organization Specific PDU Tx
        - PortName (bool): Port Name
        - RemoteRevision (bool): Remote Revision
        - SessionFlapCount (bool): Session Flap Count
        - UniqueEventNotificationPDURx (bool): Unique Event Notification PDU Rx
        - UniqueEventNotificationPDUTx (bool): Unique Event Notification PDU Tx
        - UniqueInformationPDURx (bool): Unique Information PDU Rx
        - UniqueInformationPDUTx (bool): Unique Information PDU Tx
        - UnsupportedPDURx (bool): Unsupported PDU Rx
        - VariableRequestPDURx (bool): Variable Request PDU Rx
        - VariableRequestPDUTx (bool): Variable Request PDU Tx
        - VariableResponsePDURx (bool): Variable Response PDU Rx
        - VariableResponsePDUTx (bool): Variable Response PDU Tx

        Returns
        -------
        - self: This instance with matching oamAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of oamAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the oamAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
