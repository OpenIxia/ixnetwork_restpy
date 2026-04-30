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


class Priority(Base):
    """
    The Priority class encapsulates a list of priority resources that are managed by the system.
    A list of resources can be retrieved from the server using the Priority.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "priority"
    _SDM_ATT_MAP = {
        "BufferSize": "bufferSize",
        "ConsumptionRate": "consumptionRate",
        "DscpMapping": "dscpMapping",
        "EnablePFCPriority": "enablePFCPriority",
        "PfcPriority": "pfcPriority",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Priority, self).__init__(parent, list_op)

    @property
    def BufferSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Buffer size in Kb
        """
        return self._get_attribute(self._SDM_ATT_MAP["BufferSize"])

    @BufferSize.setter
    def BufferSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BufferSize"], value)

    @property
    def ConsumptionRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Consumption Rate (% of front panel line rate)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConsumptionRate"])

    @ConsumptionRate.setter
    def ConsumptionRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConsumptionRate"], value)

    @property
    def DscpMapping(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Mapped dscp value ranges Ex. 0-50,53-58,60,62
        """
        return self._get_attribute(self._SDM_ATT_MAP["DscpMapping"])

    @DscpMapping.setter
    def DscpMapping(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DscpMapping"], value)

    @property
    def EnablePFCPriority(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, PFC priority to dscp mapping enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePFCPriority"])

    @EnablePFCPriority.setter
    def EnablePFCPriority(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePFCPriority"], value)

    @property
    def PfcPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: PFC Priority
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority"])

    def update(
        self,
        BufferSize=None,
        ConsumptionRate=None,
        DscpMapping=None,
        EnablePFCPriority=None,
    ):
        # type: (int, int, str, bool) -> Priority
        """Updates priority resource on the server.

        Args
        ----
        - BufferSize (number): Buffer size in Kb
        - ConsumptionRate (number): Consumption Rate (% of front panel line rate)
        - DscpMapping (str): Mapped dscp value ranges Ex. 0-50,53-58,60,62
        - EnablePFCPriority (bool): If true, PFC priority to dscp mapping enabled.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        BufferSize=None,
        ConsumptionRate=None,
        DscpMapping=None,
        EnablePFCPriority=None,
    ):
        # type: (int, int, str, bool) -> Priority
        """Adds a new priority resource on the json, only valid with batch add utility

        Args
        ----
        - BufferSize (number): Buffer size in Kb
        - ConsumptionRate (number): Consumption Rate (% of front panel line rate)
        - DscpMapping (str): Mapped dscp value ranges Ex. 0-50,53-58,60,62
        - EnablePFCPriority (bool): If true, PFC priority to dscp mapping enabled.

        Returns
        -------
        - self: This instance with all currently retrieved priority resources using find and the newly added priority resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BufferSize=None,
        ConsumptionRate=None,
        DscpMapping=None,
        EnablePFCPriority=None,
        PfcPriority=None,
    ):
        # type: (int, int, str, bool, int) -> Priority
        """Finds and retrieves priority resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve priority resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all priority resources from the server.

        Args
        ----
        - BufferSize (number): Buffer size in Kb
        - ConsumptionRate (number): Consumption Rate (% of front panel line rate)
        - DscpMapping (str): Mapped dscp value ranges Ex. 0-50,53-58,60,62
        - EnablePFCPriority (bool): If true, PFC priority to dscp mapping enabled.
        - PfcPriority (number): PFC Priority

        Returns
        -------
        - self: This instance with matching priority resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of priority data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the priority resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
