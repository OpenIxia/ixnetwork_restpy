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


class RoceV2PortConfig(Base):
    """RoCEv2 Port Configurations which effects all the RoCEv2 Flowgroups for Tx Port Configuration.
    The RoceV2PortConfig class encapsulates a list of roceV2PortConfig resources that are managed by the system.
    A list of resources can be retrieved from the server using the RoceV2PortConfig.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "roceV2PortConfig"
    _SDM_ATT_MAP = {
        "InterBatchPeriodUnits": "interBatchPeriodUnits",
        "InterBatchPeriodValue": "interBatchPeriodValue",
        "TargetLineRateInPercent": "targetLineRateInPercent",
        "TxCtrlParam": "txCtrlParam",
        "TxPort": "txPort",
    }
    _SDM_ENUM_MAP = {
        "interBatchPeriodUnits": [
            "microseconds",
            "milliseconds",
            "nanoseconds",
            "seconds",
        ],
        "txCtrlParam": ["interBatchPeriod", "targetLineRate"],
    }

    def __init__(self, parent, list_op=False):
        super(RoceV2PortConfig, self).__init__(parent, list_op)

    @property
    def RoceV2DcqcnParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2portconfig.rocev2dcqcnparams.rocev2dcqcnparams.RoceV2DcqcnParams): An instance of the RoceV2DcqcnParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2portconfig.rocev2dcqcnparams.rocev2dcqcnparams import (
            RoceV2DcqcnParams,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RoceV2DcqcnParams", None) is not None:
                return self._properties.get("RoceV2DcqcnParams")
        return RoceV2DcqcnParams(self)._select()

    @property
    def InterBatchPeriodUnits(self):
        # type: () -> str
        """
        Returns
        -------
        - str(microseconds | milliseconds | nanoseconds | seconds): Specifies the unit for Inter Batch Period while transmitting batches.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterBatchPeriodUnits"])

    @InterBatchPeriodUnits.setter
    def InterBatchPeriodUnits(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterBatchPeriodUnits"], value)

    @property
    def InterBatchPeriodValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Inter Batch Period between batch transmit, unit is to be set
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterBatchPeriodValue"])

    @InterBatchPeriodValue.setter
    def InterBatchPeriodValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterBatchPeriodValue"], value)

    @property
    def TargetLineRateInPercent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Target Line Rate In Percent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TargetLineRateInPercent"])

    @TargetLineRateInPercent.setter
    def TargetLineRateInPercent(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TargetLineRateInPercent"], value)

    @property
    def TxCtrlParam(self):
        # type: () -> str
        """
        Returns
        -------
        - str(interBatchPeriod | targetLineRate): The Transmission Control types.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxCtrlParam"])

    @TxCtrlParam.setter
    def TxCtrlParam(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxCtrlParam"], value)

    @property
    def TxPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Transmitting Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxPort"])

    def update(
        self,
        InterBatchPeriodUnits=None,
        InterBatchPeriodValue=None,
        TargetLineRateInPercent=None,
        TxCtrlParam=None,
    ):
        # type: (str, int, int, str) -> RoceV2PortConfig
        """Updates roceV2PortConfig resource on the server.

        Args
        ----
        - InterBatchPeriodUnits (str(microseconds | milliseconds | nanoseconds | seconds)): Specifies the unit for Inter Batch Period while transmitting batches.
        - InterBatchPeriodValue (number): Inter Batch Period between batch transmit, unit is to be set
        - TargetLineRateInPercent (number): Target Line Rate In Percent.
        - TxCtrlParam (str(interBatchPeriod | targetLineRate)): The Transmission Control types.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        InterBatchPeriodUnits=None,
        InterBatchPeriodValue=None,
        TargetLineRateInPercent=None,
        TxCtrlParam=None,
    ):
        # type: (str, int, int, str) -> RoceV2PortConfig
        """Adds a new roceV2PortConfig resource on the json, only valid with batch add utility

        Args
        ----
        - InterBatchPeriodUnits (str(microseconds | milliseconds | nanoseconds | seconds)): Specifies the unit for Inter Batch Period while transmitting batches.
        - InterBatchPeriodValue (number): Inter Batch Period between batch transmit, unit is to be set
        - TargetLineRateInPercent (number): Target Line Rate In Percent.
        - TxCtrlParam (str(interBatchPeriod | targetLineRate)): The Transmission Control types.

        Returns
        -------
        - self: This instance with all currently retrieved roceV2PortConfig resources using find and the newly added roceV2PortConfig resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        InterBatchPeriodUnits=None,
        InterBatchPeriodValue=None,
        TargetLineRateInPercent=None,
        TxCtrlParam=None,
        TxPort=None,
    ):
        # type: (str, int, int, str, str) -> RoceV2PortConfig
        """Finds and retrieves roceV2PortConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve roceV2PortConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all roceV2PortConfig resources from the server.

        Args
        ----
        - InterBatchPeriodUnits (str(microseconds | milliseconds | nanoseconds | seconds)): Specifies the unit for Inter Batch Period while transmitting batches.
        - InterBatchPeriodValue (number): Inter Batch Period between batch transmit, unit is to be set
        - TargetLineRateInPercent (number): Target Line Rate In Percent.
        - TxCtrlParam (str(interBatchPeriod | targetLineRate)): The Transmission Control types.
        - TxPort (str): The Transmitting Port Name

        Returns
        -------
        - self: This instance with matching roceV2PortConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of roceV2PortConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the roceV2PortConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
