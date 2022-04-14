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


class LacpAggregatedStatistics(Base):
    """Represents stats of LACP Aggregated Statistics
    The LacpAggregatedStatistics class encapsulates a required lacpAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "lacpAggregatedStatistics"
    _SDM_ATT_MAP = {
        "LacpduMalformedRx": "lacpduMalformedRx",
        "LacpduRx": "lacpduRx",
        "LacpduTx": "lacpduTx",
        "LacpduTxRateViolationCount": "lacpduTxRateViolationCount",
        "LagIDSKPTLQ": "lagIDSKPTLQ",
        "LagMemberPortsUP": "lagMemberPortsUP",
        "LinkState": "linkState",
        "MarkerPDURx": "markerPDURx",
        "MarkerPDUTx": "markerPDUTx",
        "MarkerPDUTxRateViolationCount": "markerPDUTxRateViolationCount",
        "MarkerResponsePDURx": "markerResponsePDURx",
        "MarkerResponsePDUTx": "markerResponsePDUTx",
        "MarkerResponseTimeoutCount": "markerResponseTimeoutCount",
        "PortName": "portName",
        "SessionFlapCount": "sessionFlapCount",
        "TotalLAGMemberPorts": "totalLAGMemberPorts",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LacpAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def LacpduMalformedRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LACPDU Malformed Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LacpduMalformedRx"])

    @LacpduMalformedRx.setter
    def LacpduMalformedRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LacpduMalformedRx"], value)

    @property
    def LacpduRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LACPDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LacpduRx"])

    @LacpduRx.setter
    def LacpduRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LacpduRx"], value)

    @property
    def LacpduTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LACPDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LacpduTx"])

    @LacpduTx.setter
    def LacpduTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LacpduTx"], value)

    @property
    def LacpduTxRateViolationCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LACPDU Tx Rate Violation Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["LacpduTxRateViolationCount"])

    @LacpduTxRateViolationCount.setter
    def LacpduTxRateViolationCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LacpduTxRateViolationCount"], value)

    @property
    def LagIDSKPTLQ(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LAG ID [(SKP): (TLQ)]
        """
        return self._get_attribute(self._SDM_ATT_MAP["LagIDSKPTLQ"])

    @LagIDSKPTLQ.setter
    def LagIDSKPTLQ(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LagIDSKPTLQ"], value)

    @property
    def LagMemberPortsUP(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LAG Member Ports UP
        """
        return self._get_attribute(self._SDM_ATT_MAP["LagMemberPortsUP"])

    @LagMemberPortsUP.setter
    def LagMemberPortsUP(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LagMemberPortsUP"], value)

    @property
    def LinkState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Link State
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkState"])

    @LinkState.setter
    def LinkState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkState"], value)

    @property
    def MarkerPDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Marker PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MarkerPDURx"])

    @MarkerPDURx.setter
    def MarkerPDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MarkerPDURx"], value)

    @property
    def MarkerPDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Marker PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MarkerPDUTx"])

    @MarkerPDUTx.setter
    def MarkerPDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MarkerPDUTx"], value)

    @property
    def MarkerPDUTxRateViolationCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Marker PDU Tx Rate Violation Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MarkerPDUTxRateViolationCount"])

    @MarkerPDUTxRateViolationCount.setter
    def MarkerPDUTxRateViolationCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MarkerPDUTxRateViolationCount"], value)

    @property
    def MarkerResponsePDURx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Marker Response PDU Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MarkerResponsePDURx"])

    @MarkerResponsePDURx.setter
    def MarkerResponsePDURx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MarkerResponsePDURx"], value)

    @property
    def MarkerResponsePDUTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Marker Response PDU Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MarkerResponsePDUTx"])

    @MarkerResponsePDUTx.setter
    def MarkerResponsePDUTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MarkerResponsePDUTx"], value)

    @property
    def MarkerResponseTimeoutCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Marker Response Timeout Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MarkerResponseTimeoutCount"])

    @MarkerResponseTimeoutCount.setter
    def MarkerResponseTimeoutCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MarkerResponseTimeoutCount"], value)

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
    def TotalLAGMemberPorts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Total LAG Member Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP["TotalLAGMemberPorts"])

    @TotalLAGMemberPorts.setter
    def TotalLAGMemberPorts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TotalLAGMemberPorts"], value)

    def update(
        self,
        LacpduMalformedRx=None,
        LacpduRx=None,
        LacpduTx=None,
        LacpduTxRateViolationCount=None,
        LagIDSKPTLQ=None,
        LagMemberPortsUP=None,
        LinkState=None,
        MarkerPDURx=None,
        MarkerPDUTx=None,
        MarkerPDUTxRateViolationCount=None,
        MarkerResponsePDURx=None,
        MarkerResponsePDUTx=None,
        MarkerResponseTimeoutCount=None,
        PortName=None,
        SessionFlapCount=None,
        TotalLAGMemberPorts=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> LacpAggregatedStatistics
        """Updates lacpAggregatedStatistics resource on the server.

        Args
        ----
        - LacpduMalformedRx (bool): LACPDU Malformed Rx
        - LacpduRx (bool): LACPDU Rx
        - LacpduTx (bool): LACPDU Tx
        - LacpduTxRateViolationCount (bool): LACPDU Tx Rate Violation Count
        - LagIDSKPTLQ (bool): LAG ID [(SKP): (TLQ)]
        - LagMemberPortsUP (bool): LAG Member Ports UP
        - LinkState (bool): Link State
        - MarkerPDURx (bool): Marker PDU Rx
        - MarkerPDUTx (bool): Marker PDU Tx
        - MarkerPDUTxRateViolationCount (bool): Marker PDU Tx Rate Violation Count
        - MarkerResponsePDURx (bool): Marker Response PDU Rx
        - MarkerResponsePDUTx (bool): Marker Response PDU Tx
        - MarkerResponseTimeoutCount (bool): Marker Response Timeout Count
        - PortName (bool): Port Name
        - SessionFlapCount (bool): Session Flap Count
        - TotalLAGMemberPorts (bool): Total LAG Member Ports

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        LacpduMalformedRx=None,
        LacpduRx=None,
        LacpduTx=None,
        LacpduTxRateViolationCount=None,
        LagIDSKPTLQ=None,
        LagMemberPortsUP=None,
        LinkState=None,
        MarkerPDURx=None,
        MarkerPDUTx=None,
        MarkerPDUTxRateViolationCount=None,
        MarkerResponsePDURx=None,
        MarkerResponsePDUTx=None,
        MarkerResponseTimeoutCount=None,
        PortName=None,
        SessionFlapCount=None,
        TotalLAGMemberPorts=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> LacpAggregatedStatistics
        """Finds and retrieves lacpAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lacpAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lacpAggregatedStatistics resources from the server.

        Args
        ----
        - LacpduMalformedRx (bool): LACPDU Malformed Rx
        - LacpduRx (bool): LACPDU Rx
        - LacpduTx (bool): LACPDU Tx
        - LacpduTxRateViolationCount (bool): LACPDU Tx Rate Violation Count
        - LagIDSKPTLQ (bool): LAG ID [(SKP): (TLQ)]
        - LagMemberPortsUP (bool): LAG Member Ports UP
        - LinkState (bool): Link State
        - MarkerPDURx (bool): Marker PDU Rx
        - MarkerPDUTx (bool): Marker PDU Tx
        - MarkerPDUTxRateViolationCount (bool): Marker PDU Tx Rate Violation Count
        - MarkerResponsePDURx (bool): Marker Response PDU Rx
        - MarkerResponsePDUTx (bool): Marker Response PDU Tx
        - MarkerResponseTimeoutCount (bool): Marker Response Timeout Count
        - PortName (bool): Port Name
        - SessionFlapCount (bool): Session Flap Count
        - TotalLAGMemberPorts (bool): Total LAG Member Ports

        Returns
        -------
        - self: This instance with matching lacpAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lacpAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lacpAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
