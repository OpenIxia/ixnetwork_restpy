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


class PfcPauseGeneration(Base):
    """
    The PfcPauseGeneration class encapsulates a required pfcPauseGeneration resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pfcPauseGeneration"
    _SDM_ATT_MAP = {
        "DestAddress": "destAddress",
        "EnablePFCPause": "enablePFCPause",
        "HighThreshold": "highThreshold",
        "LowThreshold": "lowThreshold",
        "SrcAddress": "srcAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PfcPauseGeneration, self).__init__(parent, list_op)

    @property
    def Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.starfourhundredgiglan.pfcpausegeneration.priority.priority.Priority): An instance of the Priority class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.starfourhundredgiglan.pfcpausegeneration.priority.priority import (
            Priority,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Priority", None) is not None:
                return self._properties.get("Priority")
        return Priority(self)

    @property
    def DestAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Destination MAC Address
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestAddress"])

    @DestAddress.setter
    def DestAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestAddress"], value)

    @property
    def EnablePFCPause(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, PFC pause generation is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePFCPause"])

    @EnablePFCPause.setter
    def EnablePFCPause(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePFCPause"], value)

    @property
    def HighThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Pause High Threshold - Pause is started reaching this limit
        """
        return self._get_attribute(self._SDM_ATT_MAP["HighThreshold"])

    @HighThreshold.setter
    def HighThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HighThreshold"], value)

    @property
    def LowThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Pause Low Threshold - Pause is stopp reaching this limit
        """
        return self._get_attribute(self._SDM_ATT_MAP["LowThreshold"])

    @LowThreshold.setter
    def LowThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LowThreshold"], value)

    @property
    def SrcAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Source MAC Address
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcAddress"])

    @SrcAddress.setter
    def SrcAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcAddress"], value)

    def update(
        self,
        DestAddress=None,
        EnablePFCPause=None,
        HighThreshold=None,
        LowThreshold=None,
        SrcAddress=None,
    ):
        # type: (str, bool, int, int, str) -> PfcPauseGeneration
        """Updates pfcPauseGeneration resource on the server.

        Args
        ----
        - DestAddress (str): Destination MAC Address
        - EnablePFCPause (bool): If true, PFC pause generation is enabled.
        - HighThreshold (number): Pause High Threshold - Pause is started reaching this limit
        - LowThreshold (number): Pause Low Threshold - Pause is stopp reaching this limit
        - SrcAddress (str): Source MAC Address

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DestAddress=None,
        EnablePFCPause=None,
        HighThreshold=None,
        LowThreshold=None,
        SrcAddress=None,
    ):
        # type: (str, bool, int, int, str) -> PfcPauseGeneration
        """Finds and retrieves pfcPauseGeneration resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pfcPauseGeneration resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pfcPauseGeneration resources from the server.

        Args
        ----
        - DestAddress (str): Destination MAC Address
        - EnablePFCPause (bool): If true, PFC pause generation is enabled.
        - HighThreshold (number): Pause High Threshold - Pause is started reaching this limit
        - LowThreshold (number): Pause Low Threshold - Pause is stopp reaching this limit
        - SrcAddress (str): Source MAC Address

        Returns
        -------
        - self: This instance with matching pfcPauseGeneration resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pfcPauseGeneration data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pfcPauseGeneration resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
