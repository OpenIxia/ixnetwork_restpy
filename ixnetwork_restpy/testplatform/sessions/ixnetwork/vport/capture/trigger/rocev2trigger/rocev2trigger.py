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


class Rocev2Trigger(Base):
    """
    The Rocev2Trigger class encapsulates a required rocev2Trigger resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rocev2Trigger"
    _SDM_ATT_MAP = {
        "TriggerABitSetEnable": "triggerABitSetEnable",
        "TriggerAckOpcodeEnable": "triggerAckOpcodeEnable",
        "TriggerCnpOpcodeEnable": "triggerCnpOpcodeEnable",
        "TriggerDataMaxLatencyEnable": "triggerDataMaxLatencyEnable",
        "TriggerDuplicateEnable": "triggerDuplicateEnable",
        "TriggerFirstOpcodeEnable": "triggerFirstOpcodeEnable",
        "TriggerInvalidRoceEnable": "triggerInvalidRoceEnable",
        "TriggerLastOpcodeEnable": "triggerLastOpcodeEnable",
        "TriggerMaxLatency": "triggerMaxLatency",
        "TriggerMiddleOpcodeEnable": "triggerMiddleOpcodeEnable",
        "TriggerNakOpcodeEnable": "triggerNakOpcodeEnable",
        "TriggerOnlyOpcodeEnable": "triggerOnlyOpcodeEnable",
        "TriggerOpcodeOrderErrorEnable": "triggerOpcodeOrderErrorEnable",
        "TriggerPauseEnable": "triggerPauseEnable",
        "TriggerQpidLookupFailureEnable": "triggerQpidLookupFailureEnable",
        "TriggerReorderEnable": "triggerReorderEnable",
        "TriggerSequenceErrorEnable": "triggerSequenceErrorEnable",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Rocev2Trigger, self).__init__(parent, list_op)

    @property
    def TriggerABitSetEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerABitSetEnable"])

    @TriggerABitSetEnable.setter
    def TriggerABitSetEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerABitSetEnable"], value)

    @property
    def TriggerAckOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerAckOpcodeEnable"])

    @TriggerAckOpcodeEnable.setter
    def TriggerAckOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerAckOpcodeEnable"], value)

    @property
    def TriggerCnpOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerCnpOpcodeEnable"])

    @TriggerCnpOpcodeEnable.setter
    def TriggerCnpOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerCnpOpcodeEnable"], value)

    @property
    def TriggerDataMaxLatencyEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerDataMaxLatencyEnable"])

    @TriggerDataMaxLatencyEnable.setter
    def TriggerDataMaxLatencyEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerDataMaxLatencyEnable"], value)

    @property
    def TriggerDuplicateEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerDuplicateEnable"])

    @TriggerDuplicateEnable.setter
    def TriggerDuplicateEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerDuplicateEnable"], value)

    @property
    def TriggerFirstOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerFirstOpcodeEnable"])

    @TriggerFirstOpcodeEnable.setter
    def TriggerFirstOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerFirstOpcodeEnable"], value)

    @property
    def TriggerInvalidRoceEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerInvalidRoceEnable"])

    @TriggerInvalidRoceEnable.setter
    def TriggerInvalidRoceEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerInvalidRoceEnable"], value)

    @property
    def TriggerLastOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerLastOpcodeEnable"])

    @TriggerLastOpcodeEnable.setter
    def TriggerLastOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerLastOpcodeEnable"], value)

    @property
    def TriggerMaxLatency(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerMaxLatency"])

    @TriggerMaxLatency.setter
    def TriggerMaxLatency(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerMaxLatency"], value)

    @property
    def TriggerMiddleOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerMiddleOpcodeEnable"])

    @TriggerMiddleOpcodeEnable.setter
    def TriggerMiddleOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerMiddleOpcodeEnable"], value)

    @property
    def TriggerNakOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerNakOpcodeEnable"])

    @TriggerNakOpcodeEnable.setter
    def TriggerNakOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerNakOpcodeEnable"], value)

    @property
    def TriggerOnlyOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerOnlyOpcodeEnable"])

    @TriggerOnlyOpcodeEnable.setter
    def TriggerOnlyOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerOnlyOpcodeEnable"], value)

    @property
    def TriggerOpcodeOrderErrorEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerOpcodeOrderErrorEnable"])

    @TriggerOpcodeOrderErrorEnable.setter
    def TriggerOpcodeOrderErrorEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerOpcodeOrderErrorEnable"], value)

    @property
    def TriggerPauseEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerPauseEnable"])

    @TriggerPauseEnable.setter
    def TriggerPauseEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerPauseEnable"], value)

    @property
    def TriggerQpidLookupFailureEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerQpidLookupFailureEnable"])

    @TriggerQpidLookupFailureEnable.setter
    def TriggerQpidLookupFailureEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerQpidLookupFailureEnable"], value)

    @property
    def TriggerReorderEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerReorderEnable"])

    @TriggerReorderEnable.setter
    def TriggerReorderEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerReorderEnable"], value)

    @property
    def TriggerSequenceErrorEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerSequenceErrorEnable"])

    @TriggerSequenceErrorEnable.setter
    def TriggerSequenceErrorEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerSequenceErrorEnable"], value)

    def update(
        self,
        TriggerABitSetEnable=None,
        TriggerAckOpcodeEnable=None,
        TriggerCnpOpcodeEnable=None,
        TriggerDataMaxLatencyEnable=None,
        TriggerDuplicateEnable=None,
        TriggerFirstOpcodeEnable=None,
        TriggerInvalidRoceEnable=None,
        TriggerLastOpcodeEnable=None,
        TriggerMaxLatency=None,
        TriggerMiddleOpcodeEnable=None,
        TriggerNakOpcodeEnable=None,
        TriggerOnlyOpcodeEnable=None,
        TriggerOpcodeOrderErrorEnable=None,
        TriggerPauseEnable=None,
        TriggerQpidLookupFailureEnable=None,
        TriggerReorderEnable=None,
        TriggerSequenceErrorEnable=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool) -> Rocev2Trigger
        """Updates rocev2Trigger resource on the server.

        Args
        ----
        - TriggerABitSetEnable (bool):
        - TriggerAckOpcodeEnable (bool):
        - TriggerCnpOpcodeEnable (bool):
        - TriggerDataMaxLatencyEnable (bool):
        - TriggerDuplicateEnable (bool):
        - TriggerFirstOpcodeEnable (bool):
        - TriggerInvalidRoceEnable (bool):
        - TriggerLastOpcodeEnable (bool):
        - TriggerMaxLatency (number):
        - TriggerMiddleOpcodeEnable (bool):
        - TriggerNakOpcodeEnable (bool):
        - TriggerOnlyOpcodeEnable (bool):
        - TriggerOpcodeOrderErrorEnable (bool):
        - TriggerPauseEnable (bool):
        - TriggerQpidLookupFailureEnable (bool):
        - TriggerReorderEnable (bool):
        - TriggerSequenceErrorEnable (bool):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        TriggerABitSetEnable=None,
        TriggerAckOpcodeEnable=None,
        TriggerCnpOpcodeEnable=None,
        TriggerDataMaxLatencyEnable=None,
        TriggerDuplicateEnable=None,
        TriggerFirstOpcodeEnable=None,
        TriggerInvalidRoceEnable=None,
        TriggerLastOpcodeEnable=None,
        TriggerMaxLatency=None,
        TriggerMiddleOpcodeEnable=None,
        TriggerNakOpcodeEnable=None,
        TriggerOnlyOpcodeEnable=None,
        TriggerOpcodeOrderErrorEnable=None,
        TriggerPauseEnable=None,
        TriggerQpidLookupFailureEnable=None,
        TriggerReorderEnable=None,
        TriggerSequenceErrorEnable=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool) -> Rocev2Trigger
        """Finds and retrieves rocev2Trigger resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rocev2Trigger resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rocev2Trigger resources from the server.

        Args
        ----
        - TriggerABitSetEnable (bool):
        - TriggerAckOpcodeEnable (bool):
        - TriggerCnpOpcodeEnable (bool):
        - TriggerDataMaxLatencyEnable (bool):
        - TriggerDuplicateEnable (bool):
        - TriggerFirstOpcodeEnable (bool):
        - TriggerInvalidRoceEnable (bool):
        - TriggerLastOpcodeEnable (bool):
        - TriggerMaxLatency (number):
        - TriggerMiddleOpcodeEnable (bool):
        - TriggerNakOpcodeEnable (bool):
        - TriggerOnlyOpcodeEnable (bool):
        - TriggerOpcodeOrderErrorEnable (bool):
        - TriggerPauseEnable (bool):
        - TriggerQpidLookupFailureEnable (bool):
        - TriggerReorderEnable (bool):
        - TriggerSequenceErrorEnable (bool):

        Returns
        -------
        - self: This instance with matching rocev2Trigger resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rocev2Trigger data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rocev2Trigger resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
