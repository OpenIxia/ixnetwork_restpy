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


class PimsmAggregatedStatistics(Base):
    """Represents stats of PIMSM Aggregated Statistics
    The PimsmAggregatedStatistics class encapsulates a required pimsmAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pimsmAggregatedStatistics"
    _SDM_ATT_MAP = {
        "BootstrapMsgRx": "bootstrapMsgRx",
        "BootstrapMsgTx": "bootstrapMsgTx",
        "DatamdtTLVRx": "datamdtTLVRx",
        "DatamdtTLVTx": "datamdtTLVTx",
        "HellosRx": "hellosRx",
        "HellosTx": "hellosTx",
        "JoinSGRPTRx": "joinSGRPTRx",
        "JoinSGRPTTx": "joinSGRPTTx",
        "JoinSGRx": "joinSGRx",
        "JoinSGTx": "joinSGTx",
        "JoinXGRx": "joinXGRx",
        "JoinXGTx": "joinXGTx",
        "JoinXXRPRx": "joinXXRPRx",
        "JoinXXRPTx": "joinXXRPTx",
        "NbrsLearnt": "nbrsLearnt",
        "NormalCRPAdvMsgRx": "normalCRPAdvMsgRx",
        "NormalCRPAdvMsgTx": "normalCRPAdvMsgTx",
        "PortName": "portName",
        "PruneSGRPTRx": "pruneSGRPTRx",
        "PruneSGRPTTx": "pruneSGRPTTx",
        "PruneSGRx": "pruneSGRx",
        "PruneSGTx": "pruneSGTx",
        "PruneXGRx": "pruneXGRx",
        "PruneXGTx": "pruneXGTx",
        "PruneXXRPRx": "pruneXXRPRx",
        "PruneXXRPTx": "pruneXXRPTx",
        "RegisterRx": "registerRx",
        "RegisterTx": "registerTx",
        "RegisternullRx": "registernullRx",
        "RegisternullTx": "registernullTx",
        "RegisterstopRx": "registerstopRx",
        "RegisterstopTx": "registerstopTx",
        "RtrsConfigured": "rtrsConfigured",
        "RtrsRunning": "rtrsRunning",
        "SessionFlapCount": "sessionFlapCount",
        "ShutdownCRPAdvMsgRx": "shutdownCRPAdvMsgRx",
        "ShutdownCRPAdvMsgTx": "shutdownCRPAdvMsgTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PimsmAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def BootstrapMsgRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bootstrap Msg Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BootstrapMsgRx"])

    @BootstrapMsgRx.setter
    def BootstrapMsgRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BootstrapMsgRx"], value)

    @property
    def BootstrapMsgTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bootstrap Msg Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BootstrapMsgTx"])

    @BootstrapMsgTx.setter
    def BootstrapMsgTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BootstrapMsgTx"], value)

    @property
    def DatamdtTLVRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DataMDT TLV Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DatamdtTLVRx"])

    @DatamdtTLVRx.setter
    def DatamdtTLVRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DatamdtTLVRx"], value)

    @property
    def DatamdtTLVTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DataMDT TLV Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DatamdtTLVTx"])

    @DatamdtTLVTx.setter
    def DatamdtTLVTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DatamdtTLVTx"], value)

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
    def JoinSGRPTRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(S,G,RPT) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinSGRPTRx"])

    @JoinSGRPTRx.setter
    def JoinSGRPTRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinSGRPTRx"], value)

    @property
    def JoinSGRPTTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(S,G,RPT) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinSGRPTTx"])

    @JoinSGRPTTx.setter
    def JoinSGRPTTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinSGRPTTx"], value)

    @property
    def JoinSGRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(S,G) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinSGRx"])

    @JoinSGRx.setter
    def JoinSGRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinSGRx"], value)

    @property
    def JoinSGTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(S,G) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinSGTx"])

    @JoinSGTx.setter
    def JoinSGTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinSGTx"], value)

    @property
    def JoinXGRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(X,G) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinXGRx"])

    @JoinXGRx.setter
    def JoinXGRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinXGRx"], value)

    @property
    def JoinXGTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(X,G) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinXGTx"])

    @JoinXGTx.setter
    def JoinXGTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinXGTx"], value)

    @property
    def JoinXXRPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(X,X,RP) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinXXRPRx"])

    @JoinXXRPRx.setter
    def JoinXXRPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinXXRPRx"], value)

    @property
    def JoinXXRPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Join(X,X,RP) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinXXRPTx"])

    @JoinXXRPTx.setter
    def JoinXXRPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinXXRPTx"], value)

    @property
    def NbrsLearnt(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Nbrs. Learnt
        """
        return self._get_attribute(self._SDM_ATT_MAP["NbrsLearnt"])

    @NbrsLearnt.setter
    def NbrsLearnt(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NbrsLearnt"], value)

    @property
    def NormalCRPAdvMsgRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Normal C-RP-Adv Msg Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NormalCRPAdvMsgRx"])

    @NormalCRPAdvMsgRx.setter
    def NormalCRPAdvMsgRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NormalCRPAdvMsgRx"], value)

    @property
    def NormalCRPAdvMsgTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Normal C-RP-Adv Msg Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NormalCRPAdvMsgTx"])

    @NormalCRPAdvMsgTx.setter
    def NormalCRPAdvMsgTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NormalCRPAdvMsgTx"], value)

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
    def PruneSGRPTRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(S,G,RPT) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneSGRPTRx"])

    @PruneSGRPTRx.setter
    def PruneSGRPTRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneSGRPTRx"], value)

    @property
    def PruneSGRPTTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(S,G,RPT) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneSGRPTTx"])

    @PruneSGRPTTx.setter
    def PruneSGRPTTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneSGRPTTx"], value)

    @property
    def PruneSGRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(S,G) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneSGRx"])

    @PruneSGRx.setter
    def PruneSGRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneSGRx"], value)

    @property
    def PruneSGTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(S,G) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneSGTx"])

    @PruneSGTx.setter
    def PruneSGTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneSGTx"], value)

    @property
    def PruneXGRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(X,G) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneXGRx"])

    @PruneXGRx.setter
    def PruneXGRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneXGRx"], value)

    @property
    def PruneXGTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(X,G) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneXGTx"])

    @PruneXGTx.setter
    def PruneXGTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneXGTx"], value)

    @property
    def PruneXXRPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(X,X,RP) Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneXXRPRx"])

    @PruneXXRPRx.setter
    def PruneXXRPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneXXRPRx"], value)

    @property
    def PruneXXRPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prune(X,X,RP) Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneXXRPTx"])

    @PruneXXRPTx.setter
    def PruneXXRPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneXXRPTx"], value)

    @property
    def RegisterRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Register Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisterRx"])

    @RegisterRx.setter
    def RegisterRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisterRx"], value)

    @property
    def RegisterTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Register Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisterTx"])

    @RegisterTx.setter
    def RegisterTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisterTx"], value)

    @property
    def RegisternullRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RegisterNull Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisternullRx"])

    @RegisternullRx.setter
    def RegisternullRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisternullRx"], value)

    @property
    def RegisternullTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RegisterNull Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisternullTx"])

    @RegisternullTx.setter
    def RegisternullTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisternullTx"], value)

    @property
    def RegisterstopRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RegisterStop Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisterstopRx"])

    @RegisterstopRx.setter
    def RegisterstopRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisterstopRx"], value)

    @property
    def RegisterstopTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RegisterStop Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegisterstopTx"])

    @RegisterstopTx.setter
    def RegisterstopTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegisterstopTx"], value)

    @property
    def RtrsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rtrs. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["RtrsConfigured"])

    @RtrsConfigured.setter
    def RtrsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RtrsConfigured"], value)

    @property
    def RtrsRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rtrs. Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["RtrsRunning"])

    @RtrsRunning.setter
    def RtrsRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RtrsRunning"], value)

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
    def ShutdownCRPAdvMsgRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Shutdown C-RP-Adv Msg Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShutdownCRPAdvMsgRx"])

    @ShutdownCRPAdvMsgRx.setter
    def ShutdownCRPAdvMsgRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShutdownCRPAdvMsgRx"], value)

    @property
    def ShutdownCRPAdvMsgTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Shutdown C-RP-Adv Msg Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShutdownCRPAdvMsgTx"])

    @ShutdownCRPAdvMsgTx.setter
    def ShutdownCRPAdvMsgTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShutdownCRPAdvMsgTx"], value)

    def update(
        self,
        BootstrapMsgRx=None,
        BootstrapMsgTx=None,
        DatamdtTLVRx=None,
        DatamdtTLVTx=None,
        HellosRx=None,
        HellosTx=None,
        JoinSGRPTRx=None,
        JoinSGRPTTx=None,
        JoinSGRx=None,
        JoinSGTx=None,
        JoinXGRx=None,
        JoinXGTx=None,
        JoinXXRPRx=None,
        JoinXXRPTx=None,
        NbrsLearnt=None,
        NormalCRPAdvMsgRx=None,
        NormalCRPAdvMsgTx=None,
        PortName=None,
        PruneSGRPTRx=None,
        PruneSGRPTTx=None,
        PruneSGRx=None,
        PruneSGTx=None,
        PruneXGRx=None,
        PruneXGTx=None,
        PruneXXRPRx=None,
        PruneXXRPTx=None,
        RegisterRx=None,
        RegisterTx=None,
        RegisternullRx=None,
        RegisternullTx=None,
        RegisterstopRx=None,
        RegisterstopTx=None,
        RtrsConfigured=None,
        RtrsRunning=None,
        SessionFlapCount=None,
        ShutdownCRPAdvMsgRx=None,
        ShutdownCRPAdvMsgTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> PimsmAggregatedStatistics
        """Updates pimsmAggregatedStatistics resource on the server.

        Args
        ----
        - BootstrapMsgRx (bool): Bootstrap Msg Rx
        - BootstrapMsgTx (bool): Bootstrap Msg Tx
        - DatamdtTLVRx (bool): DataMDT TLV Rx
        - DatamdtTLVTx (bool): DataMDT TLV Tx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - JoinSGRPTRx (bool): Join(S,G,RPT) Rx
        - JoinSGRPTTx (bool): Join(S,G,RPT) Tx
        - JoinSGRx (bool): Join(S,G) Rx
        - JoinSGTx (bool): Join(S,G) Tx
        - JoinXGRx (bool): Join(X,G) Rx
        - JoinXGTx (bool): Join(X,G) Tx
        - JoinXXRPRx (bool): Join(X,X,RP) Rx
        - JoinXXRPTx (bool): Join(X,X,RP) Tx
        - NbrsLearnt (bool): Nbrs. Learnt
        - NormalCRPAdvMsgRx (bool): Normal C-RP-Adv Msg Rx
        - NormalCRPAdvMsgTx (bool): Normal C-RP-Adv Msg Tx
        - PortName (bool): Port Name
        - PruneSGRPTRx (bool): Prune(S,G,RPT) Rx
        - PruneSGRPTTx (bool): Prune(S,G,RPT) Tx
        - PruneSGRx (bool): Prune(S,G) Rx
        - PruneSGTx (bool): Prune(S,G) Tx
        - PruneXGRx (bool): Prune(X,G) Rx
        - PruneXGTx (bool): Prune(X,G) Tx
        - PruneXXRPRx (bool): Prune(X,X,RP) Rx
        - PruneXXRPTx (bool): Prune(X,X,RP) Tx
        - RegisterRx (bool): Register Rx
        - RegisterTx (bool): Register Tx
        - RegisternullRx (bool): RegisterNull Rx
        - RegisternullTx (bool): RegisterNull Tx
        - RegisterstopRx (bool): RegisterStop Rx
        - RegisterstopTx (bool): RegisterStop Tx
        - RtrsConfigured (bool): Rtrs. Configured
        - RtrsRunning (bool): Rtrs. Running
        - SessionFlapCount (bool): Session Flap Count
        - ShutdownCRPAdvMsgRx (bool): Shutdown C-RP-Adv Msg Rx
        - ShutdownCRPAdvMsgTx (bool): Shutdown C-RP-Adv Msg Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BootstrapMsgRx=None,
        BootstrapMsgTx=None,
        DatamdtTLVRx=None,
        DatamdtTLVTx=None,
        HellosRx=None,
        HellosTx=None,
        JoinSGRPTRx=None,
        JoinSGRPTTx=None,
        JoinSGRx=None,
        JoinSGTx=None,
        JoinXGRx=None,
        JoinXGTx=None,
        JoinXXRPRx=None,
        JoinXXRPTx=None,
        NbrsLearnt=None,
        NormalCRPAdvMsgRx=None,
        NormalCRPAdvMsgTx=None,
        PortName=None,
        PruneSGRPTRx=None,
        PruneSGRPTTx=None,
        PruneSGRx=None,
        PruneSGTx=None,
        PruneXGRx=None,
        PruneXGTx=None,
        PruneXXRPRx=None,
        PruneXXRPTx=None,
        RegisterRx=None,
        RegisterTx=None,
        RegisternullRx=None,
        RegisternullTx=None,
        RegisterstopRx=None,
        RegisterstopTx=None,
        RtrsConfigured=None,
        RtrsRunning=None,
        SessionFlapCount=None,
        ShutdownCRPAdvMsgRx=None,
        ShutdownCRPAdvMsgTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> PimsmAggregatedStatistics
        """Finds and retrieves pimsmAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pimsmAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pimsmAggregatedStatistics resources from the server.

        Args
        ----
        - BootstrapMsgRx (bool): Bootstrap Msg Rx
        - BootstrapMsgTx (bool): Bootstrap Msg Tx
        - DatamdtTLVRx (bool): DataMDT TLV Rx
        - DatamdtTLVTx (bool): DataMDT TLV Tx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - JoinSGRPTRx (bool): Join(S,G,RPT) Rx
        - JoinSGRPTTx (bool): Join(S,G,RPT) Tx
        - JoinSGRx (bool): Join(S,G) Rx
        - JoinSGTx (bool): Join(S,G) Tx
        - JoinXGRx (bool): Join(X,G) Rx
        - JoinXGTx (bool): Join(X,G) Tx
        - JoinXXRPRx (bool): Join(X,X,RP) Rx
        - JoinXXRPTx (bool): Join(X,X,RP) Tx
        - NbrsLearnt (bool): Nbrs. Learnt
        - NormalCRPAdvMsgRx (bool): Normal C-RP-Adv Msg Rx
        - NormalCRPAdvMsgTx (bool): Normal C-RP-Adv Msg Tx
        - PortName (bool): Port Name
        - PruneSGRPTRx (bool): Prune(S,G,RPT) Rx
        - PruneSGRPTTx (bool): Prune(S,G,RPT) Tx
        - PruneSGRx (bool): Prune(S,G) Rx
        - PruneSGTx (bool): Prune(S,G) Tx
        - PruneXGRx (bool): Prune(X,G) Rx
        - PruneXGTx (bool): Prune(X,G) Tx
        - PruneXXRPRx (bool): Prune(X,X,RP) Rx
        - PruneXXRPTx (bool): Prune(X,X,RP) Tx
        - RegisterRx (bool): Register Rx
        - RegisterTx (bool): Register Tx
        - RegisternullRx (bool): RegisterNull Rx
        - RegisternullTx (bool): RegisterNull Tx
        - RegisterstopRx (bool): RegisterStop Rx
        - RegisterstopTx (bool): RegisterStop Tx
        - RtrsConfigured (bool): Rtrs. Configured
        - RtrsRunning (bool): Rtrs. Running
        - SessionFlapCount (bool): Session Flap Count
        - ShutdownCRPAdvMsgRx (bool): Shutdown C-RP-Adv Msg Rx
        - ShutdownCRPAdvMsgTx (bool): Shutdown C-RP-Adv Msg Tx

        Returns
        -------
        - self: This instance with matching pimsmAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pimsmAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pimsmAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
