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


class BfdAggregatedStatistics(Base):
    """Represents stats of BFD Aggregated Statistics
    The BfdAggregatedStatistics class encapsulates a required bfdAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bfdAggregatedStatistics"
    _SDM_ATT_MAP = {
        "AutoCreatedUPSessions": "autoCreatedUPSessions",
        "BfdMPLSPDUsRx": "bfdMPLSPDUsRx",
        "BfdMPLSPDUsTx": "bfdMPLSPDUsTx",
        "ConfiguredUPSessions": "configuredUPSessions",
        "ControlRx": "controlRx",
        "ControlTx": "controlTx",
        "EchoDUTLoopBack": "echoDUTLoopBack",
        "EchoDUTReceived": "echoDUTReceived",
        "EchoSelfRx": "echoSelfRx",
        "EchoSelfTx": "echoSelfTx",
        "PortName": "portName",
        "RoutersConfigured": "routersConfigured",
        "RoutersRunning": "routersRunning",
        "SessionFlapCount": "sessionFlapCount",
        "SessionsAutoCreated": "sessionsAutoCreated",
        "SessionsConfigured": "sessionsConfigured",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BfdAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def AutoCreatedUPSessions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Auto-Created UP-Sessions
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoCreatedUPSessions"])

    @AutoCreatedUPSessions.setter
    def AutoCreatedUPSessions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoCreatedUPSessions"], value)

    @property
    def BfdMPLSPDUsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BFD MPLS PDUs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BfdMPLSPDUsRx"])

    @BfdMPLSPDUsRx.setter
    def BfdMPLSPDUsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BfdMPLSPDUsRx"], value)

    @property
    def BfdMPLSPDUsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BFD MPLS PDUs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BfdMPLSPDUsTx"])

    @BfdMPLSPDUsTx.setter
    def BfdMPLSPDUsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BfdMPLSPDUsTx"], value)

    @property
    def ConfiguredUPSessions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Configured UP-Sessions
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfiguredUPSessions"])

    @ConfiguredUPSessions.setter
    def ConfiguredUPSessions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConfiguredUPSessions"], value)

    @property
    def ControlRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Control Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlRx"])

    @ControlRx.setter
    def ControlRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlRx"], value)

    @property
    def ControlTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Control Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlTx"])

    @ControlTx.setter
    def ControlTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlTx"], value)

    @property
    def EchoDUTLoopBack(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo DUT Loop Back
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoDUTLoopBack"])

    @EchoDUTLoopBack.setter
    def EchoDUTLoopBack(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoDUTLoopBack"], value)

    @property
    def EchoDUTReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo DUT Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoDUTReceived"])

    @EchoDUTReceived.setter
    def EchoDUTReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoDUTReceived"], value)

    @property
    def EchoSelfRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo Self Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoSelfRx"])

    @EchoSelfRx.setter
    def EchoSelfRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoSelfRx"], value)

    @property
    def EchoSelfTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo Self Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoSelfTx"])

    @EchoSelfTx.setter
    def EchoSelfTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoSelfTx"], value)

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
    def RoutersConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routers Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutersConfigured"])

    @RoutersConfigured.setter
    def RoutersConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutersConfigured"], value)

    @property
    def RoutersRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routers Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutersRunning"])

    @RoutersRunning.setter
    def RoutersRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutersRunning"], value)

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
    def SessionsAutoCreated(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sessions Auto-Created
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionsAutoCreated"])

    @SessionsAutoCreated.setter
    def SessionsAutoCreated(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionsAutoCreated"], value)

    @property
    def SessionsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sessions Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionsConfigured"])

    @SessionsConfigured.setter
    def SessionsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionsConfigured"], value)

    def update(
        self,
        AutoCreatedUPSessions=None,
        BfdMPLSPDUsRx=None,
        BfdMPLSPDUsTx=None,
        ConfiguredUPSessions=None,
        ControlRx=None,
        ControlTx=None,
        EchoDUTLoopBack=None,
        EchoDUTReceived=None,
        EchoSelfRx=None,
        EchoSelfTx=None,
        PortName=None,
        RoutersConfigured=None,
        RoutersRunning=None,
        SessionFlapCount=None,
        SessionsAutoCreated=None,
        SessionsConfigured=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> BfdAggregatedStatistics
        """Updates bfdAggregatedStatistics resource on the server.

        Args
        ----
        - AutoCreatedUPSessions (bool): Auto-Created UP-Sessions
        - BfdMPLSPDUsRx (bool): BFD MPLS PDUs Rx
        - BfdMPLSPDUsTx (bool): BFD MPLS PDUs Tx
        - ConfiguredUPSessions (bool): Configured UP-Sessions
        - ControlRx (bool): Control Rx
        - ControlTx (bool): Control Tx
        - EchoDUTLoopBack (bool): Echo DUT Loop Back
        - EchoDUTReceived (bool): Echo DUT Received
        - EchoSelfRx (bool): Echo Self Rx
        - EchoSelfTx (bool): Echo Self Tx
        - PortName (bool): Port Name
        - RoutersConfigured (bool): Routers Configured
        - RoutersRunning (bool): Routers Running
        - SessionFlapCount (bool): Session Flap Count
        - SessionsAutoCreated (bool): Sessions Auto-Created
        - SessionsConfigured (bool): Sessions Configured

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoCreatedUPSessions=None,
        BfdMPLSPDUsRx=None,
        BfdMPLSPDUsTx=None,
        ConfiguredUPSessions=None,
        ControlRx=None,
        ControlTx=None,
        EchoDUTLoopBack=None,
        EchoDUTReceived=None,
        EchoSelfRx=None,
        EchoSelfTx=None,
        PortName=None,
        RoutersConfigured=None,
        RoutersRunning=None,
        SessionFlapCount=None,
        SessionsAutoCreated=None,
        SessionsConfigured=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> BfdAggregatedStatistics
        """Finds and retrieves bfdAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bfdAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bfdAggregatedStatistics resources from the server.

        Args
        ----
        - AutoCreatedUPSessions (bool): Auto-Created UP-Sessions
        - BfdMPLSPDUsRx (bool): BFD MPLS PDUs Rx
        - BfdMPLSPDUsTx (bool): BFD MPLS PDUs Tx
        - ConfiguredUPSessions (bool): Configured UP-Sessions
        - ControlRx (bool): Control Rx
        - ControlTx (bool): Control Tx
        - EchoDUTLoopBack (bool): Echo DUT Loop Back
        - EchoDUTReceived (bool): Echo DUT Received
        - EchoSelfRx (bool): Echo Self Rx
        - EchoSelfTx (bool): Echo Self Tx
        - PortName (bool): Port Name
        - RoutersConfigured (bool): Routers Configured
        - RoutersRunning (bool): Routers Running
        - SessionFlapCount (bool): Session Flap Count
        - SessionsAutoCreated (bool): Sessions Auto-Created
        - SessionsConfigured (bool): Sessions Configured

        Returns
        -------
        - self: This instance with matching bfdAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bfdAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bfdAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
