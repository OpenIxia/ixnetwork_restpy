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


class MulticastRootRange(Base):
    """Configures the multicast root range values.
    The MulticastRootRange class encapsulates a list of multicastRootRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the MulticastRootRange.find() method.
    The list can be managed by using the MulticastRootRange.add() and MulticastRootRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "multicastRootRange"
    _SDM_ATT_MAP = {
        "ContinuousIncrOpaqueValuesAcrossRoot": "continuousIncrOpaqueValuesAcrossRoot",
        "LspCount": "lspCount",
        "LspType": "lspType",
        "RootAddrStep": "rootAddrStep",
        "RootAddress": "rootAddress",
        "RootAddressCount": "rootAddressCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(MulticastRootRange, self).__init__(parent, list_op)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_dba87f250e9ae82d8aff17b985d5ef44.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_dba87f250e9ae82d8aff17b985d5ef44 import (
            OpaqueValueElement,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpaqueValueElement", None) is not None:
                return self._properties.get("OpaqueValueElement")
        return OpaqueValueElement(self)

    @property
    def SourceTrafficRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.sourcetrafficrange_9e3a10265e96d4b6516626b5559092a9.SourceTrafficRange): An instance of the SourceTrafficRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.sourcetrafficrange_9e3a10265e96d4b6516626b5559092a9 import (
            SourceTrafficRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SourceTrafficRange", None) is not None:
                return self._properties.get("SourceTrafficRange")
        return SourceTrafficRange(self)

    @property
    def ContinuousIncrOpaqueValuesAcrossRoot(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Signifies the continuous incremented opaque values across root.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ContinuousIncrOpaqueValuesAcrossRoot"]
        )

    @ContinuousIncrOpaqueValuesAcrossRoot.setter
    def ContinuousIncrOpaqueValuesAcrossRoot(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ContinuousIncrOpaqueValuesAcrossRoot"], value
        )

    @property
    def LspCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the count of LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspCount"])

    @LspCount.setter
    def LspCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspCount"], value)

    @property
    def LspType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(): The type of multicast LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspType"])

    @property
    def RootAddrStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RootAddrStep"])

    @RootAddrStep.setter
    def RootAddrStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RootAddrStep"], value)

    @property
    def RootAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The root address of the multicast LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RootAddress"])

    @RootAddress.setter
    def RootAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RootAddress"], value)

    @property
    def RootAddressCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The root address count for this Multicast FEC range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RootAddressCount"])

    @RootAddressCount.setter
    def RootAddressCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RootAddressCount"], value)

    def update(
        self,
        ContinuousIncrOpaqueValuesAcrossRoot=None,
        LspCount=None,
        RootAddrStep=None,
        RootAddress=None,
        RootAddressCount=None,
    ):
        # type: (bool, int, str, str, int) -> MulticastRootRange
        """Updates multicastRootRange resource on the server.

        Args
        ----
        - ContinuousIncrOpaqueValuesAcrossRoot (bool): Signifies the continuous incremented opaque values across root.
        - LspCount (number): Signifies the count of LSP.
        - RootAddrStep (str): The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        - RootAddress (str): The root address of the multicast LSP.
        - RootAddressCount (number): The root address count for this Multicast FEC range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ContinuousIncrOpaqueValuesAcrossRoot=None,
        LspCount=None,
        RootAddrStep=None,
        RootAddress=None,
        RootAddressCount=None,
    ):
        # type: (bool, int, str, str, int) -> MulticastRootRange
        """Adds a new multicastRootRange resource on the server and adds it to the container.

        Args
        ----
        - ContinuousIncrOpaqueValuesAcrossRoot (bool): Signifies the continuous incremented opaque values across root.
        - LspCount (number): Signifies the count of LSP.
        - RootAddrStep (str): The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        - RootAddress (str): The root address of the multicast LSP.
        - RootAddressCount (number): The root address count for this Multicast FEC range.

        Returns
        -------
        - self: This instance with all currently retrieved multicastRootRange resources using find and the newly added multicastRootRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained multicastRootRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ContinuousIncrOpaqueValuesAcrossRoot=None,
        LspCount=None,
        LspType=None,
        RootAddrStep=None,
        RootAddress=None,
        RootAddressCount=None,
    ):
        # type: (bool, int, str, str, str, int) -> MulticastRootRange
        """Finds and retrieves multicastRootRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastRootRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastRootRange resources from the server.

        Args
        ----
        - ContinuousIncrOpaqueValuesAcrossRoot (bool): Signifies the continuous incremented opaque values across root.
        - LspCount (number): Signifies the count of LSP.
        - LspType (str()): The type of multicast LSP.
        - RootAddrStep (str): The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        - RootAddress (str): The root address of the multicast LSP.
        - RootAddressCount (number): The root address count for this Multicast FEC range.

        Returns
        -------
        - self: This instance with matching multicastRootRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastRootRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastRootRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
