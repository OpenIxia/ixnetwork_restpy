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


class Rocev2Filter(Base):
    """
    The Rocev2Filter class encapsulates a required rocev2Filter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rocev2Filter"
    _SDM_ATT_MAP = {
        "FilterABitSetEnable": "filterABitSetEnable",
        "FilterAckOpcodeEnable": "filterAckOpcodeEnable",
        "FilterCnpOpcodeEnable": "filterCnpOpcodeEnable",
        "FilterDataMaxLatencyEnable": "filterDataMaxLatencyEnable",
        "FilterDuplicateEnable": "filterDuplicateEnable",
        "FilterFirstOpcodeEnable": "filterFirstOpcodeEnable",
        "FilterInvalidRoceEnable": "filterInvalidRoceEnable",
        "FilterLastOpcodeEnable": "filterLastOpcodeEnable",
        "FilterMaxLatency": "filterMaxLatency",
        "FilterMiddleOpcodeEnable": "filterMiddleOpcodeEnable",
        "FilterNakOpcodeEnable": "filterNakOpcodeEnable",
        "FilterOnlyOpcodeEnable": "filterOnlyOpcodeEnable",
        "FilterOpcodeOrderErrorEnable": "filterOpcodeOrderErrorEnable",
        "FilterPauseEnable": "filterPauseEnable",
        "FilterQpidLookupFailureEnable": "filterQpidLookupFailureEnable",
        "FilterReorderEnable": "filterReorderEnable",
        "FilterSequenceErrorEnable": "filterSequenceErrorEnable",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Rocev2Filter, self).__init__(parent, list_op)

    @property
    def FilterABitSetEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterABitSetEnable"])

    @FilterABitSetEnable.setter
    def FilterABitSetEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterABitSetEnable"], value)

    @property
    def FilterAckOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterAckOpcodeEnable"])

    @FilterAckOpcodeEnable.setter
    def FilterAckOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterAckOpcodeEnable"], value)

    @property
    def FilterCnpOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterCnpOpcodeEnable"])

    @FilterCnpOpcodeEnable.setter
    def FilterCnpOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterCnpOpcodeEnable"], value)

    @property
    def FilterDataMaxLatencyEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterDataMaxLatencyEnable"])

    @FilterDataMaxLatencyEnable.setter
    def FilterDataMaxLatencyEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterDataMaxLatencyEnable"], value)

    @property
    def FilterDuplicateEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterDuplicateEnable"])

    @FilterDuplicateEnable.setter
    def FilterDuplicateEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterDuplicateEnable"], value)

    @property
    def FilterFirstOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterFirstOpcodeEnable"])

    @FilterFirstOpcodeEnable.setter
    def FilterFirstOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterFirstOpcodeEnable"], value)

    @property
    def FilterInvalidRoceEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterInvalidRoceEnable"])

    @FilterInvalidRoceEnable.setter
    def FilterInvalidRoceEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterInvalidRoceEnable"], value)

    @property
    def FilterLastOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterLastOpcodeEnable"])

    @FilterLastOpcodeEnable.setter
    def FilterLastOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterLastOpcodeEnable"], value)

    @property
    def FilterMaxLatency(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterMaxLatency"])

    @FilterMaxLatency.setter
    def FilterMaxLatency(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterMaxLatency"], value)

    @property
    def FilterMiddleOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterMiddleOpcodeEnable"])

    @FilterMiddleOpcodeEnable.setter
    def FilterMiddleOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterMiddleOpcodeEnable"], value)

    @property
    def FilterNakOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterNakOpcodeEnable"])

    @FilterNakOpcodeEnable.setter
    def FilterNakOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterNakOpcodeEnable"], value)

    @property
    def FilterOnlyOpcodeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterOnlyOpcodeEnable"])

    @FilterOnlyOpcodeEnable.setter
    def FilterOnlyOpcodeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterOnlyOpcodeEnable"], value)

    @property
    def FilterOpcodeOrderErrorEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterOpcodeOrderErrorEnable"])

    @FilterOpcodeOrderErrorEnable.setter
    def FilterOpcodeOrderErrorEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterOpcodeOrderErrorEnable"], value)

    @property
    def FilterPauseEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterPauseEnable"])

    @FilterPauseEnable.setter
    def FilterPauseEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterPauseEnable"], value)

    @property
    def FilterQpidLookupFailureEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterQpidLookupFailureEnable"])

    @FilterQpidLookupFailureEnable.setter
    def FilterQpidLookupFailureEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterQpidLookupFailureEnable"], value)

    @property
    def FilterReorderEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterReorderEnable"])

    @FilterReorderEnable.setter
    def FilterReorderEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterReorderEnable"], value)

    @property
    def FilterSequenceErrorEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterSequenceErrorEnable"])

    @FilterSequenceErrorEnable.setter
    def FilterSequenceErrorEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterSequenceErrorEnable"], value)

    def update(
        self,
        FilterABitSetEnable=None,
        FilterAckOpcodeEnable=None,
        FilterCnpOpcodeEnable=None,
        FilterDataMaxLatencyEnable=None,
        FilterDuplicateEnable=None,
        FilterFirstOpcodeEnable=None,
        FilterInvalidRoceEnable=None,
        FilterLastOpcodeEnable=None,
        FilterMaxLatency=None,
        FilterMiddleOpcodeEnable=None,
        FilterNakOpcodeEnable=None,
        FilterOnlyOpcodeEnable=None,
        FilterOpcodeOrderErrorEnable=None,
        FilterPauseEnable=None,
        FilterQpidLookupFailureEnable=None,
        FilterReorderEnable=None,
        FilterSequenceErrorEnable=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool) -> Rocev2Filter
        """Updates rocev2Filter resource on the server.

        Args
        ----
        - FilterABitSetEnable (bool):
        - FilterAckOpcodeEnable (bool):
        - FilterCnpOpcodeEnable (bool):
        - FilterDataMaxLatencyEnable (bool):
        - FilterDuplicateEnable (bool):
        - FilterFirstOpcodeEnable (bool):
        - FilterInvalidRoceEnable (bool):
        - FilterLastOpcodeEnable (bool):
        - FilterMaxLatency (number):
        - FilterMiddleOpcodeEnable (bool):
        - FilterNakOpcodeEnable (bool):
        - FilterOnlyOpcodeEnable (bool):
        - FilterOpcodeOrderErrorEnable (bool):
        - FilterPauseEnable (bool):
        - FilterQpidLookupFailureEnable (bool):
        - FilterReorderEnable (bool):
        - FilterSequenceErrorEnable (bool):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        FilterABitSetEnable=None,
        FilterAckOpcodeEnable=None,
        FilterCnpOpcodeEnable=None,
        FilterDataMaxLatencyEnable=None,
        FilterDuplicateEnable=None,
        FilterFirstOpcodeEnable=None,
        FilterInvalidRoceEnable=None,
        FilterLastOpcodeEnable=None,
        FilterMaxLatency=None,
        FilterMiddleOpcodeEnable=None,
        FilterNakOpcodeEnable=None,
        FilterOnlyOpcodeEnable=None,
        FilterOpcodeOrderErrorEnable=None,
        FilterPauseEnable=None,
        FilterQpidLookupFailureEnable=None,
        FilterReorderEnable=None,
        FilterSequenceErrorEnable=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool) -> Rocev2Filter
        """Finds and retrieves rocev2Filter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rocev2Filter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rocev2Filter resources from the server.

        Args
        ----
        - FilterABitSetEnable (bool):
        - FilterAckOpcodeEnable (bool):
        - FilterCnpOpcodeEnable (bool):
        - FilterDataMaxLatencyEnable (bool):
        - FilterDuplicateEnable (bool):
        - FilterFirstOpcodeEnable (bool):
        - FilterInvalidRoceEnable (bool):
        - FilterLastOpcodeEnable (bool):
        - FilterMaxLatency (number):
        - FilterMiddleOpcodeEnable (bool):
        - FilterNakOpcodeEnable (bool):
        - FilterOnlyOpcodeEnable (bool):
        - FilterOpcodeOrderErrorEnable (bool):
        - FilterPauseEnable (bool):
        - FilterQpidLookupFailureEnable (bool):
        - FilterReorderEnable (bool):
        - FilterSequenceErrorEnable (bool):

        Returns
        -------
        - self: This instance with matching rocev2Filter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rocev2Filter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rocev2Filter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
