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


class Ospfv3AggregatedStatistics(Base):
    """Represents stats of OSPFv3 Aggregated Statistics
    The Ospfv3AggregatedStatistics class encapsulates a required ospfv3AggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ospfv3AggregatedStatistics"
    _SDM_ATT_MAP = {
        "AttemptStateCount": "attemptStateCount",
        "DbdRx": "dbdRx",
        "DbdTx": "dbdTx",
        "DownStateCount": "downStateCount",
        "ExchangeStateCount": "exchangeStateCount",
        "ExstartStateCount": "exstartStateCount",
        "ExternallsaRx": "externallsaRx",
        "ExternallsaTx": "externallsaTx",
        "FullNbrs": "fullNbrs",
        "FullStateCount": "fullStateCount",
        "GracelsaRx": "gracelsaRx",
        "HellosRx": "hellosRx",
        "HellosTx": "hellosTx",
        "InitStateCount": "initStateCount",
        "InterareaprefixlsaRx": "interareaprefixlsaRx",
        "InterareaprefixlsaTx": "interareaprefixlsaTx",
        "InterarearouterlsaRx": "interarearouterlsaRx",
        "InterarearouterlsaTx": "interarearouterlsaTx",
        "IntraareaprefixlsaRx": "intraareaprefixlsaRx",
        "IntraareaprefixlsaTx": "intraareaprefixlsaTx",
        "LinklsaRx": "linklsaRx",
        "LinklsaTx": "linklsaTx",
        "LinkstateAdvertisementRx": "linkstateAdvertisementRx",
        "LinkstateAdvertisementTx": "linkstateAdvertisementTx",
        "LoadingStateCount": "loadingStateCount",
        "LsAckRx": "lsAckRx",
        "LsAckTx": "lsAckTx",
        "LsRequestRx": "lsRequestRx",
        "LsRequestTx": "lsRequestTx",
        "LsUpdateRx": "lsUpdateRx",
        "LsUpdateTx": "lsUpdateTx",
        "NetworklsaRx": "networklsaRx",
        "NetworklsaTx": "networklsaTx",
        "PortName": "portName",
        "RetransmittedLSA": "retransmittedLSA",
        "RouterlsaRx": "routerlsaRx",
        "RouterlsaTx": "routerlsaTx",
        "SessConfigured": "sessConfigured",
        "SessionFlapCount": "sessionFlapCount",
        "TwowayStateCount": "twowayStateCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Ospfv3AggregatedStatistics, self).__init__(parent, list_op)

    @property
    def AttemptStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Attempt State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["AttemptStateCount"])

    @AttemptStateCount.setter
    def AttemptStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AttemptStateCount"], value)

    @property
    def DbdRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DBD Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbdRx"])

    @DbdRx.setter
    def DbdRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbdRx"], value)

    @property
    def DbdTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DBD Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbdTx"])

    @DbdTx.setter
    def DbdTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbdTx"], value)

    @property
    def DownStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Down State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownStateCount"])

    @DownStateCount.setter
    def DownStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownStateCount"], value)

    @property
    def ExchangeStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Exchange State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExchangeStateCount"])

    @ExchangeStateCount.setter
    def ExchangeStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExchangeStateCount"], value)

    @property
    def ExstartStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ExStart State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExstartStateCount"])

    @ExstartStateCount.setter
    def ExstartStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExstartStateCount"], value)

    @property
    def ExternallsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ExternalLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExternallsaRx"])

    @ExternallsaRx.setter
    def ExternallsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExternallsaRx"], value)

    @property
    def ExternallsaTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ExternalLSA Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExternallsaTx"])

    @ExternallsaTx.setter
    def ExternallsaTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExternallsaTx"], value)

    @property
    def FullNbrs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Full Nbrs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FullNbrs"])

    @FullNbrs.setter
    def FullNbrs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FullNbrs"], value)

    @property
    def FullStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Full State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FullStateCount"])

    @FullStateCount.setter
    def FullStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FullStateCount"], value)

    @property
    def GracelsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: GraceLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GracelsaRx"])

    @GracelsaRx.setter
    def GracelsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GracelsaRx"], value)

    @property
    def HellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hellos Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosRx"])

    @HellosRx.setter
    def HellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosRx"], value)

    @property
    def HellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hellos Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosTx"])

    @HellosTx.setter
    def HellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosTx"], value)

    @property
    def InitStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Init State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitStateCount"])

    @InitStateCount.setter
    def InitStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitStateCount"], value)

    @property
    def InterareaprefixlsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: InterareaPrefixLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterareaprefixlsaRx"])

    @InterareaprefixlsaRx.setter
    def InterareaprefixlsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterareaprefixlsaRx"], value)

    @property
    def InterareaprefixlsaTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: InterareaPrefixLSA Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterareaprefixlsaTx"])

    @InterareaprefixlsaTx.setter
    def InterareaprefixlsaTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterareaprefixlsaTx"], value)

    @property
    def InterarearouterlsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: InterareaRouterLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterarearouterlsaRx"])

    @InterarearouterlsaRx.setter
    def InterarearouterlsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterarearouterlsaRx"], value)

    @property
    def InterarearouterlsaTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: InterareaRouterLSA Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterarearouterlsaTx"])

    @InterarearouterlsaTx.setter
    def InterarearouterlsaTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterarearouterlsaTx"], value)

    @property
    def IntraareaprefixlsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IntraareaPrefixLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["IntraareaprefixlsaRx"])

    @IntraareaprefixlsaRx.setter
    def IntraareaprefixlsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IntraareaprefixlsaRx"], value)

    @property
    def IntraareaprefixlsaTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IntraareaPrefixLSA Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["IntraareaprefixlsaTx"])

    @IntraareaprefixlsaTx.setter
    def IntraareaprefixlsaTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IntraareaprefixlsaTx"], value)

    @property
    def LinklsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LinkLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinklsaRx"])

    @LinklsaRx.setter
    def LinklsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinklsaRx"], value)

    @property
    def LinklsaTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LinkLSA Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinklsaTx"])

    @LinklsaTx.setter
    def LinklsaTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinklsaTx"], value)

    @property
    def LinkstateAdvertisementRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LinkState Advertisement Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkstateAdvertisementRx"])

    @LinkstateAdvertisementRx.setter
    def LinkstateAdvertisementRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkstateAdvertisementRx"], value)

    @property
    def LinkstateAdvertisementTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LinkState Advertisement Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkstateAdvertisementTx"])

    @LinkstateAdvertisementTx.setter
    def LinkstateAdvertisementTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkstateAdvertisementTx"], value)

    @property
    def LoadingStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Loading State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadingStateCount"])

    @LoadingStateCount.setter
    def LoadingStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadingStateCount"], value)

    @property
    def LsAckRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LS Ack Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsAckRx"])

    @LsAckRx.setter
    def LsAckRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsAckRx"], value)

    @property
    def LsAckTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LS Ack Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsAckTx"])

    @LsAckTx.setter
    def LsAckTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsAckTx"], value)

    @property
    def LsRequestRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LS Request Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsRequestRx"])

    @LsRequestRx.setter
    def LsRequestRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsRequestRx"], value)

    @property
    def LsRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LS Request Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsRequestTx"])

    @LsRequestTx.setter
    def LsRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsRequestTx"], value)

    @property
    def LsUpdateRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LS Update Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsUpdateRx"])

    @LsUpdateRx.setter
    def LsUpdateRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsUpdateRx"], value)

    @property
    def LsUpdateTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LS Update Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsUpdateTx"])

    @LsUpdateTx.setter
    def LsUpdateTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsUpdateTx"], value)

    @property
    def NetworklsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NetworkLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworklsaRx"])

    @NetworklsaRx.setter
    def NetworklsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworklsaRx"], value)

    @property
    def NetworklsaTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NetworkLSA Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworklsaTx"])

    @NetworklsaTx.setter
    def NetworklsaTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworklsaTx"], value)

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
    def RetransmittedLSA(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Retransmitted LSA
        """
        return self._get_attribute(self._SDM_ATT_MAP["RetransmittedLSA"])

    @RetransmittedLSA.setter
    def RetransmittedLSA(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RetransmittedLSA"], value)

    @property
    def RouterlsaRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RouterLSA Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterlsaRx"])

    @RouterlsaRx.setter
    def RouterlsaRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterlsaRx"], value)

    @property
    def RouterlsaTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RouterLSA Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterlsaTx"])

    @RouterlsaTx.setter
    def RouterlsaTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterlsaTx"], value)

    @property
    def SessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessConfigured"])

    @SessConfigured.setter
    def SessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessConfigured"], value)

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
    def TwowayStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TwoWay State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["TwowayStateCount"])

    @TwowayStateCount.setter
    def TwowayStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TwowayStateCount"], value)

    def update(
        self,
        AttemptStateCount=None,
        DbdRx=None,
        DbdTx=None,
        DownStateCount=None,
        ExchangeStateCount=None,
        ExstartStateCount=None,
        ExternallsaRx=None,
        ExternallsaTx=None,
        FullNbrs=None,
        FullStateCount=None,
        GracelsaRx=None,
        HellosRx=None,
        HellosTx=None,
        InitStateCount=None,
        InterareaprefixlsaRx=None,
        InterareaprefixlsaTx=None,
        InterarearouterlsaRx=None,
        InterarearouterlsaTx=None,
        IntraareaprefixlsaRx=None,
        IntraareaprefixlsaTx=None,
        LinklsaRx=None,
        LinklsaTx=None,
        LinkstateAdvertisementRx=None,
        LinkstateAdvertisementTx=None,
        LoadingStateCount=None,
        LsAckRx=None,
        LsAckTx=None,
        LsRequestRx=None,
        LsRequestTx=None,
        LsUpdateRx=None,
        LsUpdateTx=None,
        NetworklsaRx=None,
        NetworklsaTx=None,
        PortName=None,
        RetransmittedLSA=None,
        RouterlsaRx=None,
        RouterlsaTx=None,
        SessConfigured=None,
        SessionFlapCount=None,
        TwowayStateCount=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Ospfv3AggregatedStatistics
        """Updates ospfv3AggregatedStatistics resource on the server.

        Args
        ----
        - AttemptStateCount (bool): Attempt State Count
        - DbdRx (bool): DBD Rx
        - DbdTx (bool): DBD Tx
        - DownStateCount (bool): Down State Count
        - ExchangeStateCount (bool): Exchange State Count
        - ExstartStateCount (bool): ExStart State Count
        - ExternallsaRx (bool): ExternalLSA Rx
        - ExternallsaTx (bool): ExternalLSA Tx
        - FullNbrs (bool): Full Nbrs.
        - FullStateCount (bool): Full State Count
        - GracelsaRx (bool): GraceLSA Rx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - InitStateCount (bool): Init State Count
        - InterareaprefixlsaRx (bool): InterareaPrefixLSA Rx
        - InterareaprefixlsaTx (bool): InterareaPrefixLSA Tx
        - InterarearouterlsaRx (bool): InterareaRouterLSA Rx
        - InterarearouterlsaTx (bool): InterareaRouterLSA Tx
        - IntraareaprefixlsaRx (bool): IntraareaPrefixLSA Rx
        - IntraareaprefixlsaTx (bool): IntraareaPrefixLSA Tx
        - LinklsaRx (bool): LinkLSA Rx
        - LinklsaTx (bool): LinkLSA Tx
        - LinkstateAdvertisementRx (bool): LinkState Advertisement Rx
        - LinkstateAdvertisementTx (bool): LinkState Advertisement Tx
        - LoadingStateCount (bool): Loading State Count
        - LsAckRx (bool): LS Ack Rx
        - LsAckTx (bool): LS Ack Tx
        - LsRequestRx (bool): LS Request Rx
        - LsRequestTx (bool): LS Request Tx
        - LsUpdateRx (bool): LS Update Rx
        - LsUpdateTx (bool): LS Update Tx
        - NetworklsaRx (bool): NetworkLSA Rx
        - NetworklsaTx (bool): NetworkLSA Tx
        - PortName (bool): Port Name
        - RetransmittedLSA (bool): Retransmitted LSA
        - RouterlsaRx (bool): RouterLSA Rx
        - RouterlsaTx (bool): RouterLSA Tx
        - SessConfigured (bool): Sess. Configured
        - SessionFlapCount (bool): Session Flap Count
        - TwowayStateCount (bool): TwoWay State Count

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AttemptStateCount=None,
        DbdRx=None,
        DbdTx=None,
        DownStateCount=None,
        ExchangeStateCount=None,
        ExstartStateCount=None,
        ExternallsaRx=None,
        ExternallsaTx=None,
        FullNbrs=None,
        FullStateCount=None,
        GracelsaRx=None,
        HellosRx=None,
        HellosTx=None,
        InitStateCount=None,
        InterareaprefixlsaRx=None,
        InterareaprefixlsaTx=None,
        InterarearouterlsaRx=None,
        InterarearouterlsaTx=None,
        IntraareaprefixlsaRx=None,
        IntraareaprefixlsaTx=None,
        LinklsaRx=None,
        LinklsaTx=None,
        LinkstateAdvertisementRx=None,
        LinkstateAdvertisementTx=None,
        LoadingStateCount=None,
        LsAckRx=None,
        LsAckTx=None,
        LsRequestRx=None,
        LsRequestTx=None,
        LsUpdateRx=None,
        LsUpdateTx=None,
        NetworklsaRx=None,
        NetworklsaTx=None,
        PortName=None,
        RetransmittedLSA=None,
        RouterlsaRx=None,
        RouterlsaTx=None,
        SessConfigured=None,
        SessionFlapCount=None,
        TwowayStateCount=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Ospfv3AggregatedStatistics
        """Finds and retrieves ospfv3AggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfv3AggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfv3AggregatedStatistics resources from the server.

        Args
        ----
        - AttemptStateCount (bool): Attempt State Count
        - DbdRx (bool): DBD Rx
        - DbdTx (bool): DBD Tx
        - DownStateCount (bool): Down State Count
        - ExchangeStateCount (bool): Exchange State Count
        - ExstartStateCount (bool): ExStart State Count
        - ExternallsaRx (bool): ExternalLSA Rx
        - ExternallsaTx (bool): ExternalLSA Tx
        - FullNbrs (bool): Full Nbrs.
        - FullStateCount (bool): Full State Count
        - GracelsaRx (bool): GraceLSA Rx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - InitStateCount (bool): Init State Count
        - InterareaprefixlsaRx (bool): InterareaPrefixLSA Rx
        - InterareaprefixlsaTx (bool): InterareaPrefixLSA Tx
        - InterarearouterlsaRx (bool): InterareaRouterLSA Rx
        - InterarearouterlsaTx (bool): InterareaRouterLSA Tx
        - IntraareaprefixlsaRx (bool): IntraareaPrefixLSA Rx
        - IntraareaprefixlsaTx (bool): IntraareaPrefixLSA Tx
        - LinklsaRx (bool): LinkLSA Rx
        - LinklsaTx (bool): LinkLSA Tx
        - LinkstateAdvertisementRx (bool): LinkState Advertisement Rx
        - LinkstateAdvertisementTx (bool): LinkState Advertisement Tx
        - LoadingStateCount (bool): Loading State Count
        - LsAckRx (bool): LS Ack Rx
        - LsAckTx (bool): LS Ack Tx
        - LsRequestRx (bool): LS Request Rx
        - LsRequestTx (bool): LS Request Tx
        - LsUpdateRx (bool): LS Update Rx
        - LsUpdateTx (bool): LS Update Tx
        - NetworklsaRx (bool): NetworkLSA Rx
        - NetworklsaTx (bool): NetworkLSA Tx
        - PortName (bool): Port Name
        - RetransmittedLSA (bool): Retransmitted LSA
        - RouterlsaRx (bool): RouterLSA Rx
        - RouterlsaTx (bool): RouterLSA Tx
        - SessConfigured (bool): Sess. Configured
        - SessionFlapCount (bool): Session Flap Count
        - TwowayStateCount (bool): TwoWay State Count

        Returns
        -------
        - self: This instance with matching ospfv3AggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfv3AggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfv3AggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
