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


class TxLane(Base):
    """This object contains the TxLane parameters.
    The TxLane class encapsulates a required txLane resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "txLane"
    _SDM_ATT_MAP = {
        "IsSkewSynchronized": "isSkewSynchronized",
        "LaneMappingType": "laneMappingType",
        "MaxSkewVal": "maxSkewVal",
        "MinSkewVal": "minSkewVal",
        "NoOfLanes": "noOfLanes",
        "PcsLane": "pcsLane",
        "PhysicalLanes": "physicalLanes",
        "Resolution": "resolution",
        "SkewValues": "skewValues",
        "SynchronizedSkewVal": "synchronizedSkewVal",
    }
    _SDM_ENUM_MAP = {
        "laneMappingType": ["default", "increment", "decrement", "custom", "random"],
    }

    def __init__(self, parent, list_op=False):
        super(TxLane, self).__init__(parent, list_op)

    @property
    def IsSkewSynchronized(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, skew value will apply for all the lanes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsSkewSynchronized"])

    @IsSkewSynchronized.setter
    def IsSkewSynchronized(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsSkewSynchronized"], value)

    @property
    def LaneMappingType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(default | increment | decrement | custom | random): Lane Mapping
        """
        return self._get_attribute(self._SDM_ATT_MAP["LaneMappingType"])

    @LaneMappingType.setter
    def LaneMappingType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LaneMappingType"], value)

    @property
    def MaxSkewVal(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxSkewVal"])

    @property
    def MinSkewVal(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinSkewVal"])

    @property
    def NoOfLanes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of lanes
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfLanes"])

    @property
    def PcsLane(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Pcs Lane
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsLane"])

    @PcsLane.setter
    def PcsLane(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsLane"], value)

    @property
    def PhysicalLanes(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str):
        """
        return self._get_attribute(self._SDM_ATT_MAP["PhysicalLanes"])

    @property
    def Resolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Resolution"])

    @property
    def SkewValues(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Skew Values
        """
        return self._get_attribute(self._SDM_ATT_MAP["SkewValues"])

    @SkewValues.setter
    def SkewValues(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SkewValues"], value)

    @property
    def SynchronizedSkewVal(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Synchronized Skew Values
        """
        return self._get_attribute(self._SDM_ATT_MAP["SynchronizedSkewVal"])

    @SynchronizedSkewVal.setter
    def SynchronizedSkewVal(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SynchronizedSkewVal"], value)

    def update(
        self,
        IsSkewSynchronized=None,
        LaneMappingType=None,
        PcsLane=None,
        SkewValues=None,
        SynchronizedSkewVal=None,
    ):
        # type: (bool, str, List[int], List[int], int) -> TxLane
        """Updates txLane resource on the server.

        Args
        ----
        - IsSkewSynchronized (bool): If true, skew value will apply for all the lanes.
        - LaneMappingType (str(default | increment | decrement | custom | random)): Lane Mapping
        - PcsLane (list(number)): Pcs Lane
        - SkewValues (list(number)): Skew Values
        - SynchronizedSkewVal (number): Synchronized Skew Values

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        IsSkewSynchronized=None,
        LaneMappingType=None,
        MaxSkewVal=None,
        MinSkewVal=None,
        NoOfLanes=None,
        PcsLane=None,
        PhysicalLanes=None,
        Resolution=None,
        SkewValues=None,
        SynchronizedSkewVal=None,
    ):
        # type: (bool, str, int, int, int, List[int], List[str], int, List[int], int) -> TxLane
        """Finds and retrieves txLane resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve txLane resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all txLane resources from the server.

        Args
        ----
        - IsSkewSynchronized (bool): If true, skew value will apply for all the lanes.
        - LaneMappingType (str(default | increment | decrement | custom | random)): Lane Mapping
        - MaxSkewVal (number):
        - MinSkewVal (number):
        - NoOfLanes (number): Number of lanes
        - PcsLane (list(number)): Pcs Lane
        - PhysicalLanes (list(str)):
        - Resolution (number):
        - SkewValues (list(number)): Skew Values
        - SynchronizedSkewVal (number): Synchronized Skew Values

        Returns
        -------
        - self: This instance with matching txLane resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of txLane data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the txLane resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
