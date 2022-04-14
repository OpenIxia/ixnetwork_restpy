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


class StpAggregatedStatistics(Base):
    """Represents stats of STP Aggregated Statistics
    The StpAggregatedStatistics class encapsulates a required stpAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "stpAggregatedStatistics"
    _SDM_ATT_MAP = {
        "DiscardingStateCount": "discardingStateCount",
        "ForwardingStateCount": "forwardingStateCount",
        "LearningStateCount": "learningStateCount",
        "ListeningStateCount": "listeningStateCount",
        "MstpBPDUsRx": "mstpBPDUsRx",
        "MstpBPDUsTx": "mstpBPDUsTx",
        "PortName": "portName",
        "PvstBPDUsRx": "pvstBPDUsRx",
        "PvstBPDUsRxConfigTC": "pvstBPDUsRxConfigTC",
        "PvstBPDUsRxConfigTCA": "pvstBPDUsRxConfigTCA",
        "PvstBPDUsRxTCN": "pvstBPDUsRxTCN",
        "PvstBPDUsTx": "pvstBPDUsTx",
        "PvstBPDUsTxConfigTC": "pvstBPDUsTxConfigTC",
        "PvstBPDUsTxConfigTCA": "pvstBPDUsTxConfigTCA",
        "PvstBPDUsTxTCN": "pvstBPDUsTxTCN",
        "RpvstBPDUsRx": "rpvstBPDUsRx",
        "RpvstBPDUsRxTC": "rpvstBPDUsRxTC",
        "RpvstBPDUsTx": "rpvstBPDUsTx",
        "RpvstBPDUsTxTC": "rpvstBPDUsTxTC",
        "RstpBPDUsRx": "rstpBPDUsRx",
        "RstpBPDUsRxTC": "rstpBPDUsRxTC",
        "RstpBPDUsTx": "rstpBPDUsTx",
        "RstpBPDUsTxTC": "rstpBPDUsTxTC",
        "SessionFlapCount": "sessionFlapCount",
        "StpBPDUsRx": "stpBPDUsRx",
        "StpBPDUsRxConfigTC": "stpBPDUsRxConfigTC",
        "StpBPDUsRxConfigTCA": "stpBPDUsRxConfigTCA",
        "StpBPDUsRxTCN": "stpBPDUsRxTCN",
        "StpBPDUsTx": "stpBPDUsTx",
        "StpBPDUsTxConfigTC": "stpBPDUsTxConfigTC",
        "StpBPDUsTxConfigTCA": "stpBPDUsTxConfigTCA",
        "StpBPDUsTxTCN": "stpBPDUsTxTCN",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(StpAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def DiscardingStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Discarding State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscardingStateCount"])

    @DiscardingStateCount.setter
    def DiscardingStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DiscardingStateCount"], value)

    @property
    def ForwardingStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Forwarding State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForwardingStateCount"])

    @ForwardingStateCount.setter
    def ForwardingStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForwardingStateCount"], value)

    @property
    def LearningStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Learning State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearningStateCount"])

    @LearningStateCount.setter
    def LearningStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearningStateCount"], value)

    @property
    def ListeningStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Listening State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ListeningStateCount"])

    @ListeningStateCount.setter
    def ListeningStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ListeningStateCount"], value)

    @property
    def MstpBPDUsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MSTP BPDUs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MstpBPDUsRx"])

    @MstpBPDUsRx.setter
    def MstpBPDUsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MstpBPDUsRx"], value)

    @property
    def MstpBPDUsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MSTP BPDUs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MstpBPDUsTx"])

    @MstpBPDUsTx.setter
    def MstpBPDUsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MstpBPDUsTx"], value)

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
    def PvstBPDUsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsRx"])

    @PvstBPDUsRx.setter
    def PvstBPDUsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsRx"], value)

    @property
    def PvstBPDUsRxConfigTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Rx Config TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsRxConfigTC"])

    @PvstBPDUsRxConfigTC.setter
    def PvstBPDUsRxConfigTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsRxConfigTC"], value)

    @property
    def PvstBPDUsRxConfigTCA(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Rx Config TCA
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsRxConfigTCA"])

    @PvstBPDUsRxConfigTCA.setter
    def PvstBPDUsRxConfigTCA(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsRxConfigTCA"], value)

    @property
    def PvstBPDUsRxTCN(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Rx TCN
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsRxTCN"])

    @PvstBPDUsRxTCN.setter
    def PvstBPDUsRxTCN(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsRxTCN"], value)

    @property
    def PvstBPDUsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsTx"])

    @PvstBPDUsTx.setter
    def PvstBPDUsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsTx"], value)

    @property
    def PvstBPDUsTxConfigTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Tx Config TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsTxConfigTC"])

    @PvstBPDUsTxConfigTC.setter
    def PvstBPDUsTxConfigTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsTxConfigTC"], value)

    @property
    def PvstBPDUsTxConfigTCA(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Tx Config TCA
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsTxConfigTCA"])

    @PvstBPDUsTxConfigTCA.setter
    def PvstBPDUsTxConfigTCA(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsTxConfigTCA"], value)

    @property
    def PvstBPDUsTxTCN(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PVST+ BPDUs Tx TCN
        """
        return self._get_attribute(self._SDM_ATT_MAP["PvstBPDUsTxTCN"])

    @PvstBPDUsTxTCN.setter
    def PvstBPDUsTxTCN(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PvstBPDUsTxTCN"], value)

    @property
    def RpvstBPDUsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RPVST BPDUs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RpvstBPDUsRx"])

    @RpvstBPDUsRx.setter
    def RpvstBPDUsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RpvstBPDUsRx"], value)

    @property
    def RpvstBPDUsRxTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RPVST BPDUs Rx TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["RpvstBPDUsRxTC"])

    @RpvstBPDUsRxTC.setter
    def RpvstBPDUsRxTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RpvstBPDUsRxTC"], value)

    @property
    def RpvstBPDUsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RPVST BPDUs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RpvstBPDUsTx"])

    @RpvstBPDUsTx.setter
    def RpvstBPDUsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RpvstBPDUsTx"], value)

    @property
    def RpvstBPDUsTxTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RPVST BPDUs Tx TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["RpvstBPDUsTxTC"])

    @RpvstBPDUsTxTC.setter
    def RpvstBPDUsTxTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RpvstBPDUsTxTC"], value)

    @property
    def RstpBPDUsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RSTP BPDUs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RstpBPDUsRx"])

    @RstpBPDUsRx.setter
    def RstpBPDUsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RstpBPDUsRx"], value)

    @property
    def RstpBPDUsRxTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RSTP BPDUs Rx TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["RstpBPDUsRxTC"])

    @RstpBPDUsRxTC.setter
    def RstpBPDUsRxTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RstpBPDUsRxTC"], value)

    @property
    def RstpBPDUsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RSTP BPDUs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RstpBPDUsTx"])

    @RstpBPDUsTx.setter
    def RstpBPDUsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RstpBPDUsTx"], value)

    @property
    def RstpBPDUsTxTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RSTP BPDUs Tx TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["RstpBPDUsTxTC"])

    @RstpBPDUsTxTC.setter
    def RstpBPDUsTxTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RstpBPDUsTxTC"], value)

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
    def StpBPDUsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsRx"])

    @StpBPDUsRx.setter
    def StpBPDUsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsRx"], value)

    @property
    def StpBPDUsRxConfigTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Rx Config TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsRxConfigTC"])

    @StpBPDUsRxConfigTC.setter
    def StpBPDUsRxConfigTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsRxConfigTC"], value)

    @property
    def StpBPDUsRxConfigTCA(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Rx Config TCA
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsRxConfigTCA"])

    @StpBPDUsRxConfigTCA.setter
    def StpBPDUsRxConfigTCA(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsRxConfigTCA"], value)

    @property
    def StpBPDUsRxTCN(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Rx TCN
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsRxTCN"])

    @StpBPDUsRxTCN.setter
    def StpBPDUsRxTCN(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsRxTCN"], value)

    @property
    def StpBPDUsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsTx"])

    @StpBPDUsTx.setter
    def StpBPDUsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsTx"], value)

    @property
    def StpBPDUsTxConfigTC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Tx Config TC
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsTxConfigTC"])

    @StpBPDUsTxConfigTC.setter
    def StpBPDUsTxConfigTC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsTxConfigTC"], value)

    @property
    def StpBPDUsTxConfigTCA(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Tx Config TCA
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsTxConfigTCA"])

    @StpBPDUsTxConfigTCA.setter
    def StpBPDUsTxConfigTCA(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsTxConfigTCA"], value)

    @property
    def StpBPDUsTxTCN(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Tx TCN
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsTxTCN"])

    @StpBPDUsTxTCN.setter
    def StpBPDUsTxTCN(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsTxTCN"], value)

    def update(
        self,
        DiscardingStateCount=None,
        ForwardingStateCount=None,
        LearningStateCount=None,
        ListeningStateCount=None,
        MstpBPDUsRx=None,
        MstpBPDUsTx=None,
        PortName=None,
        PvstBPDUsRx=None,
        PvstBPDUsRxConfigTC=None,
        PvstBPDUsRxConfigTCA=None,
        PvstBPDUsRxTCN=None,
        PvstBPDUsTx=None,
        PvstBPDUsTxConfigTC=None,
        PvstBPDUsTxConfigTCA=None,
        PvstBPDUsTxTCN=None,
        RpvstBPDUsRx=None,
        RpvstBPDUsRxTC=None,
        RpvstBPDUsTx=None,
        RpvstBPDUsTxTC=None,
        RstpBPDUsRx=None,
        RstpBPDUsRxTC=None,
        RstpBPDUsTx=None,
        RstpBPDUsTxTC=None,
        SessionFlapCount=None,
        StpBPDUsRx=None,
        StpBPDUsRxConfigTC=None,
        StpBPDUsRxConfigTCA=None,
        StpBPDUsRxTCN=None,
        StpBPDUsTx=None,
        StpBPDUsTxConfigTC=None,
        StpBPDUsTxConfigTCA=None,
        StpBPDUsTxTCN=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> StpAggregatedStatistics
        """Updates stpAggregatedStatistics resource on the server.

        Args
        ----
        - DiscardingStateCount (bool): Discarding State Count
        - ForwardingStateCount (bool): Forwarding State Count
        - LearningStateCount (bool): Learning State Count
        - ListeningStateCount (bool): Listening State Count
        - MstpBPDUsRx (bool): MSTP BPDUs Rx
        - MstpBPDUsTx (bool): MSTP BPDUs Tx
        - PortName (bool): Port Name
        - PvstBPDUsRx (bool): PVST+ BPDUs Rx
        - PvstBPDUsRxConfigTC (bool): PVST+ BPDUs Rx Config TC
        - PvstBPDUsRxConfigTCA (bool): PVST+ BPDUs Rx Config TCA
        - PvstBPDUsRxTCN (bool): PVST+ BPDUs Rx TCN
        - PvstBPDUsTx (bool): PVST+ BPDUs Tx
        - PvstBPDUsTxConfigTC (bool): PVST+ BPDUs Tx Config TC
        - PvstBPDUsTxConfigTCA (bool): PVST+ BPDUs Tx Config TCA
        - PvstBPDUsTxTCN (bool): PVST+ BPDUs Tx TCN
        - RpvstBPDUsRx (bool): RPVST BPDUs Rx
        - RpvstBPDUsRxTC (bool): RPVST BPDUs Rx TC
        - RpvstBPDUsTx (bool): RPVST BPDUs Tx
        - RpvstBPDUsTxTC (bool): RPVST BPDUs Tx TC
        - RstpBPDUsRx (bool): RSTP BPDUs Rx
        - RstpBPDUsRxTC (bool): RSTP BPDUs Rx TC
        - RstpBPDUsTx (bool): RSTP BPDUs Tx
        - RstpBPDUsTxTC (bool): RSTP BPDUs Tx TC
        - SessionFlapCount (bool): Session Flap Count
        - StpBPDUsRx (bool): STP BPDUs Rx
        - StpBPDUsRxConfigTC (bool): STP BPDUs Rx Config TC
        - StpBPDUsRxConfigTCA (bool): STP BPDUs Rx Config TCA
        - StpBPDUsRxTCN (bool): STP BPDUs Rx TCN
        - StpBPDUsTx (bool): STP BPDUs Tx
        - StpBPDUsTxConfigTC (bool): STP BPDUs Tx Config TC
        - StpBPDUsTxConfigTCA (bool): STP BPDUs Tx Config TCA
        - StpBPDUsTxTCN (bool): STP BPDUs Tx TCN

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DiscardingStateCount=None,
        ForwardingStateCount=None,
        LearningStateCount=None,
        ListeningStateCount=None,
        MstpBPDUsRx=None,
        MstpBPDUsTx=None,
        PortName=None,
        PvstBPDUsRx=None,
        PvstBPDUsRxConfigTC=None,
        PvstBPDUsRxConfigTCA=None,
        PvstBPDUsRxTCN=None,
        PvstBPDUsTx=None,
        PvstBPDUsTxConfigTC=None,
        PvstBPDUsTxConfigTCA=None,
        PvstBPDUsTxTCN=None,
        RpvstBPDUsRx=None,
        RpvstBPDUsRxTC=None,
        RpvstBPDUsTx=None,
        RpvstBPDUsTxTC=None,
        RstpBPDUsRx=None,
        RstpBPDUsRxTC=None,
        RstpBPDUsTx=None,
        RstpBPDUsTxTC=None,
        SessionFlapCount=None,
        StpBPDUsRx=None,
        StpBPDUsRxConfigTC=None,
        StpBPDUsRxConfigTCA=None,
        StpBPDUsRxTCN=None,
        StpBPDUsTx=None,
        StpBPDUsTxConfigTC=None,
        StpBPDUsTxConfigTCA=None,
        StpBPDUsTxTCN=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> StpAggregatedStatistics
        """Finds and retrieves stpAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve stpAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all stpAggregatedStatistics resources from the server.

        Args
        ----
        - DiscardingStateCount (bool): Discarding State Count
        - ForwardingStateCount (bool): Forwarding State Count
        - LearningStateCount (bool): Learning State Count
        - ListeningStateCount (bool): Listening State Count
        - MstpBPDUsRx (bool): MSTP BPDUs Rx
        - MstpBPDUsTx (bool): MSTP BPDUs Tx
        - PortName (bool): Port Name
        - PvstBPDUsRx (bool): PVST+ BPDUs Rx
        - PvstBPDUsRxConfigTC (bool): PVST+ BPDUs Rx Config TC
        - PvstBPDUsRxConfigTCA (bool): PVST+ BPDUs Rx Config TCA
        - PvstBPDUsRxTCN (bool): PVST+ BPDUs Rx TCN
        - PvstBPDUsTx (bool): PVST+ BPDUs Tx
        - PvstBPDUsTxConfigTC (bool): PVST+ BPDUs Tx Config TC
        - PvstBPDUsTxConfigTCA (bool): PVST+ BPDUs Tx Config TCA
        - PvstBPDUsTxTCN (bool): PVST+ BPDUs Tx TCN
        - RpvstBPDUsRx (bool): RPVST BPDUs Rx
        - RpvstBPDUsRxTC (bool): RPVST BPDUs Rx TC
        - RpvstBPDUsTx (bool): RPVST BPDUs Tx
        - RpvstBPDUsTxTC (bool): RPVST BPDUs Tx TC
        - RstpBPDUsRx (bool): RSTP BPDUs Rx
        - RstpBPDUsRxTC (bool): RSTP BPDUs Rx TC
        - RstpBPDUsTx (bool): RSTP BPDUs Tx
        - RstpBPDUsTxTC (bool): RSTP BPDUs Tx TC
        - SessionFlapCount (bool): Session Flap Count
        - StpBPDUsRx (bool): STP BPDUs Rx
        - StpBPDUsRxConfigTC (bool): STP BPDUs Rx Config TC
        - StpBPDUsRxConfigTCA (bool): STP BPDUs Rx Config TCA
        - StpBPDUsRxTCN (bool): STP BPDUs Rx TCN
        - StpBPDUsTx (bool): STP BPDUs Tx
        - StpBPDUsTxConfigTC (bool): STP BPDUs Tx Config TC
        - StpBPDUsTxConfigTCA (bool): STP BPDUs Tx Config TCA
        - StpBPDUsTxTCN (bool): STP BPDUs Tx TCN

        Returns
        -------
        - self: This instance with matching stpAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of stpAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the stpAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
