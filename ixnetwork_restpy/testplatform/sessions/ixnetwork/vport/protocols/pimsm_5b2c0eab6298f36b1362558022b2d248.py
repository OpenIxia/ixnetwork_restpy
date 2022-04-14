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


class Pimsm(Base):
    """This object simulates one or more PIM-SM routers in a network of routers.
    The Pimsm class encapsulates a required pimsm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pimsm"
    _SDM_ATT_MAP = {
        "BsmFramePerInterval": "bsmFramePerInterval",
        "CrpFramePerInterval": "crpFramePerInterval",
        "DataMdtFramePerInterval": "dataMdtFramePerInterval",
        "DenyGrePimIpPrefix": "denyGrePimIpPrefix",
        "EnableDiscardJoinPruneProcessing": "enableDiscardJoinPruneProcessing",
        "EnableRateControl": "enableRateControl",
        "Enabled": "enabled",
        "GreFilterType": "greFilterType",
        "HelloMsgsPerInterval": "helloMsgsPerInterval",
        "Interval": "interval",
        "JoinPruneMessagesPerInterval": "joinPruneMessagesPerInterval",
        "OverrideSourceIpForSmInterface": "overrideSourceIpForSmInterface",
        "RegisterMessagesPerInterval": "registerMessagesPerInterval",
        "RegisterStopMessagesPerInterval": "registerStopMessagesPerInterval",
        "RunningState": "runningState",
    }
    _SDM_ENUM_MAP = {
        "greFilterType": ["noDataMdt", "dataMdtIpv4"],
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(Pimsm, self).__init__(parent, list_op)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_904e72c6fa0992bd72a34758e59774b5.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_904e72c6fa0992bd72a34758e59774b5 import (
            Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Router", None) is not None:
                return self._properties.get("Router")
        return Router(self)

    @property
    def BsmFramePerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Allows to specify the rate of the number of BSM messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BsmFramePerInterval"])

    @BsmFramePerInterval.setter
    def BsmFramePerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BsmFramePerInterval"], value)

    @property
    def CrpFramePerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Allows to specify the rate of the number of CRP Adv messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CrpFramePerInterval"])

    @CrpFramePerInterval.setter
    def CrpFramePerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CrpFramePerInterval"], value)

    @property
    def DataMdtFramePerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Data MST message to be sent per interval specified in the interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataMdtFramePerInterval"])

    @DataMdtFramePerInterval.setter
    def DataMdtFramePerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataMdtFramePerInterval"], value)

    @property
    def DenyGrePimIpPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Ixia will reject all GRE-PIM packets whose outer source IP address falls within this specified network prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DenyGrePimIpPrefix"])

    @DenyGrePimIpPrefix.setter
    def DenyGrePimIpPrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DenyGrePimIpPrefix"], value)

    @property
    def EnableDiscardJoinPruneProcessing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, discards the join/prune messages.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableDiscardJoinPruneProcessing"]
        )

    @EnableDiscardJoinPruneProcessing.setter
    def EnableDiscardJoinPruneProcessing(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableDiscardJoinPruneProcessing"], value
        )

    @property
    def EnableRateControl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rate control (flow control) is enabled on this PIM-SM port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRateControl"])

    @EnableRateControl.setter
    def EnableRateControl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRateControl"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the emulated PIM-SM router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def GreFilterType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noDataMdt | dataMdtIpv4): Specifies type of filter for GRE.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GreFilterType"])

    @GreFilterType.setter
    def GreFilterType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GreFilterType"], value)

    @property
    def HelloMsgsPerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The total hello messages received per interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HelloMsgsPerInterval"])

    @HelloMsgsPerInterval.setter
    def HelloMsgsPerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HelloMsgsPerInterval"], value)

    @property
    def Interval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The length of the interval during which a number of messages are sent. The default value is 0, which means that messages will be sent on a best effort basis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Interval"])

    @Interval.setter
    def Interval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Interval"], value)

    @property
    def JoinPruneMessagesPerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The join/prune interval specifies the length of time between transmissions of join/prune messages.The default is 60 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinPruneMessagesPerInterval"])

    @JoinPruneMessagesPerInterval.setter
    def JoinPruneMessagesPerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinPruneMessagesPerInterval"], value)

    @property
    def OverrideSourceIpForSmInterface(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it will override source ip for SM interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideSourceIpForSmInterface"])

    @OverrideSourceIpForSmInterface.setter
    def OverrideSourceIpForSmInterface(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideSourceIpForSmInterface"], value)

    @property
    def RegisterMessagesPerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisterMessagesPerInterval"])

    @RegisterMessagesPerInterval.setter
    def RegisterMessagesPerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisterMessagesPerInterval"], value)

    @property
    def RegisterStopMessagesPerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisterStopMessagesPerInterval"])

    @RegisterStopMessagesPerInterval.setter
    def RegisterStopMessagesPerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisterStopMessagesPerInterval"], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the PIM-SM server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    def update(
        self,
        BsmFramePerInterval=None,
        CrpFramePerInterval=None,
        DataMdtFramePerInterval=None,
        DenyGrePimIpPrefix=None,
        EnableDiscardJoinPruneProcessing=None,
        EnableRateControl=None,
        Enabled=None,
        GreFilterType=None,
        HelloMsgsPerInterval=None,
        Interval=None,
        JoinPruneMessagesPerInterval=None,
        OverrideSourceIpForSmInterface=None,
        RegisterMessagesPerInterval=None,
        RegisterStopMessagesPerInterval=None,
    ):
        # type: (int, int, int, str, bool, bool, bool, str, int, int, int, bool, int, int) -> Pimsm
        """Updates pimsm resource on the server.

        Args
        ----
        - BsmFramePerInterval (number): Allows to specify the rate of the number of BSM messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
        - CrpFramePerInterval (number): Allows to specify the rate of the number of CRP Adv messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
        - DataMdtFramePerInterval (number): The number of Data MST message to be sent per interval specified in the interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        - DenyGrePimIpPrefix (str): Ixia will reject all GRE-PIM packets whose outer source IP address falls within this specified network prefix.
        - EnableDiscardJoinPruneProcessing (bool): If enabled, discards the join/prune messages.
        - EnableRateControl (bool): Rate control (flow control) is enabled on this PIM-SM port.
        - Enabled (bool): Enables the emulated PIM-SM router.
        - GreFilterType (str(noDataMdt | dataMdtIpv4)): Specifies type of filter for GRE.
        - HelloMsgsPerInterval (number): The total hello messages received per interval.
        - Interval (number): The length of the interval during which a number of messages are sent. The default value is 0, which means that messages will be sent on a best effort basis.
        - JoinPruneMessagesPerInterval (number): The join/prune interval specifies the length of time between transmissions of join/prune messages.The default is 60 seconds.
        - OverrideSourceIpForSmInterface (bool): If enabled, it will override source ip for SM interfaces.
        - RegisterMessagesPerInterval (number): The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        - RegisterStopMessagesPerInterval (number): The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BsmFramePerInterval=None,
        CrpFramePerInterval=None,
        DataMdtFramePerInterval=None,
        DenyGrePimIpPrefix=None,
        EnableDiscardJoinPruneProcessing=None,
        EnableRateControl=None,
        Enabled=None,
        GreFilterType=None,
        HelloMsgsPerInterval=None,
        Interval=None,
        JoinPruneMessagesPerInterval=None,
        OverrideSourceIpForSmInterface=None,
        RegisterMessagesPerInterval=None,
        RegisterStopMessagesPerInterval=None,
        RunningState=None,
    ):
        # type: (int, int, int, str, bool, bool, bool, str, int, int, int, bool, int, int, str) -> Pimsm
        """Finds and retrieves pimsm resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pimsm resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pimsm resources from the server.

        Args
        ----
        - BsmFramePerInterval (number): Allows to specify the rate of the number of BSM messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
        - CrpFramePerInterval (number): Allows to specify the rate of the number of CRP Adv messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
        - DataMdtFramePerInterval (number): The number of Data MST message to be sent per interval specified in the interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        - DenyGrePimIpPrefix (str): Ixia will reject all GRE-PIM packets whose outer source IP address falls within this specified network prefix.
        - EnableDiscardJoinPruneProcessing (bool): If enabled, discards the join/prune messages.
        - EnableRateControl (bool): Rate control (flow control) is enabled on this PIM-SM port.
        - Enabled (bool): Enables the emulated PIM-SM router.
        - GreFilterType (str(noDataMdt | dataMdtIpv4)): Specifies type of filter for GRE.
        - HelloMsgsPerInterval (number): The total hello messages received per interval.
        - Interval (number): The length of the interval during which a number of messages are sent. The default value is 0, which means that messages will be sent on a best effort basis.
        - JoinPruneMessagesPerInterval (number): The join/prune interval specifies the length of time between transmissions of join/prune messages.The default is 60 seconds.
        - OverrideSourceIpForSmInterface (bool): If enabled, it will override source ip for SM interfaces.
        - RegisterMessagesPerInterval (number): The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        - RegisterStopMessagesPerInterval (number): The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current running state of the PIM-SM server.

        Returns
        -------
        - self: This instance with matching pimsm resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pimsm data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pimsm resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the PIMSM protocol on a port or group of ports simultaneously.

        start(async_operation=bool)
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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the PIMSM protocol on a port or group of ports simultaneously.

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
