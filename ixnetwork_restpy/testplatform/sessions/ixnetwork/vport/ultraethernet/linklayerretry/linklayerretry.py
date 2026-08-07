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


class LinkLayerRetry(Base):
    """
    The LinkLayerRetry class encapsulates a required linkLayerRetry resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "linkLayerRetry"
    _SDM_ATT_MAP = {
        "DataAgeTimerMax": "dataAgeTimerMax",
        "InitData": "initData",
        "InitDataIsTimeStamp": "initDataIsTimeStamp",
        "InitRttIsValid": "initRttIsValid",
        "InitRttNs": "initRttNs",
        "InitialSequence": "initialSequence",
        "LlrFlushBehavior": "llrFlushBehavior",
        "LlrInitBehavior": "llrInitBehavior",
        "LocalEnable": "localEnable",
        "OutstandingDataMax": "outstandingDataMax",
        "OutstandingSeqMax": "outstandingSeqMax",
        "PcsLostStatusTimerMax": "pcsLostStatusTimerMax",
        "ReInitOnDiscard": "reInitOnDiscard",
        "RemoteEnable": "remoteEnable",
        "ReplayCtMax": "replayCtMax",
        "ReplayTimerMax": "replayTimerMax",
        "ReplayedFrameTimestampMode": "replayedFrameTimestampMode",
    }
    _SDM_ENUM_MAP = {
        "llrFlushBehavior": ["discard", "block", "bestEffort"],
        "llrInitBehavior": ["discard", "block", "bestEffort"],
        "replayedFrameTimestampMode": ["current", "original"],
    }

    def __init__(self, parent, list_op=False):
        super(LinkLayerRetry, self).__init__(parent, list_op)

    @property
    def DataAgeTimerMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum time (in nanoseconds) data may sit unacknowledged in the replay buffer before it is discarded as too old.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataAgeTimerMax"])

    @DataAgeTimerMax.setter
    def DataAgeTimerMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataAgeTimerMax"], value)

    @property
    def InitData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Initial 2-byte data value placed in the transmitted LLR_INIT CtlOS (ignored when INIT data is timestamp is enabled). Range: 00 00 to FF FF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitData"])

    @InitData.setter
    def InitData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitData"], value)

    @property
    def InitDataIsTimeStamp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When enabled, the LLR_INIT CtlOS data field is overwritten with the current timestamp instead of the custom user value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitDataIsTimeStamp"])

    @InitDataIsTimeStamp.setter
    def InitDataIsTimeStamp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitDataIsTimeStamp"], value)

    @property
    def InitRttIsValid(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether the most recent LLR_INIT round-trip-time measurement is valid.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitRttIsValid"])

    @property
    def InitRttNs(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Measured round-trip time of the LLR_INIT CtlOS handshake, in nanoseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitRttNs"])

    @property
    def InitialSequence(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Initial 3-byte sequence value placed in the first transmitted LLR_INIT CtlOS. Range: 00 00 00 to 0F FF FF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialSequence"])

    @InitialSequence.setter
    def InitialSequence(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialSequence"], value)

    @property
    def LlrFlushBehavior(self):
        # type: () -> str
        """
        Returns
        -------
        - str(discard | block | bestEffort): Controls how the TX LLR handles outgoing frames while in the FLUSH state (Discard / Block / Best Effort).
        """
        return self._get_attribute(self._SDM_ATT_MAP["LlrFlushBehavior"])

    @LlrFlushBehavior.setter
    def LlrFlushBehavior(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LlrFlushBehavior"], value)

    @property
    def LlrInitBehavior(self):
        # type: () -> str
        """
        Returns
        -------
        - str(discard | block | bestEffort): Controls how the TX LLR handles outgoing frames while in the INIT state (Discard / Block / Best Effort).
        """
        return self._get_attribute(self._SDM_ATT_MAP["LlrInitBehavior"])

    @LlrInitBehavior.setter
    def LlrInitBehavior(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LlrInitBehavior"], value)

    @property
    def LocalEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables LLR reception on this port. When ON, the port is allowed to receive LLR_INIT and operate as an LLR receiver.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalEnable"])

    @LocalEnable.setter
    def LocalEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalEnable"], value)

    @property
    def OutstandingDataMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of unacknowledged bytes allowed in flight. Should be set to the link's bandwidth-delay product for correct pause/PFC behavior.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutstandingDataMax"])

    @OutstandingDataMax.setter
    def OutstandingDataMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutstandingDataMax"], value)

    @property
    def OutstandingSeqMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of unacknowledged frames allowed in flight. Caps how many transmitted frames may remain unacknowledged at any time.Range-1600G -> 0-16383800G -> 0-8191400G -> 0-4095200G -> 0-2047
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutstandingSeqMax"])

    @OutstandingSeqMax.setter
    def OutstandingSeqMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutstandingSeqMax"], value)

    @property
    def PcsLostStatusTimerMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time (in nanoseconds) the PCS link may stay down before the LLR transmit state machine forces a transition to FLUSH.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsLostStatusTimerMax"])

    @PcsLostStatusTimerMax.setter
    def PcsLostStatusTimerMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsLostStatusTimerMax"], value)

    @property
    def ReInitOnDiscard(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, the LLR automatically re-initializes after a replay failure. When OFF, it waits for manual intervention.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReInitOnDiscard"])

    @ReInitOnDiscard.setter
    def ReInitOnDiscard(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReInitOnDiscard"], value)

    @property
    def RemoteEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables LLR transmission on this port. When ON, the port may send LLR_INIT and operate as an LLR transmitter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteEnable"])

    @RemoteEnable.setter
    def RemoteEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteEnable"], value)

    @property
    def ReplayCtMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of replay attempts before the LLR gives up and enters the FLUSH state. Use 255 for unlimited retries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplayCtMax"])

    @ReplayCtMax.setter
    def ReplayCtMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReplayCtMax"], value)

    @property
    def ReplayTimerMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time (in nanoseconds) before a missing acknowledgment triggers a replay of unacknowledged frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplayTimerMax"])

    @ReplayTimerMax.setter
    def ReplayTimerMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReplayTimerMax"], value)

    @property
    def ReplayedFrameTimestampMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(current | original): Value current would insert current timestamp into replayed frame and value original inserts timestamp saved from original frame into replayed frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplayedFrameTimestampMode"])

    @ReplayedFrameTimestampMode.setter
    def ReplayedFrameTimestampMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReplayedFrameTimestampMode"], value)

    def update(
        self,
        DataAgeTimerMax=None,
        InitData=None,
        InitDataIsTimeStamp=None,
        InitialSequence=None,
        LlrFlushBehavior=None,
        LlrInitBehavior=None,
        LocalEnable=None,
        OutstandingDataMax=None,
        OutstandingSeqMax=None,
        PcsLostStatusTimerMax=None,
        ReInitOnDiscard=None,
        RemoteEnable=None,
        ReplayCtMax=None,
        ReplayTimerMax=None,
        ReplayedFrameTimestampMode=None,
    ):
        # type: (int, str, bool, str, str, str, bool, int, int, int, bool, bool, int, int, str) -> LinkLayerRetry
        """Updates linkLayerRetry resource on the server.

        Args
        ----
        - DataAgeTimerMax (number): Maximum time (in nanoseconds) data may sit unacknowledged in the replay buffer before it is discarded as too old.
        - InitData (str): Initial 2-byte data value placed in the transmitted LLR_INIT CtlOS (ignored when INIT data is timestamp is enabled). Range: 00 00 to FF FF.
        - InitDataIsTimeStamp (bool): When enabled, the LLR_INIT CtlOS data field is overwritten with the current timestamp instead of the custom user value.
        - InitialSequence (str): Initial 3-byte sequence value placed in the first transmitted LLR_INIT CtlOS. Range: 00 00 00 to 0F FF FF.
        - LlrFlushBehavior (str(discard | block | bestEffort)): Controls how the TX LLR handles outgoing frames while in the FLUSH state (Discard / Block / Best Effort).
        - LlrInitBehavior (str(discard | block | bestEffort)): Controls how the TX LLR handles outgoing frames while in the INIT state (Discard / Block / Best Effort).
        - LocalEnable (bool): Enables LLR reception on this port. When ON, the port is allowed to receive LLR_INIT and operate as an LLR receiver.
        - OutstandingDataMax (number): Maximum number of unacknowledged bytes allowed in flight. Should be set to the link's bandwidth-delay product for correct pause/PFC behavior.
        - OutstandingSeqMax (number): Maximum number of unacknowledged frames allowed in flight. Caps how many transmitted frames may remain unacknowledged at any time.Range-1600G -> 0-16383800G -> 0-8191400G -> 0-4095200G -> 0-2047
        - PcsLostStatusTimerMax (number): Time (in nanoseconds) the PCS link may stay down before the LLR transmit state machine forces a transition to FLUSH.
        - ReInitOnDiscard (bool): When ON, the LLR automatically re-initializes after a replay failure. When OFF, it waits for manual intervention.
        - RemoteEnable (bool): Enables LLR transmission on this port. When ON, the port may send LLR_INIT and operate as an LLR transmitter.
        - ReplayCtMax (number): Maximum number of replay attempts before the LLR gives up and enters the FLUSH state. Use 255 for unlimited retries.
        - ReplayTimerMax (number): Time (in nanoseconds) before a missing acknowledgment triggers a replay of unacknowledged frames.
        - ReplayedFrameTimestampMode (str(current | original)): Value current would insert current timestamp into replayed frame and value original inserts timestamp saved from original frame into replayed frame.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DataAgeTimerMax=None,
        InitData=None,
        InitDataIsTimeStamp=None,
        InitRttIsValid=None,
        InitRttNs=None,
        InitialSequence=None,
        LlrFlushBehavior=None,
        LlrInitBehavior=None,
        LocalEnable=None,
        OutstandingDataMax=None,
        OutstandingSeqMax=None,
        PcsLostStatusTimerMax=None,
        ReInitOnDiscard=None,
        RemoteEnable=None,
        ReplayCtMax=None,
        ReplayTimerMax=None,
        ReplayedFrameTimestampMode=None,
    ):
        # type: (int, str, bool, bool, str, str, str, str, bool, int, int, int, bool, bool, int, int, str) -> LinkLayerRetry
        """Finds and retrieves linkLayerRetry resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve linkLayerRetry resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all linkLayerRetry resources from the server.

        Args
        ----
        - DataAgeTimerMax (number): Maximum time (in nanoseconds) data may sit unacknowledged in the replay buffer before it is discarded as too old.
        - InitData (str): Initial 2-byte data value placed in the transmitted LLR_INIT CtlOS (ignored when INIT data is timestamp is enabled). Range: 00 00 to FF FF.
        - InitDataIsTimeStamp (bool): When enabled, the LLR_INIT CtlOS data field is overwritten with the current timestamp instead of the custom user value.
        - InitRttIsValid (bool): Indicates whether the most recent LLR_INIT round-trip-time measurement is valid.
        - InitRttNs (str): Measured round-trip time of the LLR_INIT CtlOS handshake, in nanoseconds.
        - InitialSequence (str): Initial 3-byte sequence value placed in the first transmitted LLR_INIT CtlOS. Range: 00 00 00 to 0F FF FF.
        - LlrFlushBehavior (str(discard | block | bestEffort)): Controls how the TX LLR handles outgoing frames while in the FLUSH state (Discard / Block / Best Effort).
        - LlrInitBehavior (str(discard | block | bestEffort)): Controls how the TX LLR handles outgoing frames while in the INIT state (Discard / Block / Best Effort).
        - LocalEnable (bool): Enables LLR reception on this port. When ON, the port is allowed to receive LLR_INIT and operate as an LLR receiver.
        - OutstandingDataMax (number): Maximum number of unacknowledged bytes allowed in flight. Should be set to the link's bandwidth-delay product for correct pause/PFC behavior.
        - OutstandingSeqMax (number): Maximum number of unacknowledged frames allowed in flight. Caps how many transmitted frames may remain unacknowledged at any time.Range-1600G -> 0-16383800G -> 0-8191400G -> 0-4095200G -> 0-2047
        - PcsLostStatusTimerMax (number): Time (in nanoseconds) the PCS link may stay down before the LLR transmit state machine forces a transition to FLUSH.
        - ReInitOnDiscard (bool): When ON, the LLR automatically re-initializes after a replay failure. When OFF, it waits for manual intervention.
        - RemoteEnable (bool): Enables LLR transmission on this port. When ON, the port may send LLR_INIT and operate as an LLR transmitter.
        - ReplayCtMax (number): Maximum number of replay attempts before the LLR gives up and enters the FLUSH state. Use 255 for unlimited retries.
        - ReplayTimerMax (number): Time (in nanoseconds) before a missing acknowledgment triggers a replay of unacknowledged frames.
        - ReplayedFrameTimestampMode (str(current | original)): Value current would insert current timestamp into replayed frame and value original inserts timestamp saved from original frame into replayed frame.

        Returns
        -------
        - self: This instance with matching linkLayerRetry resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of linkLayerRetry data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the linkLayerRetry resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
