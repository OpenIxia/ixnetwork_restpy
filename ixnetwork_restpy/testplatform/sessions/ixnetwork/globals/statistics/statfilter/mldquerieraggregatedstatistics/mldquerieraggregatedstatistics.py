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


class MldQuerierAggregatedStatistics(Base):
    """Represents stats of MLD Querier Aggregated Statistics
    The MldQuerierAggregatedStatistics class encapsulates a required mldQuerierAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "mldQuerierAggregatedStatistics"
    _SDM_ATT_MAP = {
        "Mldv1DoneRx": "mldv1DoneRx",
        "PortName": "portName",
        "QuerierInvalidPacketsRx": "querierInvalidPacketsRx",
        "QuerierTotalFramesRx": "querierTotalFramesRx",
        "QuerierTotalFramesTx": "querierTotalFramesTx",
        "Querierv1MembershipRptsRx": "querierv1MembershipRptsRx",
        "V1GeneralQueriesRx": "v1GeneralQueriesRx",
        "V1GeneralQueryTx": "v1GeneralQueryTx",
        "V1GrpSpecificQueriesRx": "v1GrpSpecificQueriesRx",
        "V1GrpspecificQueryTx": "v1GrpspecificQueryTx",
        "V2GeneralQueriesRx": "v2GeneralQueriesRx",
        "V2GeneralQueryTx": "v2GeneralQueryTx",
        "V2GrpSpecificQueriesRx": "v2GrpSpecificQueriesRx",
        "V2GrpandSrcSpecificQueryTx": "v2GrpandSrcSpecificQueryTx",
        "V2GrpspecificQueryTx": "v2GrpspecificQueryTx",
        "V2MembershipRptsRx": "v2MembershipRptsRx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(MldQuerierAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def Mldv1DoneRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MLDv1 Done Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mldv1DoneRx"])

    @Mldv1DoneRx.setter
    def Mldv1DoneRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mldv1DoneRx"], value)

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
    def V1GeneralQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v1 General Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V1GeneralQueriesRx"])

    @V1GeneralQueriesRx.setter
    def V1GeneralQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V1GeneralQueriesRx"], value)

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
    def V1GrpSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v1 Grp. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V1GrpSpecificQueriesRx"])

    @V1GrpSpecificQueriesRx.setter
    def V1GrpSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V1GrpSpecificQueriesRx"], value)

    @property
    def V1GrpspecificQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v1 Grp. specific Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V1GrpspecificQueryTx"])

    @V1GrpspecificQueryTx.setter
    def V1GrpspecificQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V1GrpspecificQueryTx"], value)

    @property
    def V2GeneralQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 General Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2GeneralQueriesRx"])

    @V2GeneralQueriesRx.setter
    def V2GeneralQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2GeneralQueriesRx"], value)

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
    def V2GrpSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 Grp. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2GrpSpecificQueriesRx"])

    @V2GrpSpecificQueriesRx.setter
    def V2GrpSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2GrpSpecificQueriesRx"], value)

    @property
    def V2GrpandSrcSpecificQueryTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 Grp. and Src. Specific Query Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2GrpandSrcSpecificQueryTx"])

    @V2GrpandSrcSpecificQueryTx.setter
    def V2GrpandSrcSpecificQueryTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2GrpandSrcSpecificQueryTx"], value)

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
    def V2MembershipRptsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 Membership Rpts. Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2MembershipRptsRx"])

    @V2MembershipRptsRx.setter
    def V2MembershipRptsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2MembershipRptsRx"], value)

    def update(
        self,
        Mldv1DoneRx=None,
        PortName=None,
        QuerierInvalidPacketsRx=None,
        QuerierTotalFramesRx=None,
        QuerierTotalFramesTx=None,
        Querierv1MembershipRptsRx=None,
        V1GeneralQueriesRx=None,
        V1GeneralQueryTx=None,
        V1GrpSpecificQueriesRx=None,
        V1GrpspecificQueryTx=None,
        V2GeneralQueriesRx=None,
        V2GeneralQueryTx=None,
        V2GrpSpecificQueriesRx=None,
        V2GrpandSrcSpecificQueryTx=None,
        V2GrpspecificQueryTx=None,
        V2MembershipRptsRx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> MldQuerierAggregatedStatistics
        """Updates mldQuerierAggregatedStatistics resource on the server.

        Args
        ----
        - Mldv1DoneRx (bool): MLDv1 Done Rx
        - PortName (bool): Port Name
        - QuerierInvalidPacketsRx (bool): Querier Invalid Packets Rx
        - QuerierTotalFramesRx (bool): Querier Total Frames Rx
        - QuerierTotalFramesTx (bool): Querier Total Frames Tx
        - Querierv1MembershipRptsRx (bool): Querier v1 Membership Rpts. Rx
        - V1GeneralQueriesRx (bool): v1 General Queries Rx
        - V1GeneralQueryTx (bool): v1 General Query Tx
        - V1GrpSpecificQueriesRx (bool): v1 Grp. Specific Queries Rx
        - V1GrpspecificQueryTx (bool): v1 Grp. specific Query Tx
        - V2GeneralQueriesRx (bool): v2 General Queries Rx
        - V2GeneralQueryTx (bool): v2 General Query Tx
        - V2GrpSpecificQueriesRx (bool): v2 Grp. Specific Queries Rx
        - V2GrpandSrcSpecificQueryTx (bool): v2 Grp. and Src. Specific Query Tx
        - V2GrpspecificQueryTx (bool): v2 Grp. specific Query Tx
        - V2MembershipRptsRx (bool): v2 Membership Rpts. Rx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Mldv1DoneRx=None,
        PortName=None,
        QuerierInvalidPacketsRx=None,
        QuerierTotalFramesRx=None,
        QuerierTotalFramesTx=None,
        Querierv1MembershipRptsRx=None,
        V1GeneralQueriesRx=None,
        V1GeneralQueryTx=None,
        V1GrpSpecificQueriesRx=None,
        V1GrpspecificQueryTx=None,
        V2GeneralQueriesRx=None,
        V2GeneralQueryTx=None,
        V2GrpSpecificQueriesRx=None,
        V2GrpandSrcSpecificQueryTx=None,
        V2GrpspecificQueryTx=None,
        V2MembershipRptsRx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> MldQuerierAggregatedStatistics
        """Finds and retrieves mldQuerierAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mldQuerierAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mldQuerierAggregatedStatistics resources from the server.

        Args
        ----
        - Mldv1DoneRx (bool): MLDv1 Done Rx
        - PortName (bool): Port Name
        - QuerierInvalidPacketsRx (bool): Querier Invalid Packets Rx
        - QuerierTotalFramesRx (bool): Querier Total Frames Rx
        - QuerierTotalFramesTx (bool): Querier Total Frames Tx
        - Querierv1MembershipRptsRx (bool): Querier v1 Membership Rpts. Rx
        - V1GeneralQueriesRx (bool): v1 General Queries Rx
        - V1GeneralQueryTx (bool): v1 General Query Tx
        - V1GrpSpecificQueriesRx (bool): v1 Grp. Specific Queries Rx
        - V1GrpspecificQueryTx (bool): v1 Grp. specific Query Tx
        - V2GeneralQueriesRx (bool): v2 General Queries Rx
        - V2GeneralQueryTx (bool): v2 General Query Tx
        - V2GrpSpecificQueriesRx (bool): v2 Grp. Specific Queries Rx
        - V2GrpandSrcSpecificQueryTx (bool): v2 Grp. and Src. Specific Query Tx
        - V2GrpspecificQueryTx (bool): v2 Grp. specific Query Tx
        - V2MembershipRptsRx (bool): v2 Membership Rpts. Rx

        Returns
        -------
        - self: This instance with matching mldQuerierAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mldQuerierAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mldQuerierAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
