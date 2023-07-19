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


class Capture(Base):
    """Allows the user to set the default behavior of the capture operation.
    The Capture class encapsulates a required capture resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "capture"
    _SDM_ATT_MAP = {
        "AfterTriggerFilter": "afterTriggerFilter",
        "BeforeTriggerFilter": "beforeTriggerFilter",
        "CaptureMode": "captureMode",
        "ContinuousFilters": "continuousFilters",
        "ControlActiveCapture": "controlActiveCapture",
        "ControlBufferBehaviour": "controlBufferBehaviour",
        "ControlBufferSize": "controlBufferSize",
        "ControlCaptureFilter": "controlCaptureFilter",
        "ControlCaptureState": "controlCaptureState",
        "ControlCaptureTrigger": "controlCaptureTrigger",
        "ControlCapturedPacketCounter": "controlCapturedPacketCounter",
        "ControlCaptures": "controlCaptures",
        "ControlDecodeAsCurrentFilter": "controlDecodeAsCurrentFilter",
        "ControlInterfaceType": "controlInterfaceType",
        "ControlPacketCounter": "controlPacketCounter",
        "ControlSliceSize": "controlSliceSize",
        "DataActiveCapture": "dataActiveCapture",
        "DataCapturePacketWindowEnabled": "dataCapturePacketWindowEnabled",
        "DataCapturePacketWindowEndIndex": "dataCapturePacketWindowEndIndex",
        "DataCapturePacketWindowStartIndex": "dataCapturePacketWindowStartIndex",
        "DataCaptureState": "dataCaptureState",
        "DataCapturedPacketCounter": "dataCapturedPacketCounter",
        "DataCaptures": "dataCaptures",
        "DataDecodeAsCurrentFilter": "dataDecodeAsCurrentFilter",
        "DataPacketCounter": "dataPacketCounter",
        "DataReceiveTimestamp": "dataReceiveTimestamp",
        "DecodeAsLinkProtocols": "decodeAsLinkProtocols",
        "DecodeAsNetworkProtocols": "decodeAsNetworkProtocols",
        "DecodeAsTransportProtocols": "decodeAsTransportProtocols",
        "DisplayFiltersControlCapture": "displayFiltersControlCapture",
        "DisplayFiltersDataCapture": "displayFiltersDataCapture",
        "HardwareEnabled": "hardwareEnabled",
        "IsCaptureRunning": "isCaptureRunning",
        "IsControlCaptureRunning": "isControlCaptureRunning",
        "IsDataCaptureRunning": "isDataCaptureRunning",
        "SliceSize": "sliceSize",
        "SoftwareEnabled": "softwareEnabled",
        "TriggerPosition": "triggerPosition",
    }
    _SDM_ENUM_MAP = {
        "afterTriggerFilter": [
            "captureAfterTriggerAll",
            "captureAfterTriggerConditionFilter",
            "captureAfterTriggerFilter",
        ],
        "beforeTriggerFilter": [
            "captureBeforeTriggerAll",
            "captureBeforeTriggerFilter",
            "captureBeforeTriggerNone",
        ],
        "captureMode": ["captureContinuousMode", "captureTriggerMode"],
        "continuousFilters": ["captureContinuousAll", "captureContinuousFilter"],
        "controlBufferBehaviour": [
            "bufferAfterStopCircular",
            "bufferAfterStopNonCircular",
            "bufferLiveCircular",
            "bufferLiveNonCircular",
        ],
        "controlCaptureState": ["notReady", "ready"],
        "controlInterfaceType": ["anyInterface", "specificInterface"],
        "dataCaptureState": ["notReady", "ready"],
        "dataReceiveTimestamp": ["chassisUtcTime", "hwTimestamp"],
    }

    def __init__(self, parent, list_op=False):
        super(Capture, self).__init__(parent, list_op)

    @property
    def CurrentPacket(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.currentpacket.currentpacket.CurrentPacket): An instance of the CurrentPacket class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.currentpacket.currentpacket import (
            CurrentPacket,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CurrentPacket", None) is not None:
                return self._properties.get("CurrentPacket")
        return CurrentPacket(self)._select()

    @property
    def Filter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.filter.filter.Filter): An instance of the Filter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.filter.filter import (
            Filter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Filter", None) is not None:
                return self._properties.get("Filter")
        return Filter(self)._select()

    @property
    def FilterPallette(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.filterpallette.filterpallette.FilterPallette): An instance of the FilterPallette class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.filterpallette.filterpallette import (
            FilterPallette,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FilterPallette", None) is not None:
                return self._properties.get("FilterPallette")
        return FilterPallette(self)._select()

    @property
    def Trigger(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.trigger.trigger.Trigger): An instance of the Trigger class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.trigger.trigger import (
            Trigger,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Trigger", None) is not None:
                return self._properties.get("Trigger")
        return Trigger(self)._select()

    @property
    def AfterTriggerFilter(self):
        # type: () -> str
        """
        Returns
        -------
        - str(captureAfterTriggerAll | captureAfterTriggerConditionFilter | captureAfterTriggerFilter): Controls the capture of data after triggering when operating in triggered mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AfterTriggerFilter"])

    @AfterTriggerFilter.setter
    def AfterTriggerFilter(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AfterTriggerFilter"], value)

    @property
    def BeforeTriggerFilter(self):
        # type: () -> str
        """
        Returns
        -------
        - str(captureBeforeTriggerAll | captureBeforeTriggerFilter | captureBeforeTriggerNone): Controls the capture of data prior to triggering when operating in triggered mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["BeforeTriggerFilter"])

    @BeforeTriggerFilter.setter
    def BeforeTriggerFilter(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BeforeTriggerFilter"], value)

    @property
    def CaptureMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(captureContinuousMode | captureTriggerMode): Controls whether data capture is performed in a continuous or triggered mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CaptureMode"])

    @CaptureMode.setter
    def CaptureMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CaptureMode"], value)

    @property
    def ContinuousFilters(self):
        # type: () -> str
        """
        Returns
        -------
        - str(captureContinuousAll | captureContinuousFilter): Controls the circular buffer behaviour: continuous capture of all received packets or continuous capture of received packets which match the filter conditions applied.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ContinuousFilters"])

    @ContinuousFilters.setter
    def ContinuousFilters(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ContinuousFilters"], value)

    @property
    def ControlActiveCapture(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the active control capture (if any).The active control capture is the last one made on the port by default; but the user can change it using this attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlActiveCapture"])

    @ControlActiveCapture.setter
    def ControlActiveCapture(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlActiveCapture"], value)

    @property
    def ControlBufferBehaviour(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bufferAfterStopCircular | bufferAfterStopNonCircular | bufferLiveCircular | bufferLiveNonCircular): Sets the control capture buffer behavior.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlBufferBehaviour"])

    @ControlBufferBehaviour.setter
    def ControlBufferBehaviour(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlBufferBehaviour"], value)

    @property
    def ControlBufferSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the size(%) of the ports memory used by the control capture.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlBufferSize"])

    @ControlBufferSize.setter
    def ControlBufferSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlBufferSize"], value)

    @property
    def ControlCaptureFilter(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Controls the dividing line within the capture buffer between before trigger data and post trigger data.This control is only useful in triggered mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlCaptureFilter"])

    @ControlCaptureFilter.setter
    def ControlCaptureFilter(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlCaptureFilter"], value)

    @property
    def ControlCaptureState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(notReady | ready): Current state of the control capture (if there are packets uploading in GUI or not).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlCaptureState"])

    @property
    def ControlCaptureTrigger(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This is the control Trigger string.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlCaptureTrigger"])

    @ControlCaptureTrigger.setter
    def ControlCaptureTrigger(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlCaptureTrigger"], value)

    @property
    def ControlCapturedPacketCounter(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlCapturedPacketCounter"])

    @property
    def ControlCaptures(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of control captures which are available for the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlCaptures"])

    @property
    def ControlDecodeAsCurrentFilter(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The control capture decode as filter used by last decode as operation (if any).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlDecodeAsCurrentFilter"])

    @property
    def ControlInterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(anyInterface | specificInterface): Enables control capture on the desired interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlInterfaceType"])

    @ControlInterfaceType.setter
    def ControlInterfaceType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlInterfaceType"], value)

    @property
    def ControlPacketCounter(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Shows the number of control capture packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlPacketCounter"])

    @property
    def ControlSliceSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the size of the control capture slices.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlSliceSize"])

    @ControlSliceSize.setter
    def ControlSliceSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlSliceSize"], value)

    @property
    def DataActiveCapture(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the active data capture (if any). The active data capture is the last one made on the port by default; but the user can change it using this attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataActiveCapture"])

    @DataActiveCapture.setter
    def DataActiveCapture(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataActiveCapture"], value)

    @property
    def DataCapturePacketWindowEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if the packet window is enabled for the current capture.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataCapturePacketWindowEnabled"])

    @DataCapturePacketWindowEnabled.setter
    def DataCapturePacketWindowEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataCapturePacketWindowEnabled"], value)

    @property
    def DataCapturePacketWindowEndIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the end index of the packet window.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataCapturePacketWindowEndIndex"])

    @DataCapturePacketWindowEndIndex.setter
    def DataCapturePacketWindowEndIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataCapturePacketWindowEndIndex"], value)

    @property
    def DataCapturePacketWindowStartIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the start index of the packet window.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DataCapturePacketWindowStartIndex"]
        )

    @DataCapturePacketWindowStartIndex.setter
    def DataCapturePacketWindowStartIndex(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["DataCapturePacketWindowStartIndex"], value
        )

    @property
    def DataCaptureState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(notReady | ready): Current state of the data capture; ready if all packets have been uploaded on client or notReady if packet uploading is in progress.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataCaptureState"])

    @property
    def DataCapturedPacketCounter(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataCapturedPacketCounter"])

    @property
    def DataCaptures(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of data captures which are available for the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataCaptures"])

    @property
    def DataDecodeAsCurrentFilter(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data capture decode as filter used by last decode as operation (if any).
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataDecodeAsCurrentFilter"])

    @property
    def DataPacketCounter(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Shows the number of data capture packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPacketCounter"])

    @property
    def DataReceiveTimestamp(self):
        # type: () -> str
        """
        Returns
        -------
        - str(chassisUtcTime | hwTimestamp): Controls whether the data capture packets timestamp are using the chassis UTC time or the HW timestamp.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataReceiveTimestamp"])

    @DataReceiveTimestamp.setter
    def DataReceiveTimestamp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataReceiveTimestamp"], value)

    @property
    def DecodeAsLinkProtocols(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List with link protocols available for capture decode as operation. Need to have an active capture to retrieve the property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DecodeAsLinkProtocols"])

    @property
    def DecodeAsNetworkProtocols(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List with network protocols available for capture decode as operation. Need to have an active capture to retrieve the property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DecodeAsNetworkProtocols"])

    @property
    def DecodeAsTransportProtocols(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List with transport protocols available for capture decode as operation. Need to have an active capture to retrieve the property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DecodeAsTransportProtocols"])

    @property
    def DisplayFiltersControlCapture(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Displays the packet filter set inside the control capture that is used to filter the already captured packets
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisplayFiltersControlCapture"])

    @DisplayFiltersControlCapture.setter
    def DisplayFiltersControlCapture(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisplayFiltersControlCapture"], value)

    @property
    def DisplayFiltersDataCapture(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Displays the packet filter set inside the data capture that is used to filter the already captured packets
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisplayFiltersDataCapture"])

    @DisplayFiltersDataCapture.setter
    def DisplayFiltersDataCapture(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisplayFiltersDataCapture"], value)

    @property
    def HardwareEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the capture of data plane traffic. Note that in order for data traffic to be captured, the vport attritbute -rxMode must be set to capture.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HardwareEnabled"])

    @HardwareEnabled.setter
    def HardwareEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HardwareEnabled"], value)

    @property
    def IsCaptureRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if the capture is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsCaptureRunning"])

    @property
    def IsControlCaptureRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if the control capture is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsControlCaptureRunning"])

    @property
    def IsDataCaptureRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if the data capture is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsDataCaptureRunning"])

    @property
    def SliceSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The size of the capture slice.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SliceSize"])

    @SliceSize.setter
    def SliceSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SliceSize"], value)

    @property
    def SoftwareEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the capture of control plane traffic. Note that in order for control traffic to be captured, the vport attritbute -rxMode must be set to capture.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SoftwareEnabled"])

    @SoftwareEnabled.setter
    def SoftwareEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SoftwareEnabled"], value)

    @property
    def TriggerPosition(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Controls the dividing line within the capture buffer between before trigger data and post trigger data. This control is only useful in triggered mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerPosition"])

    @TriggerPosition.setter
    def TriggerPosition(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerPosition"], value)

    def update(
        self,
        AfterTriggerFilter=None,
        BeforeTriggerFilter=None,
        CaptureMode=None,
        ContinuousFilters=None,
        ControlActiveCapture=None,
        ControlBufferBehaviour=None,
        ControlBufferSize=None,
        ControlCaptureFilter=None,
        ControlCaptureTrigger=None,
        ControlInterfaceType=None,
        ControlSliceSize=None,
        DataActiveCapture=None,
        DataCapturePacketWindowEnabled=None,
        DataCapturePacketWindowEndIndex=None,
        DataCapturePacketWindowStartIndex=None,
        DataReceiveTimestamp=None,
        DisplayFiltersControlCapture=None,
        DisplayFiltersDataCapture=None,
        HardwareEnabled=None,
        SliceSize=None,
        SoftwareEnabled=None,
        TriggerPosition=None,
    ):
        # type: (str, str, str, str, str, str, int, str, str, str, int, str, bool, int, int, str, str, str, bool, int, bool, int) -> Capture
        """Updates capture resource on the server.

        Args
        ----
        - AfterTriggerFilter (str(captureAfterTriggerAll | captureAfterTriggerConditionFilter | captureAfterTriggerFilter)): Controls the capture of data after triggering when operating in triggered mode.
        - BeforeTriggerFilter (str(captureBeforeTriggerAll | captureBeforeTriggerFilter | captureBeforeTriggerNone)): Controls the capture of data prior to triggering when operating in triggered mode
        - CaptureMode (str(captureContinuousMode | captureTriggerMode)): Controls whether data capture is performed in a continuous or triggered mode.
        - ContinuousFilters (str(captureContinuousAll | captureContinuousFilter)): Controls the circular buffer behaviour: continuous capture of all received packets or continuous capture of received packets which match the filter conditions applied.
        - ControlActiveCapture (str): The name of the active control capture (if any).The active control capture is the last one made on the port by default; but the user can change it using this attribute.
        - ControlBufferBehaviour (str(bufferAfterStopCircular | bufferAfterStopNonCircular | bufferLiveCircular | bufferLiveNonCircular)): Sets the control capture buffer behavior.
        - ControlBufferSize (number): Sets the size(%) of the ports memory used by the control capture.
        - ControlCaptureFilter (str): Controls the dividing line within the capture buffer between before trigger data and post trigger data.This control is only useful in triggered mode.
        - ControlCaptureTrigger (str): This is the control Trigger string.
        - ControlInterfaceType (str(anyInterface | specificInterface)): Enables control capture on the desired interfaces.
        - ControlSliceSize (number): Sets the size of the control capture slices.
        - DataActiveCapture (str): The name of the active data capture (if any). The active data capture is the last one made on the port by default; but the user can change it using this attribute.
        - DataCapturePacketWindowEnabled (bool): Indicates if the packet window is enabled for the current capture.
        - DataCapturePacketWindowEndIndex (number): Sets the end index of the packet window.
        - DataCapturePacketWindowStartIndex (number): Sets the start index of the packet window.
        - DataReceiveTimestamp (str(chassisUtcTime | hwTimestamp)): Controls whether the data capture packets timestamp are using the chassis UTC time or the HW timestamp.
        - DisplayFiltersControlCapture (str): Displays the packet filter set inside the control capture that is used to filter the already captured packets
        - DisplayFiltersDataCapture (str): Displays the packet filter set inside the data capture that is used to filter the already captured packets
        - HardwareEnabled (bool): If true, enables the capture of data plane traffic. Note that in order for data traffic to be captured, the vport attritbute -rxMode must be set to capture.
        - SliceSize (number): The size of the capture slice.
        - SoftwareEnabled (bool): If true, enables the capture of control plane traffic. Note that in order for control traffic to be captured, the vport attritbute -rxMode must be set to capture.
        - TriggerPosition (number): Controls the dividing line within the capture buffer between before trigger data and post trigger data. This control is only useful in triggered mode.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AfterTriggerFilter=None,
        BeforeTriggerFilter=None,
        CaptureMode=None,
        ContinuousFilters=None,
        ControlActiveCapture=None,
        ControlBufferBehaviour=None,
        ControlBufferSize=None,
        ControlCaptureFilter=None,
        ControlCaptureState=None,
        ControlCaptureTrigger=None,
        ControlCapturedPacketCounter=None,
        ControlCaptures=None,
        ControlDecodeAsCurrentFilter=None,
        ControlInterfaceType=None,
        ControlPacketCounter=None,
        ControlSliceSize=None,
        DataActiveCapture=None,
        DataCapturePacketWindowEnabled=None,
        DataCapturePacketWindowEndIndex=None,
        DataCapturePacketWindowStartIndex=None,
        DataCaptureState=None,
        DataCapturedPacketCounter=None,
        DataCaptures=None,
        DataDecodeAsCurrentFilter=None,
        DataPacketCounter=None,
        DataReceiveTimestamp=None,
        DecodeAsLinkProtocols=None,
        DecodeAsNetworkProtocols=None,
        DecodeAsTransportProtocols=None,
        DisplayFiltersControlCapture=None,
        DisplayFiltersDataCapture=None,
        HardwareEnabled=None,
        IsCaptureRunning=None,
        IsControlCaptureRunning=None,
        IsDataCaptureRunning=None,
        SliceSize=None,
        SoftwareEnabled=None,
        TriggerPosition=None,
    ):
        # type: (str, str, str, str, str, str, int, str, str, str, int, str, str, str, int, int, str, bool, int, int, str, int, str, str, int, str, List[str], List[str], List[str], str, str, bool, bool, bool, bool, int, bool, int) -> Capture
        """Finds and retrieves capture resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve capture resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all capture resources from the server.

        Args
        ----
        - AfterTriggerFilter (str(captureAfterTriggerAll | captureAfterTriggerConditionFilter | captureAfterTriggerFilter)): Controls the capture of data after triggering when operating in triggered mode.
        - BeforeTriggerFilter (str(captureBeforeTriggerAll | captureBeforeTriggerFilter | captureBeforeTriggerNone)): Controls the capture of data prior to triggering when operating in triggered mode
        - CaptureMode (str(captureContinuousMode | captureTriggerMode)): Controls whether data capture is performed in a continuous or triggered mode.
        - ContinuousFilters (str(captureContinuousAll | captureContinuousFilter)): Controls the circular buffer behaviour: continuous capture of all received packets or continuous capture of received packets which match the filter conditions applied.
        - ControlActiveCapture (str): The name of the active control capture (if any).The active control capture is the last one made on the port by default; but the user can change it using this attribute.
        - ControlBufferBehaviour (str(bufferAfterStopCircular | bufferAfterStopNonCircular | bufferLiveCircular | bufferLiveNonCircular)): Sets the control capture buffer behavior.
        - ControlBufferSize (number): Sets the size(%) of the ports memory used by the control capture.
        - ControlCaptureFilter (str): Controls the dividing line within the capture buffer between before trigger data and post trigger data.This control is only useful in triggered mode.
        - ControlCaptureState (str(notReady | ready)): Current state of the control capture (if there are packets uploading in GUI or not).
        - ControlCaptureTrigger (str): This is the control Trigger string.
        - ControlCapturedPacketCounter (number):
        - ControlCaptures (str): The list of control captures which are available for the port.
        - ControlDecodeAsCurrentFilter (str): The control capture decode as filter used by last decode as operation (if any).
        - ControlInterfaceType (str(anyInterface | specificInterface)): Enables control capture on the desired interfaces.
        - ControlPacketCounter (number): Shows the number of control capture packets.
        - ControlSliceSize (number): Sets the size of the control capture slices.
        - DataActiveCapture (str): The name of the active data capture (if any). The active data capture is the last one made on the port by default; but the user can change it using this attribute.
        - DataCapturePacketWindowEnabled (bool): Indicates if the packet window is enabled for the current capture.
        - DataCapturePacketWindowEndIndex (number): Sets the end index of the packet window.
        - DataCapturePacketWindowStartIndex (number): Sets the start index of the packet window.
        - DataCaptureState (str(notReady | ready)): Current state of the data capture; ready if all packets have been uploaded on client or notReady if packet uploading is in progress.
        - DataCapturedPacketCounter (number):
        - DataCaptures (str): The list of data captures which are available for the port.
        - DataDecodeAsCurrentFilter (str): The data capture decode as filter used by last decode as operation (if any).
        - DataPacketCounter (number): Shows the number of data capture packets.
        - DataReceiveTimestamp (str(chassisUtcTime | hwTimestamp)): Controls whether the data capture packets timestamp are using the chassis UTC time or the HW timestamp.
        - DecodeAsLinkProtocols (list(str)): List with link protocols available for capture decode as operation. Need to have an active capture to retrieve the property.
        - DecodeAsNetworkProtocols (list(str)): List with network protocols available for capture decode as operation. Need to have an active capture to retrieve the property.
        - DecodeAsTransportProtocols (list(str)): List with transport protocols available for capture decode as operation. Need to have an active capture to retrieve the property.
        - DisplayFiltersControlCapture (str): Displays the packet filter set inside the control capture that is used to filter the already captured packets
        - DisplayFiltersDataCapture (str): Displays the packet filter set inside the data capture that is used to filter the already captured packets
        - HardwareEnabled (bool): If true, enables the capture of data plane traffic. Note that in order for data traffic to be captured, the vport attritbute -rxMode must be set to capture.
        - IsCaptureRunning (bool): Indicates if the capture is running.
        - IsControlCaptureRunning (bool): Indicates if the control capture is running.
        - IsDataCaptureRunning (bool): Indicates if the data capture is running.
        - SliceSize (number): The size of the capture slice.
        - SoftwareEnabled (bool): If true, enables the capture of control plane traffic. Note that in order for control traffic to be captured, the vport attritbute -rxMode must be set to capture.
        - TriggerPosition (number): Controls the dividing line within the capture buffer between before trigger data and post trigger data. This control is only useful in triggered mode.

        Returns
        -------
        - self: This instance with matching capture resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of capture data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the capture resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def DecodeAsApply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the decodeAsApply operation on the server.

        The command forces a re-dissection of all packets based on a filter condition. (similar with Decode As from Wireshark)

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        decodeAsApply(Arg2=enum, Arg3=enum, Arg4=number, Arg5=string, async_operation=bool)
        -----------------------------------------------------------------------------------
        - Arg2 (str(control | data)): The capture type, could be either control or data.
        - Arg3 (str(link | network | transport)): Specifies the network layer at witch the command should take place.
        - Arg4 (number): Could be the TCP port for Transport layer (either source or destination), IP protocol for Network layer or Ethertype for Link layer.
        - Arg5 (str): The protocol name to re-dissect as.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        decodeAsApply(Arg2=enum, Arg3=enum, Arg4=number, Arg5=enum, Arg6=number, Arg7=string, async_operation=bool)
        -----------------------------------------------------------------------------------------------------------
        - Arg2 (str(control | data)): The capture type, could be either control or data.
        - Arg3 (str(transport)): The transport layer.
        - Arg4 (number): The TCP source port.
        - Arg5 (str(transport)): The transport layer.
        - Arg6 (number): The TCP destination port.
        - Arg7 (str): The protocol name to re-dissect as.
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
        return self._execute("decodeAsApply", payload=payload, response_object=None)

    def DecodeAsClear(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the decodeAsClear operation on the server.

        The command clears the dissection filter set by DecodeAsApply command.

        decodeAsClear(Arg2=enum, async_operation=bool)
        ----------------------------------------------
        - Arg2 (str(control | data)): The capture type, could be either control or data
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
        return self._execute("decodeAsClear", payload=payload, response_object=None)

    def MergeCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the mergeCapture operation on the server.

        The command merges two online captures.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mergeCapture(Arg2=enum, Arg3=href, Arg4=enum, Arg5=string, async_operation=bool)
        --------------------------------------------------------------------------------
        - Arg2 (str(control | data)): The type of the capture, either data or control.
        - Arg3 (str(None | /api/v1/sessions/1/ixnetwork/vport/capture)): The capture object of a port.
        - Arg4 (str(control | data)): The type of the capture, either data or control.
        - Arg5 (str): The full path where the resulted merged capture will be saved, the result capture name needs to contain extension also.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        mergeCapture(Arg2=enum, Arg3=string, Arg4=string, async_operation=bool)
        -----------------------------------------------------------------------
        - Arg2 (str(control | data)): The type of the capture, either data or control.
        - Arg3 (str): The full path of the offline capture.
        - Arg4 (str): The full path where the resulted merged capture will be saved, the result capture name needs to contain extension also.
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
        return self._execute("mergeCapture", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        This command starts the capture process for a port or group of ports.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(Arg2=enum, async_operation=bool)
        --------------------------------------
        - Arg2 (str(allTraffic | controlTraffic | dataTraffic)): The type of the capture that should be started.
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

        This command stops captures for the specified capture configuration.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(Arg2=enum, async_operation=bool)
        -------------------------------------
        - Arg2 (str(allTraffic | controlTraffic | dataTraffic)): The capture type.
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
