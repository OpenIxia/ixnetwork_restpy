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


class IgmpQuerierAggregatedStatistics(Base):
    """Represents stats of IGMP Querier Aggregated Statistics
    The IgmpQuerierAggregatedStatistics class encapsulates a required igmpQuerierAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "igmpQuerierAggregatedStatistics"
    _SDM_ATT_MAP = {
        "GeneralQueriesRx": "generalQueriesRx",
        "GrpSpecificQueriesRx": "grpSpecificQueriesRx",
        "LeaveRx": "leaveRx",
        "PortName": "portName",
        "QuerierInvalidPacketsRx": "querierInvalidPacketsRx",
        "QuerierTotalFramesRx": "querierTotalFramesRx",
        "QuerierTotalFramesTx": "querierTotalFramesTx",
        "Querierv1MembershipRptsRx": "querierv1MembershipRptsRx",
        "Querierv2MembershipRptsRx": "querierv2MembershipRptsRx",
        "V1GeneralQueryTx": "v1GeneralQueryTx",
        "V2GeneralQueryTx": "v2GeneralQueryTx",
        "V2GrpspecificQueryTx": "v2GrpspecificQueryTx",
        "V3GeneralQueryTx": "v3GeneralQueryTx",
        "V3GrpSpecificQueryTx": "v3GrpSpecificQueryTx",
        "V3GrpandSrcSpecificQueryTx": "v3GrpandSrcSpecificQueryTx",
        "V3MembershipRptsRx": "v3MembershipRptsRx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IgmpQuerierAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def GeneralQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: General Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GeneralQueriesRx"])

    @GeneralQueriesRx.setter
    def GeneralQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GeneralQueriesRx"], value)

    @property
    def GrpSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Grp. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GrpSpecificQueriesRx"])

    @GrpSpecificQueriesRx.setter
    def GrpSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GrpSpecificQueriesRx"], value)

    @property
    def LeaveRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Leave Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LeaveRx"])

    @LeaveRx.setter
    def LeaveRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LeaveRx"], value)

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
    def QuerierInvalidPacketsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Querier Invalid Packets Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuerierInvalidPacketsRx"])

    @QuerierInvalidPacketsRx.setter
    def QuerierInvalidPacketsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuerierInvalidPacketsRx"], value)

    @property
    def QuerierTotalFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Querier Total Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuerierTotalFramesRx"])

    @QuerierTotalFramesRx.setter
    def QuerierTotalFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuerierTotalFramesRx"], value)

    @property
    def QuerierTotalFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Querier Total Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuerierTotalFramesTx"])

    @QuerierTotalFramesTx.setter
    def QuerierTotalFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuerierTotalFramesTx"], value)

    @property
    def Querierv1MembershipRptsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Querier v1 Membership Rpts. Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Querierv1MembershipRptsRx"])

    @Querierv1MembershipRptsRx.setter
    def Querierv1MembershipRptsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Querierv1MembershipRptsRx"], value)

    @property
    def Querierv2MembershipRptsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Querier v2 Membership Rpts. Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Querierv2MembershipRptsRx"])

    @Querierv2MembershipRptsRx.setter
    def Querierv2MembershipRptsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Querierv2MembershipRptsRx"], value)

    @property
    def V1GeneralQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v1 General Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V1GeneralQueryTx"])

    @V1GeneralQueryTx.setter
    def V1GeneralQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V1GeneralQueryTx"], value)

    @property
    def V2GeneralQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 General Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2GeneralQueryTx"])

    @V2GeneralQueryTx.setter
    def V2GeneralQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2GeneralQueryTx"], value)

    @property
    def V2GrpspecificQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 Grp. specific Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2GrpspecificQueryTx"])

    @V2GrpspecificQueryTx.setter
    def V2GrpspecificQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2GrpspecificQueryTx"], value)

    @property
    def V3GeneralQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v3 General Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V3GeneralQueryTx"])

    @V3GeneralQueryTx.setter
    def V3GeneralQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V3GeneralQueryTx"], value)

    @property
    def V3GrpSpecificQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v3 Grp. Specific Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V3GrpSpecificQueryTx"])

    @V3GrpSpecificQueryTx.setter
    def V3GrpSpecificQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V3GrpSpecificQueryTx"], value)

    @property
    def V3GrpandSrcSpecificQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v3 Grp. and Src. Specific Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V3GrpandSrcSpecificQueryTx"])

    @V3GrpandSrcSpecificQueryTx.setter
    def V3GrpandSrcSpecificQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V3GrpandSrcSpecificQueryTx"], value)

    @property
    def V3MembershipRptsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v3 Membership Rpts. Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V3MembershipRptsRx"])

    @V3MembershipRptsRx.setter
    def V3MembershipRptsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V3MembershipRptsRx"], value)

    def update(
        self,
        GeneralQueriesRx=None,
        GrpSpecificQueriesRx=None,
        LeaveRx=None,
        PortName=None,
        QuerierInvalidPacketsRx=None,
        QuerierTotalFramesRx=None,
        QuerierTotalFramesTx=None,
        Querierv1MembershipRptsRx=None,
        Querierv2MembershipRptsRx=None,
        V1GeneralQueryTx=None,
        V2GeneralQueryTx=None,
        V2GrpspecificQueryTx=None,
        V3GeneralQueryTx=None,
        V3GrpSpecificQueryTx=None,
        V3GrpandSrcSpecificQueryTx=None,
        V3MembershipRptsRx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IgmpQuerierAggregatedStatistics
        """Updates igmpQuerierAggregatedStatistics resource on the server.

        Args
        ----
        - GeneralQueriesRx (bool): General Queries Rx
        - GrpSpecificQueriesRx (bool): Grp. Specific Queries Rx
        - LeaveRx (bool): Leave Rx
        - PortName (bool): Port Name
        - QuerierInvalidPacketsRx (bool): Querier Invalid Packets Rx
        - QuerierTotalFramesRx (bool): Querier Total Frames Rx
        - QuerierTotalFramesTx (bool): Querier Total Frames Tx
        - Querierv1MembershipRptsRx (bool): Querier v1 Membership Rpts. Rx
        - Querierv2MembershipRptsRx (bool): Querier v2 Membership Rpts. Rx
        - V1GeneralQueryTx (bool): v1 General Query Tx
        - V2GeneralQueryTx (bool): v2 General Query Tx
        - V2GrpspecificQueryTx (bool): v2 Grp. specific Query Tx
        - V3GeneralQueryTx (bool): v3 General Query Tx
        - V3GrpSpecificQueryTx (bool): v3 Grp. Specific Query Tx
        - V3GrpandSrcSpecificQueryTx (bool): v3 Grp. and Src. Specific Query Tx
        - V3MembershipRptsRx (bool): v3 Membership Rpts. Rx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        GeneralQueriesRx=None,
        GrpSpecificQueriesRx=None,
        LeaveRx=None,
        PortName=None,
        QuerierInvalidPacketsRx=None,
        QuerierTotalFramesRx=None,
        QuerierTotalFramesTx=None,
        Querierv1MembershipRptsRx=None,
        Querierv2MembershipRptsRx=None,
        V1GeneralQueryTx=None,
        V2GeneralQueryTx=None,
        V2GrpspecificQueryTx=None,
        V3GeneralQueryTx=None,
        V3GrpSpecificQueryTx=None,
        V3GrpandSrcSpecificQueryTx=None,
        V3MembershipRptsRx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IgmpQuerierAggregatedStatistics
        """Finds and retrieves igmpQuerierAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpQuerierAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpQuerierAggregatedStatistics resources from the server.

        Args
        ----
        - GeneralQueriesRx (bool): General Queries Rx
        - GrpSpecificQueriesRx (bool): Grp. Specific Queries Rx
        - LeaveRx (bool): Leave Rx
        - PortName (bool): Port Name
        - QuerierInvalidPacketsRx (bool): Querier Invalid Packets Rx
        - QuerierTotalFramesRx (bool): Querier Total Frames Rx
        - QuerierTotalFramesTx (bool): Querier Total Frames Tx
        - Querierv1MembershipRptsRx (bool): Querier v1 Membership Rpts. Rx
        - Querierv2MembershipRptsRx (bool): Querier v2 Membership Rpts. Rx
        - V1GeneralQueryTx (bool): v1 General Query Tx
        - V2GeneralQueryTx (bool): v2 General Query Tx
        - V2GrpspecificQueryTx (bool): v2 Grp. specific Query Tx
        - V3GeneralQueryTx (bool): v3 General Query Tx
        - V3GrpSpecificQueryTx (bool): v3 Grp. Specific Query Tx
        - V3GrpandSrcSpecificQueryTx (bool): v3 Grp. and Src. Specific Query Tx
        - V3MembershipRptsRx (bool): v3 Membership Rpts. Rx

        Returns
        -------
        - self: This instance with matching igmpQuerierAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpQuerierAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpQuerierAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
