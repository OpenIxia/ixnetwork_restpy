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


class Controller131TriggerAttributes(Base):
    """This object allows to configure the controller131TriggerAttributes API.
    The Controller131TriggerAttributes class encapsulates a required controller131TriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "controller131TriggerAttributes"
    _SDM_ATT_MAP = {
        "EnableSendTriggerMeterConfigStatsLearnedInformation": "enableSendTriggerMeterConfigStatsLearnedInformation",
        "EnableSendTriggerMeterFeatureStatsLearnedInformation": "enableSendTriggerMeterFeatureStatsLearnedInformation",
        "EnableSendTriggerMeterStatLearnedInformation": "enableSendTriggerMeterStatLearnedInformation",
        "FlowStatOutGroup": "flowStatOutGroup",
        "FlowStatOutGroupInputMode": "flowStatOutGroupInputMode",
        "FlowStatOutPort": "flowStatOutPort",
        "FlowStatOutPortInputMode": "flowStatOutPortInputMode",
        "FlowStatTableId": "flowStatTableId",
        "FlowStatTableIdInputMode": "flowStatTableIdInputMode",
        "IsMeterConfigStatLearnedInformationRefreshed": "isMeterConfigStatLearnedInformationRefreshed",
        "IsMeterFeatureStatLearnedInformationRefreshed": "isMeterFeatureStatLearnedInformationRefreshed",
        "IsMeterStatLearnedInformationRefreshed": "isMeterStatLearnedInformationRefreshed",
        "MeterConfigStatMeterId": "meterConfigStatMeterId",
        "MeterConfigStatMeterNumber": "meterConfigStatMeterNumber",
        "MeterConfigStatResponseTimeOut": "meterConfigStatResponseTimeOut",
        "MeterFeatureStatResponseTimeOut": "meterFeatureStatResponseTimeOut",
        "MeterStatMeterId": "meterStatMeterId",
        "MeterStatMeterNumber": "meterStatMeterNumber",
        "MeterStatResponseTimeOut": "meterStatResponseTimeOut",
        "PortStatPortNumber": "portStatPortNumber",
        "PortStatPortNumberInputMode": "portStatPortNumberInputMode",
        "QueueConfigPortNumber": "queueConfigPortNumber",
        "QueueConfigPortNumberInputMode": "queueConfigPortNumberInputMode",
        "QueueStatPortNumber": "queueStatPortNumber",
        "QueueStatPortNumberInputMode": "queueStatPortNumberInputMode",
        "VendorMessageExperimenterType": "vendorMessageExperimenterType",
        "VendorStatExperimenterType": "vendorStatExperimenterType",
    }
    _SDM_ENUM_MAP = {
        "flowStatOutGroupInputMode": ["allGroups", "anyGroup", "outGroupCustom"],
        "flowStatOutPortInputMode": [
            "ofppInPort",
            "ofppNormal",
            "ofppFlood",
            "ofppAll",
            "ofppController",
            "ofppLocal",
            "ofppAny",
            "outPortCustom",
        ],
        "flowStatTableIdInputMode": ["allTables", "emergency", "custom"],
        "meterConfigStatMeterId": [
            "ofpmController",
            "ofpmSlowPath",
            "ofpmAll",
            "manual",
        ],
        "meterStatMeterId": ["ofpmController", "ofpmSlowPath", "ofpmAll", "manual"],
        "portStatPortNumberInputMode": ["ofppAny", "portNumberCustom"],
        "queueConfigPortNumberInputMode": ["ofppAny", "portNumberCustom"],
        "queueStatPortNumberInputMode": ["ofppAll", "ofppAny", "portNumberCustom"],
    }

    def __init__(self, parent, list_op=False):
        super(Controller131TriggerAttributes, self).__init__(parent, list_op)

    @property
    def EnableSendTriggerMeterConfigStatsLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerMeterConfigStatsLearnedInformation"]
        )

    @EnableSendTriggerMeterConfigStatsLearnedInformation.setter
    def EnableSendTriggerMeterConfigStatsLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerMeterConfigStatsLearnedInformation"],
            value,
        )

    @property
    def EnableSendTriggerMeterFeatureStatsLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerMeterFeatureStatsLearnedInformation"]
        )

    @EnableSendTriggerMeterFeatureStatsLearnedInformation.setter
    def EnableSendTriggerMeterFeatureStatsLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerMeterFeatureStatsLearnedInformation"],
            value,
        )

    @property
    def EnableSendTriggerMeterStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerMeterStatLearnedInformation"]
        )

    @EnableSendTriggerMeterStatLearnedInformation.setter
    def EnableSendTriggerMeterStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerMeterStatLearnedInformation"], value
        )

    @property
    def FlowStatOutGroup(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The out group used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutGroup"])

    @FlowStatOutGroup.setter
    def FlowStatOutGroup(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutGroup"], value)

    @property
    def FlowStatOutGroupInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allGroups | anyGroup | outGroupCustom): The input mode of the out group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutGroupInputMode"])

    @FlowStatOutGroupInputMode.setter
    def FlowStatOutGroupInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutGroupInputMode"], value)

    @property
    def FlowStatOutPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Output port number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutPort"])

    @FlowStatOutPort.setter
    def FlowStatOutPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutPort"], value)

    @property
    def FlowStatOutPortInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom): The output port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutPortInputMode"])

    @FlowStatOutPortInputMode.setter
    def FlowStatOutPortInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutPortInputMode"], value)

    @property
    def FlowStatTableId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identifier of the table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTableId"])

    @FlowStatTableId.setter
    def FlowStatTableId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTableId"], value)

    @property
    def FlowStatTableIdInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allTables | emergency | custom): The identifier of the table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTableIdInputMode"])

    @FlowStatTableIdInputMode.setter
    def FlowStatTableIdInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTableIdInputMode"], value)

    @property
    def IsMeterConfigStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsMeterConfigStatLearnedInformationRefreshed"]
        )

    @property
    def IsMeterFeatureStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsMeterFeatureStatLearnedInformationRefreshed"]
        )

    @property
    def IsMeterStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsMeterStatLearnedInformationRefreshed"]
        )

    @property
    def MeterConfigStatMeterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofpmController | ofpmSlowPath | ofpmAll | manual): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigStatMeterId"])

    @MeterConfigStatMeterId.setter
    def MeterConfigStatMeterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigStatMeterId"], value)

    @property
    def MeterConfigStatMeterNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigStatMeterNumber"])

    @MeterConfigStatMeterNumber.setter
    def MeterConfigStatMeterNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigStatMeterNumber"], value)

    @property
    def MeterConfigStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigStatResponseTimeOut"])

    @MeterConfigStatResponseTimeOut.setter
    def MeterConfigStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigStatResponseTimeOut"], value)

    @property
    def MeterFeatureStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterFeatureStatResponseTimeOut"])

    @MeterFeatureStatResponseTimeOut.setter
    def MeterFeatureStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterFeatureStatResponseTimeOut"], value)

    @property
    def MeterStatMeterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofpmController | ofpmSlowPath | ofpmAll | manual): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatMeterId"])

    @MeterStatMeterId.setter
    def MeterStatMeterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatMeterId"], value)

    @property
    def MeterStatMeterNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatMeterNumber"])

    @MeterStatMeterNumber.setter
    def MeterStatMeterNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatMeterNumber"], value)

    @property
    def MeterStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatResponseTimeOut"])

    @MeterStatResponseTimeOut.setter
    def MeterStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatResponseTimeOut"], value)

    @property
    def PortStatPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The port number for port stat learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatPortNumber"])

    @PortStatPortNumber.setter
    def PortStatPortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatPortNumber"], value)

    @property
    def PortStatPortNumberInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppAny | portNumberCustom): The input mode of port number for port stat learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatPortNumberInputMode"])

    @PortStatPortNumberInputMode.setter
    def PortStatPortNumberInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatPortNumberInputMode"], value)

    @property
    def QueueConfigPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The port number for queue config learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueConfigPortNumber"])

    @QueueConfigPortNumber.setter
    def QueueConfigPortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueConfigPortNumber"], value)

    @property
    def QueueConfigPortNumberInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppAny | portNumberCustom): The input mode of port number for queue config learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueConfigPortNumberInputMode"])

    @QueueConfigPortNumberInputMode.setter
    def QueueConfigPortNumberInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueConfigPortNumberInputMode"], value)

    @property
    def QueueStatPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The port number for queue statistics learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatPortNumber"])

    @QueueStatPortNumber.setter
    def QueueStatPortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatPortNumber"], value)

    @property
    def QueueStatPortNumberInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppAll | ofppAny | portNumberCustom): The input mode of port number for queue statistics learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatPortNumberInputMode"])

    @QueueStatPortNumberInputMode.setter
    def QueueStatPortNumberInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatPortNumberInputMode"], value)

    @property
    def VendorMessageExperimenterType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Experimenter type for Vendor Message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMessageExperimenterType"])

    @VendorMessageExperimenterType.setter
    def VendorMessageExperimenterType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMessageExperimenterType"], value)

    @property
    def VendorStatExperimenterType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Experimenter type for Vendor stat.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatExperimenterType"])

    @VendorStatExperimenterType.setter
    def VendorStatExperimenterType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatExperimenterType"], value)

    def update(
        self,
        EnableSendTriggerMeterConfigStatsLearnedInformation=None,
        EnableSendTriggerMeterFeatureStatsLearnedInformation=None,
        EnableSendTriggerMeterStatLearnedInformation=None,
        FlowStatOutGroup=None,
        FlowStatOutGroupInputMode=None,
        FlowStatOutPort=None,
        FlowStatOutPortInputMode=None,
        FlowStatTableId=None,
        FlowStatTableIdInputMode=None,
        MeterConfigStatMeterId=None,
        MeterConfigStatMeterNumber=None,
        MeterConfigStatResponseTimeOut=None,
        MeterFeatureStatResponseTimeOut=None,
        MeterStatMeterId=None,
        MeterStatMeterNumber=None,
        MeterStatResponseTimeOut=None,
        PortStatPortNumber=None,
        PortStatPortNumberInputMode=None,
        QueueConfigPortNumber=None,
        QueueConfigPortNumberInputMode=None,
        QueueStatPortNumber=None,
        QueueStatPortNumberInputMode=None,
        VendorMessageExperimenterType=None,
        VendorStatExperimenterType=None,
    ):
        # type: (bool, bool, bool, int, str, int, str, int, str, str, int, int, int, str, int, int, int, str, int, str, int, str, int, int) -> Controller131TriggerAttributes
        """Updates controller131TriggerAttributes resource on the server.

        Args
        ----
        - EnableSendTriggerMeterConfigStatsLearnedInformation (bool): NOT DEFINED
        - EnableSendTriggerMeterFeatureStatsLearnedInformation (bool): NOT DEFINED
        - EnableSendTriggerMeterStatLearnedInformation (bool): NOT DEFINED
        - FlowStatOutGroup (number): The out group used.
        - FlowStatOutGroupInputMode (str(allGroups | anyGroup | outGroupCustom)): The input mode of the out group.
        - FlowStatOutPort (number): Specifies the Output port number.
        - FlowStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom)): The output port used.
        - FlowStatTableId (number): The identifier of the table.
        - FlowStatTableIdInputMode (str(allTables | emergency | custom)): The identifier of the table.
        - MeterConfigStatMeterId (str(ofpmController | ofpmSlowPath | ofpmAll | manual)): NOT DEFINED
        - MeterConfigStatMeterNumber (number): NOT DEFINED
        - MeterConfigStatResponseTimeOut (number): NOT DEFINED
        - MeterFeatureStatResponseTimeOut (number): NOT DEFINED
        - MeterStatMeterId (str(ofpmController | ofpmSlowPath | ofpmAll | manual)): NOT DEFINED
        - MeterStatMeterNumber (number): NOT DEFINED
        - MeterStatResponseTimeOut (number): NOT DEFINED
        - PortStatPortNumber (number): The port number for port stat learned information.
        - PortStatPortNumberInputMode (str(ofppAny | portNumberCustom)): The input mode of port number for port stat learned information.
        - QueueConfigPortNumber (number): The port number for queue config learned information.
        - QueueConfigPortNumberInputMode (str(ofppAny | portNumberCustom)): The input mode of port number for queue config learned information.
        - QueueStatPortNumber (number): The port number for queue statistics learned information.
        - QueueStatPortNumberInputMode (str(ofppAll | ofppAny | portNumberCustom)): The input mode of port number for queue statistics learned information.
        - VendorMessageExperimenterType (number): Experimenter type for Vendor Message.
        - VendorStatExperimenterType (number): Experimenter type for Vendor stat.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableSendTriggerMeterConfigStatsLearnedInformation=None,
        EnableSendTriggerMeterFeatureStatsLearnedInformation=None,
        EnableSendTriggerMeterStatLearnedInformation=None,
        FlowStatOutGroup=None,
        FlowStatOutGroupInputMode=None,
        FlowStatOutPort=None,
        FlowStatOutPortInputMode=None,
        FlowStatTableId=None,
        FlowStatTableIdInputMode=None,
        IsMeterConfigStatLearnedInformationRefreshed=None,
        IsMeterFeatureStatLearnedInformationRefreshed=None,
        IsMeterStatLearnedInformationRefreshed=None,
        MeterConfigStatMeterId=None,
        MeterConfigStatMeterNumber=None,
        MeterConfigStatResponseTimeOut=None,
        MeterFeatureStatResponseTimeOut=None,
        MeterStatMeterId=None,
        MeterStatMeterNumber=None,
        MeterStatResponseTimeOut=None,
        PortStatPortNumber=None,
        PortStatPortNumberInputMode=None,
        QueueConfigPortNumber=None,
        QueueConfigPortNumberInputMode=None,
        QueueStatPortNumber=None,
        QueueStatPortNumberInputMode=None,
        VendorMessageExperimenterType=None,
        VendorStatExperimenterType=None,
    ):
        # type: (bool, bool, bool, int, str, int, str, int, str, bool, bool, bool, str, int, int, int, str, int, int, int, str, int, str, int, str, int, int) -> Controller131TriggerAttributes
        """Finds and retrieves controller131TriggerAttributes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve controller131TriggerAttributes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all controller131TriggerAttributes resources from the server.

        Args
        ----
        - EnableSendTriggerMeterConfigStatsLearnedInformation (bool): NOT DEFINED
        - EnableSendTriggerMeterFeatureStatsLearnedInformation (bool): NOT DEFINED
        - EnableSendTriggerMeterStatLearnedInformation (bool): NOT DEFINED
        - FlowStatOutGroup (number): The out group used.
        - FlowStatOutGroupInputMode (str(allGroups | anyGroup | outGroupCustom)): The input mode of the out group.
        - FlowStatOutPort (number): Specifies the Output port number.
        - FlowStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom)): The output port used.
        - FlowStatTableId (number): The identifier of the table.
        - FlowStatTableIdInputMode (str(allTables | emergency | custom)): The identifier of the table.
        - IsMeterConfigStatLearnedInformationRefreshed (bool): NOT DEFINED
        - IsMeterFeatureStatLearnedInformationRefreshed (bool): NOT DEFINED
        - IsMeterStatLearnedInformationRefreshed (bool): NOT DEFINED
        - MeterConfigStatMeterId (str(ofpmController | ofpmSlowPath | ofpmAll | manual)): NOT DEFINED
        - MeterConfigStatMeterNumber (number): NOT DEFINED
        - MeterConfigStatResponseTimeOut (number): NOT DEFINED
        - MeterFeatureStatResponseTimeOut (number): NOT DEFINED
        - MeterStatMeterId (str(ofpmController | ofpmSlowPath | ofpmAll | manual)): NOT DEFINED
        - MeterStatMeterNumber (number): NOT DEFINED
        - MeterStatResponseTimeOut (number): NOT DEFINED
        - PortStatPortNumber (number): The port number for port stat learned information.
        - PortStatPortNumberInputMode (str(ofppAny | portNumberCustom)): The input mode of port number for port stat learned information.
        - QueueConfigPortNumber (number): The port number for queue config learned information.
        - QueueConfigPortNumberInputMode (str(ofppAny | portNumberCustom)): The input mode of port number for queue config learned information.
        - QueueStatPortNumber (number): The port number for queue statistics learned information.
        - QueueStatPortNumberInputMode (str(ofppAll | ofppAny | portNumberCustom)): The input mode of port number for queue statistics learned information.
        - VendorMessageExperimenterType (number): Experimenter type for Vendor Message.
        - VendorStatExperimenterType (number): Experimenter type for Vendor stat.

        Returns
        -------
        - self: This instance with matching controller131TriggerAttributes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of controller131TriggerAttributes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the controller131TriggerAttributes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
