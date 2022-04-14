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


class Egress(Base):
    """DEPRECATED This object provides different options for Egress Tracking.
    The Egress class encapsulates a required egress resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "egress"
    _SDM_ATT_MAP = {
        "AvailableEncapsulations": "availableEncapsulations",
        "AvailableOffsets": "availableOffsets",
        "CustomOffsetBits": "customOffsetBits",
        "CustomWidthBits": "customWidthBits",
        "Enabled": "enabled",
        "Encapsulation": "encapsulation",
        "Offset": "offset",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Egress, self).__init__(parent, list_op)

    @property
    def FieldOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.egress.fieldoffset.fieldoffset.FieldOffset): An instance of the FieldOffset class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.egress.fieldoffset.fieldoffset import (
            FieldOffset,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FieldOffset", None) is not None:
                return self._properties.get("FieldOffset")
        return FieldOffset(self)._select()

    @property
    def AvailableEncapsulations(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Specifies the available Encapsulations for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableEncapsulations"])

    @property
    def AvailableOffsets(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Specifies the available Offsets for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableOffsets"])

    @property
    def CustomOffsetBits(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomOffsetBits"])

    @CustomOffsetBits.setter
    def CustomOffsetBits(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomOffsetBits"], value)

    @property
    def CustomWidthBits(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomWidthBits"])

    @CustomWidthBits.setter
    def CustomWidthBits(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomWidthBits"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, egress tracking is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Encapsulation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the Encapsulation for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encapsulation"])

    @Encapsulation.setter
    def Encapsulation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encapsulation"], value)

    @property
    def Offset(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the Offset for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Offset"])

    @Offset.setter
    def Offset(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Offset"], value)

    def update(
        self,
        CustomOffsetBits=None,
        CustomWidthBits=None,
        Enabled=None,
        Encapsulation=None,
        Offset=None,
    ):
        # type: (int, int, bool, str, str) -> Egress
        """Updates egress resource on the server.

        Args
        ----
        - CustomOffsetBits (number): Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        - CustomWidthBits (number): Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        - Enabled (bool): If true, egress tracking is enabled.
        - Encapsulation (str): Specifies the Encapsulation for Egress Tracking.
        - Offset (str): Specifies the Offset for Egress Tracking.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvailableEncapsulations=None,
        AvailableOffsets=None,
        CustomOffsetBits=None,
        CustomWidthBits=None,
        Enabled=None,
        Encapsulation=None,
        Offset=None,
    ):
        # type: (List[str], List[str], int, int, bool, str, str) -> Egress
        """Finds and retrieves egress resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egress resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egress resources from the server.

        Args
        ----
        - AvailableEncapsulations (list(str)): Specifies the available Encapsulations for Egress Tracking.
        - AvailableOffsets (list(str)): Specifies the available Offsets for Egress Tracking.
        - CustomOffsetBits (number): Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        - CustomWidthBits (number): Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        - Enabled (bool): If true, egress tracking is enabled.
        - Encapsulation (str): Specifies the Encapsulation for Egress Tracking.
        - Offset (str): Specifies the Offset for Egress Tracking.

        Returns
        -------
        - self: This instance with matching egress resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egress data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egress resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
